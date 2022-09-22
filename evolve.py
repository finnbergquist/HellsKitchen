from recipe_book import RecipeBook
import sys
import os

def output_to_file(filepath, recipes):
    """
    For each recipe in the given list, creates a file for it in the specified filepath.
    Args:
        filepath: the location of the directory the text files should be created in
        recipes: the list of recipes to create files for
    """
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    if not filepath.endswith("/"):
        filepath += "/"

    for recipe in recipes:
        file = open(filepath + recipe.name + ".txt", "w")
        content = ""
        for ingredient in recipe.ingredients:
            content += str(ingredient) + "\n"
        file.write(content)
        file.close()


def main():
    """
    The main method for the program. Reads in command-line arguments and performs each iteration
    of GA.
    """
    # Read command-line arguments
    inspiring_set_filepath, output_filepath, num_generations = sys.argv[1 : ]
    num_generations = int(num_generations)
    
    # Populate recipe book
    population = RecipeBook(inspiring_set_filepath)

    # Perform GA to evolve the population
    iteration = 0
    while iteration < num_generations:
        population.run_generation()
        print("Iteration", iteration, "completed.")
        iteration += 1
    output_to_file(output_filepath, population.recipes)


if __name__ == "__main__":
    main()
