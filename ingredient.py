
class Ingredient():

    def __init__(self, ingredient_name, amount):
        """
        Constructor for the recipe class.
        Args:
            ingredient_name (string) : name of ingredient ex.(rice)
            
            amount (int): number of ounces for ingredient
        """

        self.ingredient_name = ingredient_name
        self.amount = amount