from recipe_book import RecipeBook
import sys

def main():
    inspiring_set_filepath, num_generations = sys.argv[1 : ]
    num_generations = int(num_generations)
    population = RecipeBook(inspiring_set_filepath)
    #Step 1: read in original input file population
    #create recipes
    #store them in recipe book

    #Step 2: Loop
    iteration = 0
    while iteration < num_generations:
        population.generateIteration()
        iteration += 1


if __name__ == "__main__":
    main()
