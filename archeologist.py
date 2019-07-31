from random import choice, randint, random
import sites
import event
import helpfuncs

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
        self.site_history = [] # (site.name: <Site>)

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

        ### THIS AREA WILL BE REPLACES BY EVENETS ###
        
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
            risk_gain += randint(1, 3) # cosnider skill that mitigates max gain
            self.current_site.risk += risk_gain

        ### THIS AREA WILL BE REPLACES BY EVENETS ###

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

        self.loot_print(risk_gain, hp_loss, xp_drop, loot_droped)

    # TODO: Consider adding medkits, torches, antidotes, and ropes to the game

    def loot_print(self, risk_gain, hp_loss, xp_drop, loot_droped):
        '''Print self.loot() events to console'''
        event_str = '' # stores the string to be printed. For concatenation.

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

        # end function
        print(event_str)

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
        new_site = sites.Site()
        print(f"Welcome to {new_site.name}!\n")

        return new_site

    def leave_site(self):
        '''Leave temple, add total loot to inventory'''

        # add site inventory to player's inventory -> (self.inventory)
        self.addToInventory(self.current_site.site_loot, self.inventory)

        # reset self.hp to self.base_hp
        self.hp = self.base_hp

        # print total loot aquired at site, xp gained
        print(f"Loot Collected at {self.current_site.name}:\n")
        for item, amount in sorted(self.current_site.site_loot.items()):
            print(f"\t{item}: {amount}")
        print('\n')

        # print total current inventory
        print(f"Total Player Loot:\n")
        for item, amount in sorted(self.inventory.items()):
            print(f"\t{item}: {amount}")
        print('\n')

        # add site exited to self.site_history -> ('site': <Site>)
        self.site_history.append((self.current_site.name, self.current_site))

        # enter a new site
        self.current_site = self.enter_site()