
class Recipe:
    """
    Recipe represents a single recipe, with a dictionary that stores the ingredients.

    key value pair ex:  ingredients['chicken'] = 10
    """


    def __init__(self, ingredients, name):
        """
        Constructor for the recipe class.
        Args:
            ingredients (dict - might change to list(Ingredient)): the list of all ingredients and amounts for the recipe
            name (str): the name of the recipe
        """
        self.ingredients = ingredients
        self.name = name

    def fitness(self):
        return len(self.ingredients)

    def normalize(self):
        return

    def mutate(self):
        """
        Based on random probability, choose whether or not we will mutate

            If we are gonna mutate, choose between 4 different mutation possibilities:

            1: randomly pick an ingredient in its recipe, randomly change its amount, renormalize

            2: change one ingredient to another: use the same ammount, renomrmalize

            3: addition of an ingredient, renormalize

            4: deletion of an ingredient, renormalize
        """
        return

    def __str__(self):
        return self.name + ": " + str(self.ingredients)
