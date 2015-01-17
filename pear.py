from Cutlery.slicer import Slicer
from Cutlery.spatula import Spatula
from Filling.pear_filling import PearFilling
from Crust import pie


if __name__ == "__main__":
    slicer = Slicer()
    pear = PearFilling(slicer)
    spatula = Spatula()

    available_people_input = input('Who is available to pair today?\n')
    available_people = spatula.get_people(available_people_input)

    print('')

    cannot_pair_input = input('Who cannot pair today? (input pairs as [person_one, person_two]\n')
    cannot_pair = spatula.get_pairs(cannot_pair_input)

    print('')

    pairs = pear.create_pairs(available_people, cannot_pair)

    print('How about this?')

    for index in range(len(pairs)):
        pair = pairs[index]
        person_one = pair[0]
        if len(pair) > 1:
            person_two = pair[1]
            print(person_one + ' and ' + person_two)
        else:
            print(person_one + ' alone')
        print('')

    pie.put_a_fork_in_it()