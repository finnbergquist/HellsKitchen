import glob
import random
from recipe import Recipe
from ingredient import Ingredient

class RecipeBook:
    """
    Holds a list of all current recipes.
    """

    def __init__(self, inspiring_set_path):
        """
        Constructor for the RecipeBook class.
        Args:
            inspiring_set_path (str): the filepath for the folder containing the inspiring set of recipes to be used
            as the initial population
        """
        self.recipes = []
        self.inspiring_ingredients = set()
        self.total_recipes_created = 0
        self.initialize_recipe_book(inspiring_set_path)


    def initialize_recipe_book(self, filepath):
        """
        Parses each of the recipes in the given filepath, adds each recipe's ingredients to inspiring_ingredients, and
        creates each recipe and adds it to the recipe population.
        Args:
            filepath (str): the path of the folder containing the inspiring set of recipes
        """
        if not filepath.endswith("/"):
            filepath += "/"

        for filename in glob.glob(filepath + "/*.txt"):
            with open(filename) as file:
                current_ingredients = []
                for line in file.readlines():
                    amount, ingredient = line.split("oz")
                    ingredient = ingredient.strip()
                    current_ingredients.append(Ingredient(ingredient, float(amount)))
                    self.inspiring_ingredients.add(ingredient)
                self.recipes.append(Recipe(current_ingredients, "recipe_number_{0}".format(self.total_recipes_created), self.inspiring_ingredients))
                self.total_recipes_created += 1


    def generateIteration(self):
        self.selection() #sorts recipes by fitness
        self.recipes = self.recombination()
        for individual in self.recipes:
            individual.mutate()
        
        
    def selection(self):
        """ Method for selecting individuals for the breeding pool. 

        Args:
        """
        
        return
    
    def recombination(self, recipe_one, recipe_two):
        """
        Returns a new recipe that results from recombination using the process from PIERRE. Given two recipes pivot index 
        is randomly selected in the ingredient list of each one, which divides each recipe into two sub-lists of ingredients. 
        A new recipe is created by combining the left sub-list of the first recipe and the right sub-list of the second recipe.

        If there are duplicate ingredients in the new recipe, they are replaced with one ingredient with the same name its amount
        is the sum of each instance's amount of the ingredient. 
        Args:
            recipe_one (Recipe): the first recipe 
            recipe_two (Reicpe): the second recipe 
        """
        ingredients = []
        ingredient_indices = {}

        pivot_one = random.randint(0, len(recipe_one.ingredients) - 1)
        pivot_two = random.randint(0, len(recipe_two.ingredients) - 1)
        
        for i in range(0, pivot_one + len(recipe_two.ingredients) - pivot_two):
            # Get the current ingredient that will be added to the new recipe
            current_ingredient = None
            if i <= pivot_one:
                current_ingredient = recipe_one.ingredients[i]
            else:
                current_ingredient = recipe_two.ingredients[i - pivot_one + pivot_two]

            if current_ingredient.name not in ingredient_indices:
                ingredients.append(current_ingredient)
                ingredient_indices[current_ingredient.name] = i
            else:
                # If the ingredient name is already in the current recipe, add the current ingredient's amount to it instead
                # of appending it as a new ingredient 
                current_ingredient_index = ingredient_indices[current_ingredient.name]
                ingredients[current_ingredient_index].amount += current_ingredient.amount

        new_recipe = Recipe(ingredients, "recipe_number_{0}".format(self.total_recipes_created), self.inspiring_ingredients)
        self.total_recipes_created += 1
        
        return new_recipe


    def mutation(self):
        """Iterate through all the recipes and call recipe.mutate()"""
        return

    def sort_fitness(self):
        """
        Sorts each recipe in the population according to its fitness (degree of ingredient variety).
        """
        self.recipes.sort(key = lambda recipe: recipe.get_fitness())

    def __str__(self):
        return str("\n".join([str(recipe) for recipe in self.recipes]))

    
