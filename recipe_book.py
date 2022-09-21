from curses import newpad
import glob
import random
import math
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
        self.inspiring_ingredients = list(self.inspiring_ingredients)

    def runGeneration(self):
        """
        
        Args:

        """
        curr_top_50 = []
        self.sort_fitness(self.recipes)
        curr_top_50.append(self.recipes[0])
        curr_top_50.append(self.recipes[1])
        curr_top_50.append(self.recipes[2])
        
        #breedingPool = self.selection()
        
        #RECOMBINATION
        #offsprings = self.recombination(breedingPool)
        offsprings = self.recombination(self.recipes)

        #MUTATION
        for individual in offsprings:
            individual.mutate()
            
        #Sort recipes by fitness - most fit to least fit
        self.sort_fitness(offsprings)
        
        #Set new population - top 50% from old and new pool
        self.recipes.clear()
        for recipe in curr_top_50:
            self.recipes.append(recipe)
        
        print(offsprings)
        self.recipes.append(offsprings[0])
        self.recipes.append(offsprings[1])
        self.recipes.append(offsprings[2])

        print(self.recipes)


    def selection(self, bookLength):
        """ Method for selecting individuals for the breeding pool. 
        Returns the index corresponding to the selected individual 
        where each individual has a weight corresponding to its position in sorted order.

        Args:
        """
        breedingPool = []
        #n = len(self.recipes)
        # Use the gauss formula to get the sum of all ranks (sum of integers 1 to N).
        sumRank = (bookLength * (bookLength+1)) / 2

        for rank, ind_fitness in enumerate(self.sort_fitness(self.recipes), 1):
            breedingPool.append(rank, ind_fitness, (float(rank) / sumRank))

        return breedingPool
    
    def recombination(self, breedingPool):
        
        """Implements recombination using OnePoint crossover, a technique that will
        randomly select a pivot index in the ingredient list of each recipe, 
        thus dividing each recipe into two sub-lists of ingredients. 
        A new recipe is then created by combining the first sub-list of the first recipe
        with the second sub-list of the second recipe.
        Args:
        recipeOne (list of Ingredient obj): first recipe 
        recipeOne[i] (ingredient)

        recipeTwo (recipe): second recipe 

        """
        newPopulation = []
        
        index = 0
        while (index > len(breedingPool)):
            offspring = Recipe(self.crossover(breedingPool[index], breedingPool[index+1]), "recipe_number_{0}".format(len(newPopulation), self.inspiring_ingredients))
            newPopulation.append(offspring)
            index += 2
            
        return newPopulation
        

    def crossover(self, recipeOne, recipeTwo):
        offspringIngredients = [] #empty list of ingredients objects

        pivot1 = random.randint(1, len(recipeOne))
        pivot2 = random.randint(1, len(recipeTwo))
        
        #CHECK FOR DUPLICATES
        duplicates = set()
        for i in range(0, pivot1):
            ingredient_name = getattr(recipeOne[i], 'name')
            ingredient_amount = getattr(recipeOne[i], 'amount')
            newIngredient = Ingredient(ingredient_name, ingredient_amount)
            offspringIngredients.append(newIngredient)
            duplicates.add(ingredient_name)
        for j in range(pivot2, len(recipeTwo)):
            ingredient_name = getattr(recipeTwo[j], 'name')
            ingredient_amount = getattr(recipeTwo[j], 'amount')
            if (ingredient_name not in duplicates):
                newIngredient = Ingredient(ingredient_name, ingredient_amount)
                offspringIngredients.append(newIngredient)

        return offspringIngredients
   
    def sort_fitness(self, recipes):
        """Sorts the fitness of each recipe based on """
        return

    def __str__(self):
        return str("\n".join([str(recipe) for recipe in self.recipes]))


