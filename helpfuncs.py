from random import choice, choices

# TEXT PROCESSING, RETRIEVAL FUNCS

def load_txt(file_name):
    '''Loads a text file and returns it as a string'''

    f = open(file_name, 'r') # read file
    text_str = f.read()
    f.close()

    return text_str

def load_events_txt(txt_str, event_type):
    '''Loads a string containing the full text and returns the section'''

    event_type = f"### {event_type} EVENTS ###"

    events_str = txt_str.split(event_type)[1].split(event_type)[0].strip('\n')

    return events_str

def get_random_line(txt_str):
    '''Returns a random line from str'''

    return choice(txt_str.split('\n'))

def get_event_txt(event_type):
    '''Provides a random event text given the event type'''

    event_type_text = load_events_txt(load_txt('events.txt'), event_type)
    
    return get_random_line(event_type_text)

# EVENT HELP FUNCS
# TODO: assign the diffulty value to a new object type 'Settings'

def choose_event_type(difficulty='normal'):
    '''Returns an Event type with weighted probabilities based on difficulty'''

    if difficulty is 'normal':
        # events order: loot, big loot, xp, risk, hurt, booby traps
        weight = [0.35, 0.1, 0.2, 0.15, 0.15, 0.05]
    elif difficulty is 'hard':
        weight = [0.25, 0.05, 0.2, 0.2, 0.2, 0.1]

    return choices(['LOOT', 'BIG LOOT', 'XP', 'RISK', 'HURT', 'BOOBY TRAP'],
                    weight)[0]

# DICTIONARY INVENTORY MANAGEMENT

def add_up_loot(loot, final_inventory):
    '''Combines and returns the items from two inventory dicts'''

    for item, amount in loot.items():
            if item not in final_inventory: # if item is new
                final_inventory[item] = amount
            else: # if item exists on both dicts
                final_inventory[item] += amount

    return final_inventory

#    def addToInventory(self, loot, inventory):
#        '''Take a loot dictionary and add its items to inventory dict'''
#
#        for item, amount in loot.items(): # for each item in loot dict
#            if item not in inventory:
#                inventory[item] = amount # inventory['item'] = n
#            else: # if item in inventory
#                inventory[item] += amount # add amount of loot to existing
#
#        return inventory