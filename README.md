# CSCI 3725 - PQ1 Let's Get Cooking
## Overview
This program implements a simplified version of PIERRE (a genetic algorithm that generates soup recipes).
A genetic algorithm consists of the following steps:
<br />
<b>Generation</b>: The initial population is created

<b>Selection</b>: Each member is assessed according to a fitness function (in the program's case, this is the degree of ingredient variety). Recipes with high fitness scores are more likely to be chosen as future parents.

<b>Crossover</b>: New offspring are created by combining teh genetic information from the selected parents. In the context of the program, the genetic information of an individual is its list of ingredients.

<b>Mutation</b>: Introduce new variety into the population. The genetic information of an individual has a certain chance of being modified.
<br />
<br />

## Running the Program
In the command prompt, navigate to the directory that contains `evolve.py`. Then type: `python3 evolve.py <inspiring set path> <output directory path> <generations>`
where:
1. Inspiring set path is the filepath for the directory containing the initial recipes
2. Generations is the number of iterations the program should run for
3. Output directory path is the filepath for the directory where the final recipes should be written to

For example, the following command: `python3 evolve.py inspiring_set output 10` would specify to run the program with the text files from the inspiring_set directory as the initial population for 10 generations and store the final recipes in a folder named output located in the current directory.