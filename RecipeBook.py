import glob
import imp
import random
from Recipe import Recipe
from Ingredient import Ingredient

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
        self.inspiring_ingredients = list(self.inspiring_ingredients)


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
    
    def recombination(self, recipeOne, recipeTwo):
        """Implements recombination using OnePoint crossover, a technique that will
        randomly select a pivot index in the ingredient list of each recipe, 
        thus dividing each recipe into two sub-lists of ingredients. 
        A new recipe is then created by combining the first sub-list of the first recipe
        with the second sub-list of the second recipe.
        Args:
        recipeOne (recipe): first recipe 

        recipeTwo (recipe): second recipe 

        """

        newRecipe = Recipe()

        pivot = random.randint(len(recipeOne))

        for i in range(0, pivot):
            newRecipe.append(recipeOne[i])
        for j in range(pivot +1, len(recipeTwo)):
            newRecipe.append(recipeOne[j])


        RecipeBook.add(newRecipe)


        return newRecipe

    def mutation(self):
        """Iterate through all the recipes and call recipe.mutate()"""
        return

    def sort_fitness(self):
        """Sorts the fitness of each recipe based on """
        return

    def __str__(self):
        return str("\n".join([str(recipe) for recipe in self.recipes]))

    
