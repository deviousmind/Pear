import time
import os
from Crust import decorator


def prepare():
    filepath = os.getenv('APPDATA') + '\\Pear'
    filename = 'pear.txt'
    full_path = filepath + '\\' + filename

    if not os.path.exists(filepath):
        os.makedirs(filepath)

    return full_path


def cut(people, incompatible, pear):
    while True:
        pairs = pear.create_pairs(people, incompatible)
        print('\nHow about this?\n')
        display_pairs(pairs)
        print(decorator.request('\nOr should I try again? (y/n)'))
        response = input()

        if response.lower() != 'y':
            print()
            break


def display_pairs(pairs):
    for index in range(len(pairs)):
        pair = pairs[index]
        person_one = pair[0]
        if len(pair) > 1:
            person_two = pair[1]
            print(decorator.attention(person_one + ' and ' + person_two))
        else:
            print(decorator.attention(person_one + ' alone'))


def put_a_fork_in_it():
    print(decorator.warn('Terminating, please wait...'))
    time.sleep(1)
    print(decorator.warn('import Skynet'))
    print(decorator.warn('Attempting to terminate Sarah Conner...'))
    time.sleep(1)
    print(decorator.warn('I\'ll be back.'))
    time.sleep(1)