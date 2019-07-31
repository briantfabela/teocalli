from random import choice, choices

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
    '''Strips whitespace and extra line and returns a random line from str'''

    return choice(txt_str.split('\n'))

# will test the above functions so that they are producing the expected output
def test():
    print(get_random_line(load_events_txt(load_txt('events.txt'), 'LOOT EVENTS')))

def choose_event_type(difficulty='normal'):
    '''Returns an Event type with weighted probabilities based on difficulty'''

    if difficulty is 'normal':
        # events order: loot, big loot, xp, risk, hurt, booby traps
        weight = [0.35, 0.1, 0.2, 0.15, 0.15, 0.05]

    return choices(['LOOT', 'BIG LOOT', 'XP', 'RISK', 'HURT', 'BOOBY TRAP'],
                    weight)[0]

def test2():
    txt = load_txt('events.txt')
    for i in range(20):
        event_type = choose_event_type()
        event_line = get_random_line(load_events_txt(txt, event_type))
        print(f"{event_type}: {event_line}")