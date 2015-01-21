import time


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_available_people(spatula, filepath):
    available_people = []
    valid_people = False
    while not valid_people:
        available_people_input = input('Who is available to pair today?\n')
        available_people = spatula.get_people(available_people_input)
        if len(available_people) > 0:
            valid_people = True
        else:
            print(Colors.WARNING + 'No one?')
            print('Certainly you made a mistake...' + Colors.ENDC)
            print(Colors.FAIL + 'Yes. You made a mistake. Let me ask you again.' + Colors.ENDC)

    print('\nWould you like me to remember these people? (y/n)')
    remember = input()
    if remember.lower() == 'y':
        save_names(filepath, available_people)

    return available_people


def save_names(filepath, people):
    with open(filepath, 'w') as settings:
        for person in people:
            settings.write(person + ' ')
        settings.close()


def cool_whip(spatula, filepath, people):
    incorrect = True
    while incorrect:
        print(Colors.OKGREEN + '\nCool! These are the people I know right now:' + Colors.ENDC)
        print(Colors.OKBLUE + people.__str__() + Colors.ENDC)
        y_or_n = False
        while not y_or_n:
            print('Is that correct? (y/n)')
            response = input()
            if response.lower() == 'y':
                y_or_n = True
                incorrect = False
            elif response.lower() == 'n':
                y_or_n = True
                print('\nOh? Well let\'s try again, shall we?')
                people = get_available_people(spatula, filepath)
            else:
                print(Colors.FAIL + 'Sorry, but this is the one time I actually require \'y\' or \'n\'' + Colors.ENDC)

    return people


def display_pairs(pairs):
    for index in range(len(pairs)):
        pair = pairs[index]
        person_one = pair[0]
        if len(pair) > 1:
            person_two = pair[1]
            print(Colors.OKBLUE + person_one + ' and ' + person_two + Colors.ENDC)
        else:
            print(Colors.OKBLUE + person_one + ' alone' + Colors.ENDC)


def put_a_fork_in_it():
    print('Terminating, please wait...')
    time.sleep(1)
    print('import Skynet')
    print('Attempting to terminate Sarah Conner...')
    time.sleep(1)
    print('I\'ll be back.')
    time.sleep(1)