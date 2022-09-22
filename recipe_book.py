from curses import newpad
import glob
from hashlib import new
import imp
import random
import math
import numpy as np
from sys import orig_argv
from tokenize import Double
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
        self.sort_fitness(self.recipes)
        originalRecipeBook = self.recipes.copy()
       
        #SELECTION
        breedingPool = self.selection()
        
        #RECOMBINATION
        offsprings = self.recombination(breedingPool)
        #offsprings = self.recombination(self.recipes).copy() #for testing
        #MUTATION
        for individual in offsprings:
            individual.mutate()
            
        #Sort offsprings by fitness to take top 50%
        self.sort_fitness(offsprings)
        
        #Set new population - top 50% from old and new pool
        self.recipes.clear()
        for i in range(0, 3):
            self.recipes.append(originalRecipeBook[i])
        
        for j in range(0, 3):
            self.recipes.append(offsprings[j])
        
        return self.recipes

<<<<<<< HEAD
=======

>>>>>>> ccf1a0bd9a963102649f8bff496d78d3529ef71a
    def rankSelection(self):
        """
        Rank selection makes the probability of selection proportional 
        to relative fitness of the individual. 
        
        """
        total_weight = 0
        for recipe in self.recipes:
            total_weight += recipe.get_fitness()

        index = 0
        r = random.Random() * total_weight

        while index < (len(self.recipes) - 1):
            r -= self.recipes[index].get_fitness()
            if r <= 0:
                break
            index += 1

        self.recipes.sort(key = lambda recipe: -1 * recipe.get_fitness())
        return self.recipes[index]

    def selection(self):
        """ Method for selecting individuals for the breeding pool. 

        Args:
        """
        breeding_pool = []
        for i in range(2*len(self.recipes)):
            breeding_pool.append(self.rankSelection())

        return breeding_pool
    

    def roulette_wheel_selection(self):
  
    # Computes the totallity of the population fitness
        population_fitness = sum([recipe.getfitness() for recipe in RecipeBook])
    
    # Computes for each chromosome the probability 
        recipe_probabilities = [recipe.getfitness()/population_fitness for recipe in RecipeBook]
    
    # Selects one chromosome based on the computed probabilities
        return np.random.choice(RecipeBook, p=recipe_probabilities)

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
        while (index < len(breedingPool)):
            offspring = Recipe(self.crossover(breedingPool[index], breedingPool[index+1]), "recipe_number_{0}".format(len(newPopulation)), self.inspiring_ingredients)
            newPopulation.append(offspring)
            index += 2
            
        return newPopulation
        

    def crossover(self, recipeOne, recipeTwo):
        offspringIngredients = [] #empty list of ingredients objects
        ingredients1 = getattr(recipeOne, 'ingredients')
        ingredients2 = getattr(recipeTwo, 'ingredients')
        pivot1 = random.randint(1, len(ingredients1))
        pivot2 = random.randint(1, len(ingredients2))
        
        #CHECK FOR DUPLICATES
        duplicates = set()
        for i in range(0, pivot1):
            ingredient_name = getattr(ingredients1[i], 'name')
            ingredient_amount = getattr(ingredients1[i], 'amount')
            newIngredient = Ingredient(ingredient_name, ingredient_amount)
            offspringIngredients.append(newIngredient)
            duplicates.add(ingredient_name)
        for j in range(pivot2, len(ingredients2)):
            ingredient_name = getattr(ingredients2[j], 'name')
            ingredient_amount = getattr(ingredients2[j], 'amount')
            if (ingredient_name not in duplicates):
                newIngredient = Ingredient(ingredient_name, ingredient_amount)
                offspringIngredients.append(newIngredient)

        return offspringIngredients
   
    def sort_fitness(self, recipes):
        """Sorts the fitness of each recipe based on """
        return

    def __str__(self):
        return str("\n".join([str(recipe) for recipe in self.recipes]))

