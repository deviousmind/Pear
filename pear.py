from Cutlery.slicer import Slicer
from Cutlery.spatula import Spatula
from Filling.pear_filling import PearFilling
from Crust import pie
from FirstAid.not_a_pair_error import NotAPairError
import os


if __name__ == "__main__":
    slicer = Slicer()
    pear = PearFilling(slicer)
    spatula = Spatula()

    filepath = os.getenv('APPDATA') + '\\Pear'
    filename = 'pear.txt'
    full_path = filepath + '\\' + filename

    if not os.path.exists(filepath):
        os.makedirs(filepath)

    available_people = []
    try:
        with open(full_path) as settings:
            saved_people = settings.readline()
            available_people = spatula.get_people(saved_people)
            settings.close()
    except IOError:
        available_people = pie.get_available_people(spatula, full_path)
        available_people = pie.cool_whip(spatula, full_path, available_people)

    if len(available_people) == 0:
        print('I\'m sorry, but I seem to have forgotten you.')
        available_people = pie.get_available_people(spatula, full_path)
        available_people = pie.cool_whip(spatula, full_path, available_people)

    else:
        print('Welcome back! I remember your names.')
        print('Is this still your group of people? (y/n)')
        print(available_people.__str__())
        keep_people = input()
        if keep_people.lower() == 'n':
            print('\nOh? Well let me ask again.')
            available_people = pie.get_available_people(spatula, full_path)
            available_people = pie.cool_whip(spatula, full_path, available_people)

    print('\nIs anyone not here today?')
    missing_people_input = input('')
    missing_people = spatula.get_people(missing_people_input)
    available_people = [p for p in available_people if p not in missing_people]
    print('\nAlright. I\'ll try to make pairs out of these people:')

    print(available_people.__str__())

    print()

    invalid_input = True
    skip_text = 'You can always leave this blank if you don\'t mind\n' \
        'the possibility of having the same people pair again.'
    cannot_pair = []
    print('I can try my best to avoid having the same people pair again.')
    print(skip_text)

    while invalid_input:
        cannot_pair_input = input('Who cannot pair today? (surround incompatible pairs with [])\n')
        try:
            cannot_pair = spatula.get_pairs(cannot_pair_input)
            if len(cannot_pair) == 1:
                print('\nOne person does not make a pair. Try again.')
            else:
                invalid_input = False
        except NotAPairError:
            print('Sorry, but if you don\'t specify who the pairs are,\n'
                                'I can\'t exclude them from pairing again.')
            print(skip_text)

    while True:
        pairs = pear.create_pairs(available_people, cannot_pair)
        print('\nHow about this?\n')
        pie.display_pairs(pairs)
        print('\nOr should I try again? (y/n)')
        response = input()

        if response.lower() != 'y':
            break

    print()
    pie.put_a_fork_in_it()