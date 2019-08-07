from random import choice, random

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
        post= 'can/che/kun/pan/tuk/que/kal/pak/tza/tan/tecal/huaca/co/zingo/'\
              'yuca/pali/yotl/chiqui/catl/huani/coatl/latl/lolco/matl/tatl/'\
              'huapa/hualpa/tl'

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
                    'Ancient/Brittle/Phalic/Smiling/Weeping/Royal'

            self.name += choice(words.split('/')) + ' ' # add word to name
        
        adjectives = 'Golden/Yellow/Gold/Silver/Gray/Crystal/Red/Green/Blue/'\
                     'Black/White/Gray/Jade/Obsidian/Turquoise/Clay/Rock/Stone'

        self.name += choice(adjectives.split('/')) + ' ' # add adjective

        nouns = 'Man/Hombre/Child/Woman/Dog/Perro/Bowl/Jar/Jars/Pot/Plate/'\
                'Plates/Teen/Virgin/Duck/Quetzal/Serpent/Eagle/Jaguar/Men/'\
                'Priest/Priests/Sun/Moon/Calendar/Quetzalcoatl/Tlaloc/Acan/'\
                'God/Itzamna/Shaman/Xolo/Mixocoatl/Patecatl/Tlatoani/Star/'\
                'Huitzilopoxtli/Cocoa/Bean/Baby/Lady Xoc/Ahau/Ajaw/Pakal/'\
                'Tablet/Stelae/Mother/Mothers/Sister/Sisters/Lady/Warrior/'\
                'Flower/Coyotl/Tamale/Cactus/Bird/Deity/Ruler'

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

    def print_found(self):
        '''Print the artifact's name and rarity when found'''

        print(f"You found {self.name_full}!\nThis is a *{self.rarity}* item")


#print(f"You found {self.current_site.legend_artif.name_full}!")
#print(f"This is a *{self.current_site.legend_artif.rarity}* "\
#       "item")