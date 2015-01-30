from FirstAid.not_a_pair_error import NotAPairError
from Appliances.oven import Oven
from Appliances.refrigerator import Refrigerator
from Crust import decorator


class Pie:

    def __init__(self, spatula, filepath):
        self.filepath = filepath
        self.spatula = spatula

    def present(self):
        try:
            available_people = self.bake()
        except IOError:
            available_people = self.add_toppings()

        return available_people

    def bake(self):
        saved_people = Oven.bake(self.filepath)
        available_people = self.spatula.get_people(saved_people)

        if len(available_people) == 0:
            available_people = self.remake()
        else:
            available_people = self.taste_test(available_people)

        return available_people

    def remake(self):
        print(decorator.warn('I\'m sorry, but I seem to have forgotten you.'))
        available_people = self.add_toppings()
        return available_people

    def taste_test(self, people):
        print(decorator.emphasis('Welcome back!') + decorator.success(' I remember your names.'))
        print('Is this still your group of people? (y/n)')
        print(decorator.attention(people.__str__()))
        keep_people = input()
        if keep_people.lower() == 'n':
            print(decorator.warn('\nOh? Well let me ask again.'))
            people = self.add_toppings()

        return people

    def add_toppings(self):
        available_people = self.get_available_people()
        available_people = self.cool_whip(available_people)
        return available_people

    def get_available_people(self):
        available_people = []
        valid_people = False
        while not valid_people:
            available_people_input = input('Who is available to pair today?\n')
            available_people = self.spatula.get_people(available_people_input)
            if len(available_people) > 0:
                valid_people = True
            else:
                print(decorator.warn('No one?'))
                print(decorator.warn('Certainly you made a mistake...'))
                print(decorator.error('Yes. You made a mistake. Let me ask you again.'))

        print(decorator.request('\nWould you like me to remember these people? (y/n)'))
        remember = input()
        if remember.lower() == 'y':
            Refrigerator.save_names(self.filepath, available_people)

        return available_people

    def cool_whip(self, people):
        incorrect = True
        while incorrect:
            print(decorator.success('\nCool! These are the people I know right now:'))
            y_or_n = False
            while not y_or_n:
                print(decorator.attention(people.__str__()))
                print('Is that correct? (y/n)')
                response = input()
                if response.lower() == 'y':
                    y_or_n = True
                    incorrect = False
                elif response.lower() == 'n':
                    y_or_n = True
                    print(decorator.warn('\nOh? Well let\'s try again, shall we?'))
                    people = self.get_available_people()
                else:
                    print(decorator.error('Sorry, but this is the one time I actually require \'y\' or \'n\''))
                    print('These are the people I know right now:')

        return people

    def check_appetite(self, people):
        print('\nIs anyone not here today?')
        missing_people_input = input('')
        missing_people = self.spatula.get_people(missing_people_input)
        lower_missing = [mp.lower() for mp in missing_people]
        people = [p for p in people if p.lower() not in lower_missing]
        print(decorator.success('\nAlright. I\'ll try to make pairs out of these people:'))
        print(decorator.attention(people.__str__() + '\n'))
        return people

    def check_allergies(self):
        invalid_input = True
        skip_text = 'If you don\'t mind the possibility of the same people pairing again,\n' \
                    'you can leave this blank.'
        print('I can try my best to avoid having the same people pair again.')
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