class Chef:

    def __init__(self, pie):
        self.pie = pie

    def bake_pie(self):
        try:
            available_people = self.pie.add_toppings()
        except IOError:
            available_people = self.pie.create()

        return available_people