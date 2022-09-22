from recipe_book import RecipeBook
import sys

def main():
    
    #Read command-line & files
    inspiring_set_filepath, num_generations = sys.argv[1 : ]
    num_generations = int(num_generations)
    
    #Populate recipe book
    population = RecipeBook(inspiring_set_filepath)

    #Evolve
    iteration = 0
    while iteration < num_generations:
        population.runGeneration()
        print("Iteration", iteration, "completed.")
        iteration += 1


if __name__ == "__main__":
    main()
