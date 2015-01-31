class Chef:

    def __init__(self, crust):
        self.crust = crust

    def bake_pie(self):
        try:
            available_people = self.crust.add_toppings()
        except IOError:
            available_people = self.crust.create()

        return available_people