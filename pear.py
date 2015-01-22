from Cutlery.slicer import Slicer
from Cutlery.spatula import Spatula
from Filling.pear_filling import PearFilling
from Crust import pie


if __name__ == "__main__":
    slicer = Slicer()
    pear = PearFilling(slicer)
    spatula = Spatula()

    filepath = pie.prepare()
    available_people = pie.present(spatula, filepath)
    available_people = pie.check_appetite(spatula, available_people)
    print()
    cannot_pair = pie.check_allergies(spatula)
    pie.cut(available_people, cannot_pair, pear)
    print()
    pie.put_a_fork_in_it()