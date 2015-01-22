from FirstAid.not_a_pair_error import NotAPairError


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
        with open(self.filepath) as settings:
            saved_people = settings.readline()
            available_people = self.spatula.get_people(saved_people)
            settings.close()

        if len(available_people) == 0:
            available_people = self.remake()
        else:
            available_people = self.taste_test(available_people)

        return available_people

    def remake(self):
        print('I\'m sorry, but I seem to have forgotten you.')
        available_people = self.add_toppings()
        return available_people

    def taste_test(self, people):
        print('Welcome back! I remember your names.')
        print('Is this still your group of people? (y/n)')
        print(people.__str__())
        keep_people = input()
        if keep_people.lower() == 'n':
            print('\nOh? Well let me ask again.')
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
                print('No one?')
                print('Certainly you made a mistake...')
                print('Yes. You made a mistake. Let me ask you again.')

        print('\nWould you like me to remember these people? (y/n)')
        remember = input()
        if remember.lower() == 'y':
            self.save_names(available_people)

        return available_people

    def save_names(self, people):
        with open(self.filepath, 'w') as settings:
            for person in people:
                settings.write(person + ' ')
            settings.close()

    def cool_whip(self, people):
        incorrect = True
        while incorrect:
            print('\nCool! These are the people I know right now:')
            print(people.__str__())
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
                    people = self.get_available_people()
                else:
                    print('Sorry, but this is the one time I actually require \'y\' or \'n\'')

        return people

    def check_appetite(self, people):
        print('\nIs anyone not here today?')
        missing_people_input = input('')
        missing_people = self.spatula.get_people(missing_people_input)
        people = [p for p in people if p not in missing_people]
        print('\nAlright. I\'ll try to make pairs out of these people:')
        print(people.__str__())
        print()
        return people

    def check_allergies(self):
        invalid_input = True
        skip_text = 'You can always leave this blank if you don\'t mind\n' \
                    'the possibility of having the same people pair again.'
        print('I can try my best to avoid having the same people pair again.')
        print(skip_text)

        cannot_pair = []
        while invalid_input:
            cannot_pair_input = input('Who cannot pair today? (surround incompatible pairs with [])\n')
            try:
                cannot_pair = self.spatula.get_pairs(cannot_pair_input)
                bad_pair_found = False
                for pair in cannot_pair:
                    if len(pair) == 1:
                        bad_pair_found = True
                if bad_pair_found:
                    print('\nOne person does not make a pair. Try again.')
                else:
                    invalid_input = False
            except NotAPairError:
                print('\nSorry, but if you don\'t specify who the pairs are,\n'
                      'I can\'t exclude them from pairing again.')
                print(skip_text)

        return cannot_pair