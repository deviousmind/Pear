from Appliances.oven import Oven
from Appliances.refrigerator import Refrigerator
from Crust import decorator


class Pie:

    def __init__(self, spatula, filepath):
        self.filepath = filepath
        self.spatula = spatula

    def add_toppings(self):
        saved_people = Oven.bake(self.filepath)
        available_people = self.spatula.get_people(saved_people)

        if len(available_people) == 0:
            available_people = self.remake()
        else:
            available_people = self.taste_test(available_people)

        return available_people

    def remake(self):
        print(decorator.warn('I\'m sorry, but I seem to have forgotten you.'))
        available_people = self.create()
        return available_people

    def taste_test(self, people):
        print(decorator.emphasis('Welcome back!') + decorator.success(' I remember your names.'))
        print('Is this still your group of people? (y/n)')
        print(decorator.attention(people.__str__()))
        keep_people = input()
        if keep_people.lower() == 'n':
            print(decorator.warn('\nOh? Well let me ask again.'))
            people = self.create()

        return people

    def create(self):
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