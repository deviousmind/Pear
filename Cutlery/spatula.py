import re


class Spatula:

    @staticmethod
    def get_people(raw_text):
        people = re.findall(r"[\w']+", raw_text)
        return people

    def get_pairs(self, raw_text):
        if len(raw_text) == 0:
            return []
        raw_split = re.findall(r"\[(.*?)\]", raw_text)
        pairs = []
        for raw_pair in raw_split:
            pair = self.get_pair(raw_pair)
            pairs.append(pair)

        return pairs

    @staticmethod
    def get_pair(raw_pair):
        split_names = re.findall(r"[\w']+", raw_pair)
        return split_names