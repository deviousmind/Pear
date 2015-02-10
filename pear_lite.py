import math
import random
import re


class PearFilling():

    def __init__(self, slicer):
        self.slicer = slicer

    def create_pairs(self, available_people, cannot_pairs=None):
        if not cannot_pairs:
            cannot_pairs = []
        number_people = len(available_people)
        if number_people <= 1:
            return [available_people]
        pairs = self.generate_compatible_pairs(available_people, cannot_pairs)
        return pairs

    def generate_compatible_pairs(self, available_people, cannot_pairs):
        paired = False
        number_people = len(available_people)
        max_pairs = number_people // 2
        max_combinations = self.calculate_combinations(number_people)
        pairs_tried = 0
        pairs = []
        while not paired and pairs_tried < max_combinations:
            people = list(available_people)
            pairs = self.grow_pairs(people, max_pairs)
            paired = self.ripen_pairs(pairs, cannot_pairs)
            if not paired:
                pairs_tried += 1

        return pairs

    @staticmethod
    def ripen_pairs(pairs, cannot_pairs):
        if len(cannot_pairs) < 1:
            return True

        for pair in cannot_pairs:
            reverse_pair = [pair[1], pair[0]]
            if pair in pairs or reverse_pair in pairs:
                return False

        return True

    def grow_pairs(self, people, max_pairs):
        pairs = []
        for pair in range(max_pairs):
            self.add_pair_to_list(pairs, people)

        if len(people) > 0:
            pairs.append(people)

        return pairs

    def add_pair_to_list(self, pairs, people):
        pair = self.create_pair(people)
        self.eliminate_pair(people, pair)
        pairs.append(pair)

    def create_pair(self, people):
        number_people = len(people) - 1
        pair_indexes = self.slicer.slice(number_people)
        pair = self.pick(people, pair_indexes)
        return pair

    @staticmethod
    def pick(people, index_list):
        person_one = people[index_list[0]]
        person_two = people[index_list[1]]
        return [person_one, person_two]

    @staticmethod
    def eliminate_pair(people, pair):
        people.remove(pair[0])
        people.remove(pair[1])

    @staticmethod
    def calculate_combinations(total):
        # n! / ( r! (n - r)! )
        total_fac = math.factorial(total)
        others_chosen = 2
        pair_fac = math.factorial(others_chosen)
        combo_fac = math.factorial(total - others_chosen)
        combos = total_fac / (pair_fac * combo_fac)
        return combos


class Slicer:

    def slice(self, max_val):
        slice_one = random.randint(0, max_val)
        slice_two = self.slice_again(slice_one, max_val)
        return [slice_one, slice_two]

    @staticmethod
    def slice_again(first_slice, max_val):
        second_slice = random.randint(0, max_val)
        while second_slice == first_slice:
            second_slice = random.randint(0, max_val)

        return second_slice


def get_people(raw_text):
    people = re.findall(r"[\w']+", raw_text)
    return people


def generate_pairs(people_string):
    slicer = Slicer()
    filling = PearFilling(slicer)
    available_people = get_people(people_string)
    pairs = filling.create_pairs(available_people, [])
    return pairs