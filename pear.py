from Cutlery.slicer import Slicer
from Cutlery.spatula import Spatula
from Cutlery import knife
from Filling.pear_filling import PearFilling
from Crust.pie import Pie
from Crust import toppings
from KitchenStaff.chef import Chef
from KitchenStaff.waitress import Waitress
from colorama import init
from Crust.colors import Colors
import sys


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if 'win' in sys.platform.lower():
            init()
        Colors.colorify()
        
    slicer = Slicer()
    filling = PearFilling(slicer)
    spatula = Spatula()
    waitress = Waitress(spatula)
    filepath = waitress.serve()
    pie = Pie(spatula, filepath)
    chef = Chef(pie)

    available_people = chef.bake_pie()
    available_people = waitress.check_appetite(available_people)
    must_pair = waitress.special_order()
    print(must_pair)
    cannot_pair = waitress.check_allergies()
    knife.cut(available_people, cannot_pair, must_pair, filling)
    toppings.put_a_fork_in_it()