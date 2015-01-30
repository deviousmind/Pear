import re
from FirstAid.not_a_pair_error import NotAPairError


class Spatula:

    @staticmethod
    def get_people(raw_text):
        people = re.findall(r"[\w']+", raw_text)
        return people

    def get_pairs(self, raw_text):
        if len(raw_text) == 0:
            return []
        pair_finder_pattern = r"\[(.*?)\]"
        contains_pairs = re.search(pair_finder_pattern, raw_text)
        if not contains_pairs:
            raise NotAPairError

        raw_split = re.findall(pair_finder_pattern, raw_text)
        pairs = []
        for raw_pair in raw_split:
            pair = self.get_pair(raw_pair)
            if len(pair) > 0:
                pairs.append(pair)
        return pairs

    @staticmethod
    def get_pair(raw_pair):
        split_names = re.findall(r"[\w']+", raw_pair)
        return split_names

    def remove_people(self, people, raw_text):
        missing_people = self.get_people(raw_text)
        lower_missing = [mp.lower() for mp in missing_people]
        remaining = [p for p in people if p.lower() not in lower_missing]
        return remaining