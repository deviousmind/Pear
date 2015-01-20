import time


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