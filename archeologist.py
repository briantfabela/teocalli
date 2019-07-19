from random import choice, randint, random

class Archeologist:
    '''Archeologist contains name, hp, xp, inventory, current & visited site'''

    def __init__(self, name):
        self.name = name
        self.base_hp = 100 # base hp a player has when starting site
        self.hp = 100 # Tracks ongoing 'current' hp. Always > 0.
        self.xp = 0 # total xp earned by the player

        # inventory dictionary -> {'gold': 13, 'silver': 32, 'rope': 2}
        self.inventory = {}

        # history of sites visited along with loot collected there
        self.site_history = [] # ('site': <Site>)
        
        # enter first site
        self.current_site = self.enter_site() # new site

    def loot(self):
        '''Generate a dict of loot items based on location and player skills'''

        loot_droped = {}
        materials = ['gold', 'silver', 'jade', 'obsidian', 'turquoise']
        # add amethyst, pearls, emerald <- rarer but not necessarily more val

        for _ in range(randint(1, 3)): # generate a total inventory for loot
            self.addToInventory({choice(materials):randint(1, 3)}, loot_droped)

        # TODO: consider triggering an 'Event' instance with its unique events

        # aquire xp
        xp_drop = randint(1, 5)
        # TODO: make the probability dependant on a player skill
        if random() > 0.85 :
            xp_drop += randint(5, 10)

        self.current_site.xp_earned += xp_drop
        self.xp += xp_drop

        # loose some hp; based on risk
        hp_loss = 0
        if random() * 100 <= self.current_site.risk:
            max_dmg = 2 + self.current_site.risk //  10 # 2 - risk // 10
            hp_loss += round(randint(1, max_dmg) * 
                       (1 + self.current_site.risk / 100))
            self.hp -= hp_loss

        # increase site risk
        risk_gain = 0
        if random() < 0.6: # consider skill that reduces likelyhood of increase
            risk_gain += randint(1, 5) # cosnider skill that mitigates max gain
            self.current_site.risk += risk_gain

        # generate a chance to aquire the site's legendary loot
        if not self.current_site.legend_art_collect: # if not yet collected
            if random() >= 0.95: # make a player's skill affect this prob
                # print artifact discovery event to console
                print(f"You found {self.current_site.legend_artif.name_full}!")
                print(f"This is a *{self.current_site.legend_artif.rarity}* "\
                       "item")
                self.addToInventory({self.current_site.legend_artif.name : 1},
                                    loot_droped)
                self.current_site.legend_art_collect = True

        # add all collected loot thus far to self.current_site.site_loot
        self.addToInventory(loot_droped, self.current_site.site_loot)

        # print loot() events to console: risk, hp, total risk, total hp, etc
        # TODO: make this its own function
        event_str = ''

        # 1st Line: Risk Gain and/or HP Loss and XP gain
        if hp_loss and risk_gain:
            event_str += f"+{risk_gain}% risk, -{hp_loss} HP"
        elif risk_gain:
            event_str += f"+{risk_gain}% risk" # xp gain
        elif hp_loss:
            event_str += f"-{hp_loss} HP" # hp loss

        if len(event_str): event_str+=", " # if the string has no xp or hp stats
        event_str += f"+{xp_drop} XP\n" # add xp gain

        # 2nd Line: Total Risk & total HP loss
        event_str += f"Total Risk: {self.current_site.risk}%, HP: {self.hp}, "\
                     f"Site XP: {self.current_site.xp_earned}\n"

        # rest of string's lines: Loot dropped
        event_str += "Loot:\n"
        for item, amount in loot_droped.items():
            event_str += f"\t{item}: {amount}\n"

        # end fuicntion
        print(event_str)
        
    # TODO: Consider adding medkits, torches, antidotes, and ropes to the game

    def addToInventory(self, loot, inventory):
        '''Take a loot dictionary and add its items to inventory dict'''

        for item, amount in loot.items(): # for each item in loot dict
            if item not in inventory:
                inventory[item] = amount # inventory['item'] = n
            else: # if item in inventory
                inventory[item] += amount # add amount of loot to existing

        return inventory

    def enter_site(self):
        '''enter new temple'''

        # generate a site instance and assign it to self.current_site
        new_site = Site()
        print(f"Welcome to {new_site.name}!\n")
        return new_site

    def leave_site(self):
        '''Leave temple, add total loot to inventory'''

        # add site inventory to player's inventory -> (self.inventory)
        self.addToInventory(self.current_site, self.inventory)

        # reset self.hp to self.base_hp
        self.hp = self.base_hp

        # print total loot aquired at site, xp gained
        print(f"Loot Collected at {self.current_site.name}:\n")
        for item, amount in self.current_site.site_loot.items():
            f"\t{item}: {amount}\n"

        # print total current inventory
        print(f"Total Player Loot:\n")
        for item, amount in self.inventory.items():
            f"\t{item}: {amount}\n"

        # TODO: add site exited to self.site_history -> ('site': <Site>)

        # enter a new site
        self.enter_site()

