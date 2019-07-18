from random import choice, randint, random

class Archeologist:
    '''Archeologist contains name, hp, xp, inventory, current & visited site'''

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0

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

        for i in range(randint(1, 3)): # generate a total inventory for loot
            self.addToInventory({choice(materials):randint(1, 5)}, loot_droped)

        # add loot_dropped to site.site_loot
        self.addToInventory(loot_droped, self.current_site.site_loot)

        # TODO: consider triggering an 'Event' isntance with its unique events
        # aquire xp
        # loose some hp
        # print loot() events to console
        # end fuicntion

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
        pass

    def leave_site(self):
        '''leave temple, add total loot to inventory'''

        # add site inventory to self.inventory
        # reset self.hp
        # print total loot aquired at site, xp gained
        # print current inventory
        self.enter_site()

class Site:

    def __init__(self, name=''):
        '''lorem ipsum'''

        if not name:
            self.name = self.site_name_gen()
        else:
            self.name = name

        self.risk = 0
        self.total_loot_collected = {} # total loot

        # legenday artifact TODO: add way to aquire legend artifact, make class
        self.legend_art = '' # generate a name 'golden jaguar of {self.name}'
        self.legend_art_rarity = randint(0, 5)
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

    def __init__(self, site_name=''):
        self.name = 'The '

        if random() > 0.5:
            # assign an adjective describing appearance or attitude eg 'Angry'
            words = 'Ugly/Weird/Great/Fat/Old/Young/Shiny/Bright/Bloody/'\
                    'Adorable/Fragile/Crazy/Loco/Crooked/Terrible/Cruel'\
                    'Magestic/Hissing/Little/Round/Screaming/Hunched/Tiny'\
                    'Ancient/Brittle'

            self.name += choice(words.split('/')) + ' ' # add word to name
        
        adjectives = 'Golden/Yellow/Gold/Silver/Gray/Crystal/Red/Green/Blue'\
                     'Black/White/Gray/Jade/Obsidian/Turquoise/Clay/Rock/Stone'

        self.name += choice(adjectives.split('/')) + ' ' # add adjective

        nouns = 'Man/Hombre/Child/Woman/Dog/Perro/Bowl/Jar/Jars/Pot/Plate/'\
                'Plates/Teen/Virgin/Duck/Quetzal/Serpent/Eagle/Jaguar/Men/'\
                'Priest/Priests/Sun/Moon/Calendar/Quetzalcoatl/Tlaloc/Acan/'\
                'God/Itzamna/Shaman/Xolo/Mixocoatl/Patecatl/Tlatoani/Star/'\
                'Huitzilopoxtli/Cocoa/Bean/Baby/Lady Xoc/Ahau/Ajaw/Pakal'

        self.name += choice(nouns.split('/'))