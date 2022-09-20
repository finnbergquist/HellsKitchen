
class Ingredient():

    def __init__(self, name, amount):
        """
        Constructor for the recipe class.
        Args:
            name (str) : name of ingredient ex.(rice)
            amount (float): number of ounces for ingredient
        """
        self.name = name
        self.amount = amount

    def __str__(self):
        return "{0}: {1}".format(self.name, self.amount)