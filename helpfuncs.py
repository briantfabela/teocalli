from random import choice

def load_txt(file_name):
    '''Loads a text file and returns it as a string'''

    f = open(file_name, 'r')
    text_str = f.read()
    f.close()

    return text_str

def load_events_txt(txt_str, event_type):
    '''Loads a string containing the full text and returns the section'''

    event_type = f"### {event_type} ###"

    events_str = txt_str.split(event_type)[1].split(event_type)[0].strip('\n')

    return events_str

def get_random_line(txt_str):
    '''Strips whitespace and extra line and returns a random line from str'''

    return choice(txt_str.split('\n'))

def test():
    print(get_random_line(load_events_txt(load_txt('events.txt'), 'LOOT EVENTS')))