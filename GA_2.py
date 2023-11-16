import numpy 
import Algo_2
import random

"""
We seek to maximise this statement:

"""
#Alphabet list
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

name =input("Enter the statement you want to optimise: ")
name = name.lower()

num_of_letters = len(name)
num_of_letters_1 = len(name) - 1
#num_of_letters is equal to the number of letters in each chromosone, therefore the number of letters in the phrase we want
sol_per_pop = 16
#sol_per_pop refers to the number of chromosones in each generation
num_parents = 8

#Defining the population size: The number of chromosones multiplied by the number of inputs.

pop_size = (sol_per_pop, num_of_letters)

"""
The pop_size variable details the total population size.
This corresponds to the number of chromosones (sol_per_pop), multiplied by the number of genes (num_weights).
"""
#Creating the initial population.

new_population = numpy.random.choice(list(alphabet), size=pop_size)
#print(new_population)
#print(new_population.shape[1])
#Stating the number of generations

num_generations=int(input("How many generations do you want to run through? "))
for generation in range(num_generations+1):
    print("Generation : " + str(generation))
    print(new_population[0])
#Deducing the fitness of each chromosone in the population.
    fitness = Algo_2.cal_pop_fitness(new_population, name, num_of_letters)
    

#Selecting the best parents in the population for mating.
    parents = Algo_2.select_mating_pool(new_population, fitness, num_parents)
    

#Generating the next generation using crossover.
    offspring_crossover = Algo_2.crossover(parents, offspring_size=(pop_size[0]-parents.shape[0], num_of_letters))
    

#Adding some variations to the offspring using mutation
    offspring_mutation = Algo_2.mutation(offspring_crossover, alphabet, num_of_letters_1)

# Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

#The best result in the current iteration.
    #print("The best result so far is:")
    #print(parents[0])
    

