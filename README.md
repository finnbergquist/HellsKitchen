# Soup Recipe Generator
## Repo Link: https://github.com/finnbergquist/HellsKitchen


## Overview
This program implements a simplified version of PIERRE (a genetic algorithm that generates soup recipes):
http://computationalcreativity.net/iccc2012/wp-content/uploads/2012/05/119-Morris.pdf

## Description
### Genetic Algorithm:

* **Generation**: The initial population is created

* **Selection**: Each member is assessed according to a fitness function (in the program's case, this is the degree of ingredient variety). Recipes with high fitness scores are more likely to be chosen as future parents. Their probability of selection is proportional to their fitness. 

* **Crossover**: New offspring are created by combining the genetic information from the selected parents. In the context of the program, the genetic information of an individual is its list of ingredients. The ingredients before a random pivot in one recipe will now be merged with the ingredients after the random pivot from another recipe.

* **Mutation**: Introduce new variety into the population. Each recipe in the new generation is subject to a random chance of mutation, of which there are four types:
  
    * randomly pick an ingredient in its recipe, randomly change its amount
    * change one ingredient to another, randomly, use the same ammount
    * addition of a random ingredient
    * deletion of a random ingredient


## Running the Program
First, make sure the following dependencies are installed: numpy, glob.

In the command prompt, navigate to the directory that contains `evolve.py`. Then type:
```
python3 evolve.py <inspiring set path> <output directory path> <generations>
```
where:
1. Inspiring set path is the filepath for the directory containing the initial recipes
2. Generations is the number of iterations the program should run for
3. Output directory path is the filepath for the directory where the final recipes should be written to

For example, the following command: 
```
python3 evolve.py inspiring_set output 10
```
would specify to run the program with the text files from the inspiring_set directory as the initial population for 10 generations and store the final recipes in a folder named output located in the current directory.


## Authors

Finn Bergquist

Lily Smith

Crystal Chong

Souleman Toure


