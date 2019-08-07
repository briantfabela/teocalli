from random import choice, randint, random
from event_cards import EventCard
from helpfuncs import add_up_loot
import sites

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

        event_card = EventCard()

        # TODO: Actualize xp_gain, site_xp, hp_loss
        self.update_stats(event_card)

        # generate a chance to aquire the site's legendary loot
        if not self.current_site.legend_art_collect: # if not yet collected
            if random() >= 0.95: # approx. 5% chance to collect
                self.current_site.legend_artif.print_found()
                self.current_site.site_loot = add_up_loot(
                                    {self.current_site.legend_artif.name : 1},
                                    self.current_site.site_loot)
                self.current_site.legend_art_collect = True

        # add all collected loot thus far to self.current_site.site_loot
        self.current_site.site_loot = add_up_loot(event_card.loot,
                                                self.current_site.site_loot)

        self.loot_print(event_card.risk_change, event_card.hp_change,
                        event_card.xp_gain, event_card.loot, event_card.text)

    # TODO: Consider adding medkits, torches, antidotes, and ropes to the game

    def loot_print(self, risk_gain, hp_loss, xp_gain, loot_droped, txt):
        '''Print self.loot() events to console'''

        event_str = f"{txt}\n" # stores the string which will be printed at end

        # 1st Line: Risk Gain and/or HP Loss and XP gain
        if risk_gain:
            event_str += f"+{risk_gain}% risk\n" # risk gain
        elif hp_loss:
            event_str += f"{hp_loss} HP\n" # hp loss
        elif xp_gain:
            event_str += f"+{xp_gain} XP\n"

        # 2nd Line: Total Risk & total HP loss
        event_str += f"Total Risk: {self.current_site.risk}%, HP: {self.hp}, "\
                     f"Site XP: {self.current_site.xp_earned}\n"

        # event card loot
        if loot_droped:
            event_str += "Loot:\n"
            for item, amount in loot_droped.items():
                event_str += f"\t{item}: {amount}\n"

        # end function
        print(event_str)

    def update_stats(self, event_card):
        '''actualize xp_gain, site_xp, hp_loss'''
        
        pass

    def enter_site(self):
        '''enter new temple'''

        # generate a site instance and assign it to self.current_site
        new_site = sites.Site()
        print(f"Welcome to {new_site.name}!\n")

        return new_site

    def leave_site(self):
        '''Leave temple, add total loot to inventory'''

        # add site inventory to player's inventory -> (self.inventory)
        add_up_loot(self.current_site.site_loot, self.inventory)

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