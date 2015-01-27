from Cutlery.slicer import Slicer
from Cutlery.spatula import Spatula
from Filling.pear_filling import PearFilling
from Crust.pie import Pie
from Crust import toppings
from colorama import init
from Crust.colors import Colors
import sys


if __name__ == "__main__":
    if 'win' in sys.platform.lower():
        init()

    if len(sys.argv) > 1:
        Colors.colorify()
        
    slicer = Slicer()
    pear = PearFilling(slicer)
    spatula = Spatula()
    filepath = toppings.prepare()
    pie = Pie(spatula, filepath)

    available_people = pie.present()
    available_people = pie.check_appetite(available_people)
    cannot_pair = pie.check_allergies()
    toppings.cut(available_people, cannot_pair, pear)
    toppings.put_a_fork_in_it()