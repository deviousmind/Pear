class Refrigerator:

    @staticmethod
    def save_names(filepath, people):
        with open(filepath, 'w') as settings:
            for person in people:
                settings.write(person + ' ')
            settings.close()