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

    def generateIteration(self):
        #self.selection() #sorts recipes by fitness
        newPopulation = []
        newPopulation.append(self.recipes[0]) #keep top 3 fittest in next population
        newPopulation.append(self.recipes[1])
        newPopulation.append(self.recipes[2])
        
        newPopulation.append(Recipe(self.recombination(getattr(self.recipes[0], 'ingredients'), getattr(self.recipes[1], 'ingredients')), "recipe_number_{0}".format(len(newPopulation)+1), self.inspiring_ingredients))
        newPopulation.append(Recipe(self.recombination(getattr(self.recipes[1], 'ingredients'), getattr(self.recipes[2], 'ingredients')), "recipe_number_{0}".format(len(newPopulation)+1), self.inspiring_ingredients))
        newPopulation.append(Recipe(self.recombination(getattr(self.recipes[0], 'ingredients'), getattr(self.recipes[2], 'ingredients')), "recipe_number_{0}".format(len(newPopulation)+1), self.inspiring_ingredients))
        
        print(newPopulation)
        count=0
        for individual in newPopulation:
            print(count, individual)
            count+=1
            #individual.mutate(individual)
            
        self.recipes.clear()
        self.recipes = newPopulation


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
        
    def rankSelection(self):
        
        return

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
    
    def recombination(self, recipeOne, recipeTwo):
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
        recipeOffspring = [] #empty list of ingredients objects
        pivot = 0

        if (len(recipeOne) <= len(recipeTwo)):
            pivot = random.randint(1, len(recipeOne))
        else:
            pivot = random.randint(1, len(recipeTwo))
        
        print("Pivot", pivot)
        print("recipeOne", recipeOne)
        
        #CHECK FOR DUPLICATES
        duplicates = set()
        for i in range(0, pivot):
            ingredient_name = getattr(recipeOne[i], 'name')
            ingredient_amount = getattr(recipeOne[i], 'amount')
            newIngredient = Ingredient(ingredient_name, ingredient_amount)
            recipeOffspring.append(newIngredient)
            duplicates.add(ingredient_name)
        for j in range(pivot, len(recipeTwo)):
            ingredient_name = getattr(recipeTwo[j], 'name')
            ingredient_amount = getattr(recipeTwo[j], 'amount')
            if (ingredient_name not in duplicates):
                newIngredient = Ingredient(ingredient_name, ingredient_amount)
                recipeOffspring.append(newIngredient)

        return recipeOffspring

    def sort_fitness(self):
        """Sorts the fitness of each recipe based on """
        return

    def __str__(self):
        return str("\n".join([str(recipe) for recipe in self.recipes]))




'''#Finn's testing code:

book = RecipeBook('inspiring_set')
print(book.recipes[0])

for i in range(0,500):   
    book.recipes[0].mutate()

print(book.recipes[0])
'''