class Site:

    def __init__(self, name=''):
        '''lorem ipsum'''

        if not name:
            self.name = self.site_name_gen()
        else:
            self.name = name

        self.risk = 0 # higher risk = more likely to loose hp, more hp loss

        # legenday artifact of the Site; unique to location
        self.legend_artif = Artifact(self.name) # generate unique artif to site
        self.legend_art_collect = False # has the item been aquired by player?

        # player attributes while in the site
        self.xp_earned = 0
        self.site_loot = {}

    def site_name_gen(self):
        '''Name generation from two words'''

        # 12 x 27 = 324 unique combinations
        pre = 'Maza/Mixi/Mequi/Tla/Tepi/Zaca/Xoqui/Xi/Ana/Eli/Chico/Chipo'
        post= 'can/che/kun/pan/tuk/que/kal/pak/tza/tan/tecal/huaca/co/zingo/yuca/'\
              'pali/yotl/chiqui/catl/huani/coatl/latl/lolco/matl/tatl/huapa/tl'

        return choice(pre.split('/')) + choice(post.split('/'))

class Artifact:
    '''Artifact unique to the site visited'''

    def __init__(self, site_name='', pre_adjective = False):

        self.name = 'The '

        if random() > 0.65 or pre_adjective:
            # assign an adjective describing appearance or attitude eg 'Angry'
            # if pre_adjective is True, this will be added despite random()
            words = 'Ugly/Weird/Great/Fat/Old/Young/Shiny/Bright/Bloody/'\
                    'Adorable/Fragile/Crazy/Loco/Crooked/Terrible/Cruel/'\
                    'Magestic/Hissing/Little/Round/Screaming/Hunched/Tiny/'\
                    'Ancient/Brittle/Phalic'

            self.name += choice(words.split('/')) + ' ' # add word to name
        
        adjectives = 'Golden/Yellow/Gold/Silver/Gray/Crystal/Red/Green/Blue/'\
                     'Black/White/Gray/Jade/Obsidian/Turquoise/Clay/Rock/Stone'

        self.name += choice(adjectives.split('/')) + ' ' # add adjective

        nouns = 'Man/Hombre/Child/Woman/Dog/Perro/Bowl/Jar/Jars/Pot/Plate/'\
                'Plates/Teen/Virgin/Duck/Quetzal/Serpent/Eagle/Jaguar/Men/'\
                'Priest/Priests/Sun/Moon/Calendar/Quetzalcoatl/Tlaloc/Acan/'\
                'God/Itzamna/Shaman/Xolo/Mixocoatl/Patecatl/Tlatoani/Star/'\
                'Huitzilopoxtli/Cocoa/Bean/Baby/Lady Xoc/Ahau/Ajaw/Pakal/'\
                'Tablet/Stelae/Mother/Mothers/Sister/Sisters/Lady/Warrior'

        self.name += choice(nouns.split('/'))

        if site_name: # if site name was given
            self.name_full = self.name + ' of ' + site_name

        self.rarity = self.get_ratity()

    def get_ratity(self):
        '''Assigns rarity value to an artifact'''
        rarity_list = [] # we will append rarities here and choose() them

        # TODO: consider making the probabilities modifyable via func parameter
        rarity_list.extend(['Noteworthy'] * 40) # % 80
        rarity_list.extend(['Rare'] * 9)      # % 18
        rarity_list.extend(['Legendary'])     # % 2

        return choice(rarity_list)