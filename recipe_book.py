import glob
from recipe import Recipe

class RecipeBook:
    """
    Holds a list of all current recipes.
    """

    def __init__(self, inspiring_set_path):
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
                current_ingredients = {}
                for line in file.readlines():
                    amount, ingredient = line.split("oz")
                    ingredient = ingredient.strip()
                    self.inspiring_ingredients.add(ingredient)
                    current_ingredients[ingredient] = float(amount)
                self.recipes.append(Recipe(current_ingredients, "recipe_number_{0}".format(self.total_recipes_created)))
                self.total_recipes_created += 1
        self.inspiring_ingredients = list(self.inspiring_ingredients)


    def selection(self):
        """"""
        return
    
    def recombination(self):
        return

    def mutation(self):
        """Iterate through all the recipes and call recipe.mutate()"""
        return

    def sort_fitness(self):
        return

    def __str__(self):
        return str("\n".join([str(recipe) for recipe in self.recipes]))

    
