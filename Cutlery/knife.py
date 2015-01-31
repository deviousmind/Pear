from Crust import decorator


def cut(people, incompatible, forced, filling):
    while True:
        pairs = filling.create_pairs(people, incompatible)
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