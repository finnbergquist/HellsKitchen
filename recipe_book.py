from curses import newpad
import glob
from hashlib import new
import imp
import random
import math
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

    """
    private void Rank() {
            
            double sumRank = ((1 + population.size()) / (double) 2) * population.size(); // arithmetic series formula for the sum
            List <Double> probabilityArray = new ArrayList<Double>();
            
            sortByFitness(population, 0, population.size()-1); 

            //probability for each individual to get selected, is stored in probability array.
            //least fit individual also has least probability of getting selected for the breeding pool.
            for (int i = 0; i < population.size(); i++) {
                //place probability of selecting an individual for the breeding pool in probabilityArray
                //the index position of probability array corresponds to rank
                if (i == 0) {
                    probabilityArray.add(i/sumRank); 
                } else {
                    probabilityArray.add((i/sumRank) + probabilityArray.get(i-1));
                    //System.out.println( "um" + population.size()); 
                }
            }

            //selects individual from the population based on probability calculated from rank
            while (breedingPool.size() != population.size()) {
                int i = 0; 
                double r = random.nextDouble();
                
                //find index i in probablityArray such that ProbabilityArray[i-1] < RandomNumber < ProbabilityArray[i]
                while (probabilityArray.get(i) < r) {
                    //if random number is higher than the last element in the array, 
                    //break the loop to generate new random number, and go through from the beginning again. 
                    if (i == population.size()-1) {
                        break; 
                    } 
                    i++; 
                }
                
                if (probabilityArray.get(i) >= r) {
                    //add to the breeding pool based on probability of selection as calculated and stored in probabilityArray.
                    breedingPool.add(population.get(i)); 

    """

    def selection(self):
        """ Method for selecting individuals for the breeding pool. 

        Args:
        """

        #sumRank = ((1 + len(RecipeBook)) / (Double) 2) * len(RecipeBook)
        probabilityArray = []
        self.sort_fitness(len(RecipeBook))

        self.sort_fitness(RecipeBook)
        return

    def truncSelection(self):

        """ Method for selecting individuals for the breeding pool. 
        Args:
        """
        self.sort_fitness(RecipeBook)
        truncateIndex = math.toIntExact(math.round(.2*(len(RecipeBook))))
        for i in range(len(RecipeBook)):
            randSelection = random.randint(truncateIndex) + (len(RecipeBook) - truncateIndex)
            self.add(RecipeBook.get(randSelection))

        return
    
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

