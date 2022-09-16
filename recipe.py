
class Recipe:
    '''
    Recipe represents a single recipe, with a dictionary that stores the ingredients.

    key value pair ex:  ingredients['chicken'] = 10
    '''


    def __init__(self):
        self.ingredients = {}

    def fitness(self):
        return len(self.ingredients)

    def normalize(self):
        return

    def mutate(self):
        return

