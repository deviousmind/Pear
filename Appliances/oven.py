class Oven:

    @staticmethod
    def bake(filepath):
        with open(filepath) as settings:
            saved_people = settings.readline()
            settings.close()

        return saved_people