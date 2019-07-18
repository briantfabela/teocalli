from random import choice, randint

class archeologist:
    '''lorem ipsum'''

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0

        # inventory dictionary -> {'gold': 13, 'silver': 32, 'rope': 2}
        self.inventory = {}

    def loot(self):
        '''Generate a dict of loot items based on location and player skills'''

        loot_droped = {}
        materials = ['gold', 'silver', 'jade', 'obsidian', 'turquoise']
        # add amethyst, pearls, emerald <- rarer but not necessarily more val

        for i in range(randint(1, 3)): # generate a total inventory for loot
            self.addToInventory({choice(materials):randint(1, 5)}, loot_droped)

        self.addToInventory(loot_droped, self.inventory) # add loot to player

    def addToInventory(self, loot, inventory):
        '''Take a loot dictionary and add its items to inventory dict'''

        for item, amount in loot.items(): # for each item in loot dict
            if item not in inventory:
                inventory[item] = amount # inventory['item'] = n
            else: # if item in inventory
                inventory[item] += amount # add amount of loot to existing

        return inventory

class site:

    def __init__(self, name=''):
        
        if not name:
            self.name = self.site_name_gen()
        else:
            self.name = name

        self.risk = {}
        self.total_loot_collected = {} # total loot

        # legenday artifact TODO: add way to aquire legend artifact, make class
        self.legend_art = '' # generate a name 'golden jaguar of {self.name}'
        self.legend_art_rarity = randint(0, 5)
        self.legend_art_collect = False # has the item been aquired by player?

    def site_name_gen(self):
        '''Name generation from two words'''

        # 12 x 27 = 324 unique combinations
        pre = 'Maza/Mixi/Mequi/Tla/Tepi/Zaca/Xoqui/Xi/Ana/Eli/Chico/Chipo'
        post= 'can/che/kun/pan/tuk/que/kal/pak/tza/tan/tecal/huaca/co/zingo/yuca/'\
            'pali/yotl/chiqui/catl/huani/coatl/latl/lolco/matl/tatl/huapa/tl'

        return choice(pre.split('/')) + choice(post.split('/'))