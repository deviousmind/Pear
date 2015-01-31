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
    pie = Crust(spatula, filepath)
    chef = Chef(pie)

    available_people = chef.bake_pie()
    available_people = pie.check_appetite(available_people)
    cannot_pair = pie.check_allergies()
    toppings.cut(available_people, cannot_pair, pear)
    toppings.put_a_fork_in_it()