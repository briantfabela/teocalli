from random import choice, randint, random
from helpfuncs import choose_event_type, get_event_txt, add_up_loot

class EventCard:

    def __init__(self, event_type='', txt='', xp=0, hp=0, risk=0, loot={}):
        '''Generates an eventgenerates and event with appropriate attributes'''

        self.loot = loot
        self.hp_change = hp
        self.risk_change = risk
        self.xp_gain = xp

        # type assignment
        if event_type:
            self.type = event_type
        else:
            self.type = choose_event_type() # difficulty alters weights

        # text assignment, based on type
        if txt:
            self.text = txt
        else:
            self.text = get_event_txt(self.type)

        # assign loot, xp, hp changes, etc as per event type
        # event types: 'LOOT', 'BIG LOOT', 'XP', 'RISK', 'HURT', 'BOOBY TRAP'

        if self.type is 'LOOT':
            materials = ['gold', 'silver', 'jade', 'obsidian', 'turquoise']

            total_loot = {}

            for _ in range(randint(1, 3)): # generate loot
                add_up_loot({choice(materials) : randint(1, 3)}, total_loot)

            self.loot = add_up_loot(total_loot, self.loot)

            # TODO: consider assigning xp and risk in loot events

        elif self.type is 'BIG LOOT':
            materials = ['gold', 'silver', 'jade', 'obsidian', 'turquoise']

            total_loot = {}

            for _ in range(randint(4, 6)): # generate loot
                add_up_loot({choice(materials) : randint(1, 3)}, total_loot)

            self.loot = add_up_loot(total_loot, self.loot)

        elif self.type is 'XP':
            self.xp_gain += randint(1, 5)

            if random() > 0.8:
                self.xp_gain += randint(5, 10)

        elif self.type is 'RISK':
            self.risk_change += randint(2, 5)

        # TODO: make HP LOSS events more dynamic
        elif self.type is 'HURT':
            self.hp_change -= randint(1, 5) 

        elif self.type is 'BOOBY TRAP':
            self.hp_change -= randint(6, 12)