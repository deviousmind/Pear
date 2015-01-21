import time


def get_available_people(spatula, filepath):
    available_people = []
    valid_people = False
    while not valid_people:
        available_people_input = input('Who is available to pair today?\n')
        available_people = spatula.get_people(available_people_input)
        if len(available_people) > 0:
            valid_people = True
        else:
            print('No one?')
            print('Certainly you made a mistake...')
            print('Yes. You made a mistake. Let me ask you again.')

    print('\nWould you like me to remember these people? (y/n)')
    remember = input()
    if remember.lower() == 'y':
        with open(filepath, 'w') as settings:
            for person in available_people:
                settings.write(person + ' ')
            settings.close()

    return available_people

def display_pairs(pairs):
    for index in range(len(pairs)):
        pair = pairs[index]
        person_one = pair[0]
        if len(pair) > 1:
            person_two = pair[1]
            print(person_one + ' and ' + person_two)
        else:
            print(person_one + ' alone')


def put_a_fork_in_it():
    print('Terminating, please wait...')
    time.sleep(1)
    print('import Skynet')
    print('Attempting to terminate Sarah Conner...')
    time.sleep(1)
    print('I\'ll be back.')
    time.sleep(1)