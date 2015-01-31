from Cutlery.slicer import Slicer
from Cutlery.spatula import Spatula
from Filling.pear_filling import PearFilling
from Crust.crust import Crust
from Crust import toppings
from KitchenStaff.chef import Chef
from colorama import init
from Crust.colors import Colors
import sys


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if 'win' in sys.platform.lower():
            init()
        Colors.colorify()
        
    slicer = Slicer()
    pear = PearFilling(slicer)
    spatula = Spatula()
    filepath = toppings.prepare()
    crust = Crust(spatula, filepath)
    chef = Chef(crust)

    available_people = chef.bake_pie()
    available_people = crust.check_appetite(available_people)
    cannot_pair = crust.check_allergies()
    toppings.cut(available_people, cannot_pair, pear)
    toppings.put_a_fork_in_it()