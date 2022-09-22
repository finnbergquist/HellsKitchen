import random
from ingredient import Ingredient

class Recipe:
    """
    Recipe represents a single recipe, with a list that stores its ingredients. It also must contain
    a list of all the possible ingredient names(inspiring_ingredients), so that it can choose new ingredients
    for mutation type 2 and 3. Finally, it also has a name to label the recipe.
    """


    def __init__(self, ingredients, name, inspiring_ingredients, mutation_probability=0.2):
        """Constructor for the recipe class.
        Args:
            ingredients (list) : list of ingredient objects
            name (str): the name of the recipe
            inspiring_ingredients (set) : original set of all ingredients that can be used in mutation
        Return:
            None
        """
        self.inspiring_ingredients = inspiring_ingredients# set of ingredient_names
        self.ingredients = ingredients # list of ingredient objects
        self.name = name
        self.mutation_probability = mutation_probability


    def get_fitness(self):
        '''Fitness metric as specified in the requirements.
        Args: 
            None
        Return:
            number of ingredients (int)
        '''

        return len(self.ingredients)

    def normalize(self):
        ''' Sums the total amount of ingredients(in ounces). Then it multiplies each ingredient amount by
        100/total volume so that the sum of all ingredients sums to 100 again. The self.ingredients list
        is modified.
        Args: 
            None
        Return:
            None
        '''

        total_amount = 0.
        for ingredient in self.ingredients:
            total_amount+=ingredient.amount

        for ingredient in self.ingredients:
            ingredient.amount = (100./total_amount)*ingredient.amount

        return

    def available_ingredients(self):
        '''
        Looks at all the inspiring ingredients, and chooses an ingredient from that list which is not already
        in the recipe. The edge case that there are no available ingredients is dealt with in the mutate method.
        Args:
            None
        Return:
            available_ingredients(list) : list of ingredient objects
        '''
        used_ingredient_names = set()

        for ingredient in self.ingredients:
            used_ingredient_names.add(ingredient.name)

        available_ingredient_names = self.inspiring_ingredients - used_ingredient_names

        return list(available_ingredient_names)


    def mutate(self):
        """
        Based on random probability, choose whether or not we will mutate
            If we are gonna mutate, choose between 4 different mutation possibilities:
            1: randomly pick an ingredient in its recipe, randomly change its amount, renormalize
            2: change one ingredient to another: use the same ammount, renomrmalize
            3: addition of an ingredient, renormalize
            4: deletion of an ingredient, renormalize
        Args:
            None
        Return:
            None
        """
        mutation_probability = self.mutation_probability

        #Step 1: Decide if we will mutate
        if random.random() > mutation_probability: 
            return

        #Step 2: Choose which type of mutation
        mutation_number = random.random()

        #Type1
        if mutation_number<=0.25: 
            ingredient_to_change_index = random.randint(0, len(self.ingredients)-1)
            random_amount = random.randrange(1,80)#number of ounces, max of 80
            self.ingredients[ingredient_to_change_index].amount = random_amount
            self.normalize()
        #Type2
        elif 0.25<mutation_number<=0.5: 
            ingredient_to_change_index = random.randint(0, len(self.ingredients)-1)  
            available_ingredients = self.available_ingredients()
            if len(available_ingredients)>0:#If there are unused ingredients      
                self.ingredients[ingredient_to_change_index].name = random.choice(self.available_ingredients())
        #Type3
        elif 0.5<mutation_number<=0.75:
            available_ingredients = self.available_ingredients()
            if len(available_ingredients)>0: #only proceed if there are unused ingredients
                ingredient_name = random.choice(available_ingredients)
                amount = random.randrange(1,80)#number of ounces of new ingredinet
                new_ingredient = Ingredient(ingredient_name, amount)
                self.ingredients.append(new_ingredient)
                self.normalize()
        #Type4
        else:
            ingredient_to_change_index = random.randint(0, len(self.ingredients)-1)
            if len(self.ingredients) > 1: # don't remove the ingredient if it is the last one!
                self.ingredients.pop(ingredient_to_change_index)        
            self.normalize()

        return
    
    def getIngredients(self):
        """
        Gets the list of ingrediants
        Args:
            None

        Return: 
            returns the list of ingrediants
        """
        return self.ingredients

    def __str__(self):
        '''
       using __str__ method of ingredients, and joining them all together 
        Return:
            Name (str) concatenated string of all ingredient names and ammounts
        '''
        return self.name + ": " + ", ".join([str(ingredient) for ingredient in self.ingredients])