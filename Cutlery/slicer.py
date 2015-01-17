import random

class Slicer:

    def slice(self, max_val):
        slice_one = random.randint(0, max_val)
        slice_two = self.slice_again(slice_one, max_val)
        return [slice_one, slice_two]

    def slice_again(self, first_slice, max_val):
        second_slice = random.randint(0, max_val)
        while(second_slice == first_slice):
            second_slice = random.randint(0, max_val)

        return second_slice