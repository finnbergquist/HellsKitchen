
from unicodedata import name


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

    def getName(self):
        """
        Args:
            None
        return:
            returns name of ingredient
        """
        return self.name
    
    def setName(self, newName):
        """
        Args:
            newName (string) : New name that is given to ingrediant
        return:
            sets name of ingredient
        """
        self.name = newName
    
    def __str__(self):
        return "{0}: {1}".format(self.name, round(self.amount, 4))