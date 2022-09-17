
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
        '''
        Based on random probability, choose whether or not we will mutate

            If we are gonna mutate, choose between 4 different mutation possibilities:

            1: randomly pick an ingredient in its recipe, randomly change its amount, renormalize

            2: change one ingredient to another: use the same ammount, renomrmalize

            3: addition of an ingredient, renormalize

            4: deletion of an ingredient, renormalize
        '''
        return

