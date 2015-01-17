from Cutlery.slicer import Slicer
from Cutlery.spatula import Spatula
from Filling.pear_filling import PearFilling
from Crust import pie
from FirstAid.not_a_pair_error import NotAPairError


if __name__ == "__main__":
    slicer = Slicer()
    pear = PearFilling(slicer)
    spatula = Spatula()

    available_people_input = input('Who is available to pair today?\n')
    available_people = spatula.get_people(available_people_input)

    print('')

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
            invalid_input = False
        except NotAPairError:
            print('Sorry, but if you don\'t specify who the pairs are, I can\'t exclude them from pairing again.')
            print(skip_text)

        print('')

    while True:
        pairs = pear.create_pairs(available_people, cannot_pair)
        print('How about this?')
        pie.display_pairs(pairs)
        print('Or should I try again? (y/n)')
        response = input('')

        if response.lower() != 'y':
            break

    pie.put_a_fork_in_it()