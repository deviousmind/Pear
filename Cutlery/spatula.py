class Spatula:

    @staticmethod
    def get_people(raw_text):
        return [x.strip() for x in raw_text.split(' ')]

    def get_pairs(self, raw_text):
        if len(raw_text) == 0:
            return []
        raw_split = raw_text.split('] [')
        pairs = []
        for raw_pair in raw_split:
            pair = self.get_pair(raw_pair)
            pairs.append(pair)

        return pairs

    @staticmethod
    def get_pair(raw_pair):
        bad_chars = ['[', ']']
        text_pair = "".join(c for c in raw_pair if c not in bad_chars)
        split_names = text_pair.split(', ')
        return split_names