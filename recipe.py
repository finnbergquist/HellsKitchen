import random
from ingredient import Ingredient

class Recipe:
    """
    Recipe represents a single recipe, with a list that stores its ingredients. It also must contain
    a list of all the possible ingredient names(inspiring_ingredients), so that it can choose new ingredients
    for mutation type 2 and 3. Finally, it also has a name to label the recipe.
    """
    MUTATION_PROBABILITY = 0.5
    inspiring_ingredients = None

    def __init__(self, ingredients, name):
        """
        Constructor for the recipe class.
        Args:
            ingredients (list) : list of ingredient objects
            name (str): the name of the recipe
            inspiring_ingredients (set) : original set of all ingredients that can be used in mutation
        """
        self.inspiring_ingredients = Recipe.inspiring_ingredients # Set of ingredient_names
        self.ingredients = ingredients # List of ingredient objects
        self.name = name


    def get_fitness(self):
        """
        Returns the fitness of the recipe. The fitness is equal to the number of unique
        ingredients in the recipe, and a fitter recipe has more ingredient variety.
        """
        return len(self.ingredients)


    def normalize(self):
        """
        Sums the total amount of ingredients(in ounces). Then it multiplies each ingredient amount by
        100/total volume so that the sum of all ingredients sums to 100 again. The self.ingredients list
        is modified.
        """
        total_amount = 0
        for ingredient in self.ingredients:
            total_amount += ingredient.amount

        for ingredient in self.ingredients:
            ingredient.amount = (100.0 / total_amount) * ingredient.amount


    def available_ingredients(self):
        """
        Returns a list of available ingredients. Looks at all the inspiring ingredients, and chooses an ingredient from 
        that list which is not already in the recipe. The edge case that there are no available ingredients is dealt with 
        in the mutate method.
        """
        used_ingredient_names = set()

        for ingredient in self.ingredients:
            used_ingredient_names.add(ingredient.name)

        available_ingredient_names = self.inspiring_ingredients - used_ingredient_names

        return list(available_ingredient_names)


    def mutate(self):
        """
        Based on random probability, choose whether or not we will mutate the recipe
            If we are gonna mutate, choose between 4 different mutation possibilities:
            1: randomly pick an ingredient in its recipe, randomly change its amount, renormalize
            2: change one ingredient to another: use the same ammount, renomrmalize
            3: addition of an ingredient, renormalize
            4: deletion of an ingredient, renormalize
        """
        # Step 1: Decide if we will mutate
        if random.random() > Recipe.MUTATION_PROBABILITY: 
            return

        # Step 2: Choose which type of mutation
        mutation_number = random.random()

        # Type 1
        if mutation_number <= 0.25: 
            ingredient_to_change_index = random.randint(0, len(self.ingredients) - 1)
            random_amount = random.randrange(1, 80) # Number of ounces, max of 80
            self.ingredients[ingredient_to_change_index].amount = random_amount
            self.normalize()
        # Type 2
        elif 0.25 < mutation_number <= 0.5: 
            ingredient_to_change_index = random.randint(0, len(self.ingredients) - 1)  
            available_ingredients = self.available_ingredients()
            if len(available_ingredients) > 0: # If there are unused ingredients      
                self.ingredients[ingredient_to_change_index].name = random.choice(self.available_ingredients())
        # Type 3
        elif 0.5 < mutation_number <= 0.75:
            available_ingredients = self.available_ingredients()
            if len(available_ingredients) > 0: # Only proceed if there are unused ingredients
                ingredient_name = random.choice(available_ingredients)
                amount = random.randrange(1, 80) # Number of ounces of new ingredient
                new_ingredient = Ingredient(ingredient_name, amount)
                self.ingredients.append(new_ingredient)
                self.normalize()
        #Type 4
        else:
            ingredient_to_change_index = random.randint(0, len(self.ingredients) - 1)
            if len(self.ingredients) > 1: # Don't remove the ingredient if it is the last one!
                self.ingredients.pop(ingredient_to_change_index)        
            self.normalize()


    def __str__(self):
        """
        Returns a string representation of a recipe, which its name followed by all of its ingredients.
        """
        return self.name + ": " + ", ".join([str(ingredient) for ingredient in self.ingredients])