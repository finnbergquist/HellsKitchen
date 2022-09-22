import glob
import random
import numpy as np
from recipe import Recipe
from ingredient import Ingredient

class RecipeBook:
    """
    Represents the population for GA. The class contains a list of all current recipes and methods for selection 
    and recombination.
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


    def run_generation(self):
        """
        Runs GA for one iteration to produce and set the current population to a new generation of recipes.
        A new population of offspring are created from selecting current recipes for breeding and using them
        to perform recombination. The new population of recipes is a combination of the top 50% of the current 
        population and the top 50% of the offspring.
        """
        self.sort_fitness(self.recipes)
        original_recipe_book = self.recipes.copy()
       
        # Selection
        breedingPool = self.selection()
        
        # Recombination
        offspring = self.recombination(breedingPool)
  
        # Mutation
        for individual in offspring:
            individual.mutate()
            
        # Sort offspring by fitness to take top 50%
        self.sort_fitness(offspring)
        
        # Set new population - top 50% from old and new pool
        mid = len(original_recipe_book) // 2
        self.recipes = original_recipe_book[ : mid] + offspring[ : mid]

    
    def selection(self):
        """ 
        Returns the breeding pool for the current population. Recipes are selected for the breeding pool with probability
        to their fitness. The breeding pool is twice the size of the population since two parents produce one new recipe.
        """
        breeding_pool = []
        
        total_weight = 0
        #Compute total sum
        for recipe in self.recipes:
            total_weight += recipe.get_fitness()
            
        # Compute probability for each recipe
        recipe_probabilities = [recipe.get_fitness() / total_weight for recipe in self.recipes]
        
        # Randomly select (2 * population size) parents for recombination
        while (len(breeding_pool) < 2 * len(self.recipes)):
            breeding_pool.append(np.random.choice(self.recipes, p=recipe_probabilities))

        return breeding_pool

    
    def recombination(self, breedingPool):
        """
        Returns the offspring that result from performing crossover with each of pair of parents in the
        breeding pool.
        Args:
            breeding_pool (list): the list of recipes being used as parents to produce the new recipes

        """
        new_population = []
        index = 0
        while (len(new_population) < len(self.recipes)):
            offspring = Recipe(self.crossover(breedingPool[index], breedingPool[index+1]), "recipe_number_{0}".format(self.total_recipes_created), self.inspiring_ingredients)
            self.total_recipes_created += 1
            new_population.append(offspring)
            index += 2

        return new_population
        

    def crossover(self, recipe_one, recipe_two):
        """
        Returns a new recipe that results from recombination using the process from PIERRE. Given two recipes pivot index 
        is randomly selected in the ingredient list of each one, which divides each recipe into two sub-lists of ingredients. 
        A new recipe is created by combining the left sub-list of the first recipe and the right sub-list of the second recipe.

        If there are duplicate ingredients in the new recipe, they are removed so each ingredient only appears once.
        Args:
            recipe_one (Recipe): the first recipe 
            recipe_two (Reicpe): the second recipe 
        """
        offspring_ingredients = [] # Empty list of ingredients objects
        ingredients1 = recipe_one.ingredients
        ingredients2 = recipe_two.ingredients
        pivot1 = random.randint(0, len(ingredients1) - 1)
        pivot2 = random.randint(0, len(ingredients2) - 1)
        
        # Check for duplicates
        duplicates = set()
        for i in range(0, pivot1):
            ingredient_name = ingredients1[i].name
            ingredient_amount = ingredients1[i].amount
            new_ingredient = Ingredient(ingredient_name, ingredient_amount)

            offspring_ingredients.append(new_ingredient)
            duplicates.add(ingredient_name)

        for j in range(pivot2, len(ingredients2)):
            ingredient_name = ingredients2[j].name
            ingredient_amount = ingredients2[j].amount

            if (ingredient_name not in duplicates):
                new_ingredient = Ingredient(ingredient_name, ingredient_amount)
                offspring_ingredients.append(new_ingredient)

        return offspring_ingredients
   

    def sort_fitness(self, recipes):
        """ 
        Sorts the given list of recipes in descending order according to each recipe's fitness.
        Args:
            recipes (list): the list of recipes to sort
        """
        recipes.sort(key = lambda recipe: -1 * recipe.get_fitness())


    def __str__(self):
        """
        Returns a string representation of the population.
        """
        return str("\n".join([str(recipe) for recipe in self.recipes]))

