from FirstAid.not_a_pair_error import NotAPairError
from Crust import decorator
import os


class Waitress:

    def __init__(self, spatula):
        self.spatula = spatula

    @staticmethod
    def serve():
        filepath = os.getenv('APPDATA') + '\\Pear'
        filename = 'pear.txt'
        full_path = filepath + '\\' + filename

        if not os.path.exists(filepath):
            os.makedirs(filepath)

        return full_path

    def check_appetite(self, people):
        print('\nIs anyone not here today?')
        missing_people_input = input('')
        people = self.spatula.remove_people(people, missing_people_input)
        print(decorator.success('\nAlright. I\'ll try to make pairs out of these people:'))
        print(decorator.attention(people.__str__() + '\n'))
        return people

    def special_order(self):
        valid_input = False
        must_pairs = []
        while not valid_input:
            print('Does anyone want to stick together?' + decorator.hint('(surround pairs with [])'))
            must_pair_input = input()
            try:
                must_pairs = self.spatula.get_pairs(must_pair_input)
                bad_pair_found = False
                for pair in must_pairs:
                    if len(pair) == 1:
                        bad_pair_found = True
                if bad_pair_found:
                    print(decorator.error('\nOne person does not make a pair. Try again.'))
                else:
                    valid_input = True
            except NotAPairError:
                print(decorator.error('\nSorry, but if you don\'t specify who the pairs are,\n'
                                      'I can\'t have them pair again.'))

        return must_pairs

    def check_allergies(self):
        invalid_input = True
        skip_text = 'If you don\'t mind the possibility of the same people pairing again,\n' \
                    'you can leave this blank.'
        print('\nI can try my best to avoid having the same people pair again.')
        print(decorator.hint(skip_text))

        cannot_pair = []
        while invalid_input:
            print('Who cannot pair today? ' + decorator.hint('(surround incompatible pairs with [])'))
            cannot_pair_input = input()
            try:
                cannot_pair = self.spatula.get_pairs(cannot_pair_input)
                bad_pair_found = False
                for pair in cannot_pair:
                    if len(pair) == 1:
                        bad_pair_found = True
                if bad_pair_found:
                    print(decorator.error('\nOne person does not make a pair. Try again.'))
                    print(decorator.hint(skip_text))
                else:
                    invalid_input = False
            except NotAPairError:
                print(decorator.error('\nSorry, but if you don\'t specify who the pairs are,\n'
                                      'I can\'t exclude them from pairing again.'))
                print(decorator.hint(skip_text))

        return cannot_pair