import random

class Recipe:
    """
    Recipe represents a single recipe, with a dictionary that stores the ingredients.

    key value pair ex:  ingredients['chicken'] = 10
    """


    def __init__(self, ingredients, name, inspiring_ingredients):
        """
        Constructor for the recipe class.
        Args:
            ingredients (dict - might change to list(Ingredient)): the list of all ingredients and amounts for the recipe
                        ex.
                            rice : 0.4
                            beans : 0.6

            name (str): the name of the recipe
        """
        self.inspiring_ingredients = list(inspiring_ingredients)
        self.ingredients = ingredients
        self.name = name

    def fitness(self):
        return len(self.ingredients)

    def normalize(self):
        '''
        Sums the total amount of ingredients(in ounces). Then it multiplies each ingredient amount by
        100/total volume so that the sum of all ingredients sums to 100 again.
        '''

        total_amount = 0.
        for ingredient in self.ingredients:
            total_amount+=ingredient.amount

        for ingredient in self.ingredients:
            ingredient.amount = (100./total_amount)*ingredient.amount

        return

    def mutate(self, recipe):
        """
        Based on random probability, choose whether or not we will mutate

            If we are gonna mutate, choose between 4 different mutation possibilities:

            1: randomly pick an ingredient in its recipe, randomly change its amount, renormalize

            2: change one ingredient to another: use the same ammount, renomrmalize

            3: addition of an ingredient, renormalize

            4: deletion of an ingredient, renormalize
        """
        mutation_probability = 0.2

        #Step 1: Decide if we will mutate
        if random.random() > mutation_probability: 
            return recipe

        #Step 2: Choose which type of mutation
        mutation_number = random.random()

        #Type1
        if mutation_number<=0.25:
            ingredient_to_change_index = random.randint(0, len(self.ingredients))
            random_amount = random.random(0,100)#number of ounces
            self.ingredients[ingredient_to_change_index].amount = random_amount
            self.normalize()
        #Type2
        elif mutation_number<0.25<=0.5: #might need to change this so that it does not choose an ingredient not already in recipe
            ingredient_to_change_index = random.randint(0, len(self.ingredients))
            self.ingredients[ingredient_to_change_index].ingredient_name = random.choice(self.inspiring_ingredients)

 
        return

    def __str__(self):
        return self.name + ": " + str(self.ingredients)
