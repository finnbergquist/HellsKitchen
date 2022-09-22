from recipe_book import RecipeBook
import sys
import os

def output_to_file(filepath, recipes):
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
    
    #Read command-line & files
    inspiring_set_filepath, output_filepath, num_generations = sys.argv[1 : ]
    num_generations = int(num_generations)
    
    #Populate recipe book
    population = RecipeBook(inspiring_set_filepath)

    #Evolve
    iteration = 0
    while iteration < num_generations:
        population.runGeneration()
        print("Iteration", iteration, "completed.")
        iteration += 1
    output_to_file(output_filepath, population.recipes)


if __name__ == "__main__":
    main()
