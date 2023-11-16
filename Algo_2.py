import numpy
import random
def cal_pop_fitness(new_population, name, num_of_letters):
    #This function calculates the fitness value of each solution in the current Population
    #The fitness function judges whether the letter we want is in the correct space
    #If a letter is in the correct position, we give the fitness function +2 points
    #If a correct letter is in the array but in an incorrect position, we give the fitness function +1 points
     
     out_position = []
     in_position = []
     #print("\nIN POSITION\n")
     x = 0
     while x<num_of_letters:
       for row in new_population:
         #print(new_population[x])
         counter_in_position = 0
         y=0
         for i in row:
             if i==name[y]:
                 counter_in_position = counter_in_position+10
             y = y+1
         in_position.append(counter_in_position)
         in_position_array = numpy.array(in_position)
         #print("\n" +str(counter_in_position))
         x = x+1

         #print("\nOUT OF POSITION\n")
     y = 0
     while y<num_of_letters:
       for row in new_population:
          counter_out_of_position =0
          for letter in row:
               if letter in name:
                    counter_out_of_position = counter_out_of_position + 3
                    
          y = y+1
          out_position.append(counter_out_of_position)
     out_position_array = numpy.array(out_position)
         
     
    
     #print("Out of position: ")
     #print(out_position_array)
     #print("In position: ")
     #print(in_position_array)
  
     
     fitness = out_position_array + in_position_array
     #print("Fitness Array: ")
     #print(fitness)
     return fitness
     
    #"fitness" corresponds to the sum of products of a chromosone. The highest "fitness" indicates the one that approximates the solution we require the best.

def select_mating_pool(new_population, fitness, num_parents):
    # Selecting the best individuals in the current generation as num_parents
    parents = numpy.empty((num_parents, new_population.shape[1]), dtype = numpy.unicode_)
    #print(parents)
   #This line of code generates an empty array with 4 rows (num of parents) and 5 columns.
    x = 1
    for i in range(num_parents):
        max_fitness_idx = numpy.where(fitness==numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        #print("Max Fitness Index:" +str(x))
        #rint(max_fitness_idx)
        x = x+1
        parents[i, :] = new_population[max_fitness_idx, :]
        fitness[max_fitness_idx] = -10
        
    return parents
    
    #In this block of code, in the first loop the max fitness idx is set to the index of the row in "fitness" with the maximum fitness coefficient.
    #The top row of the parents array is then appended with the with the maximum fitness. This fitness value is then set to a value that is so low it is unlikely to 
    #be the next fittest value. This loop is repeated 4 times to obtain the parents array.

#offspring_size=(pop_size[0]-parents.shape[0]
def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size, dtype = numpy.unicode_)
    
    #The point at which crossover takes place between two parents.
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        #Index of the first parent to mate
        parent1_idx = k%parents.shape[0]
        #Index of the second parent to mate
        parent2_idx = (k+1)%parents.shape[0]
        #The new offspring will have the first half of its genes taken from one parent, and the second half from the other
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring
    print(offspring)
def mutation(offspring_crossover, alphabet, num_of_letters_1):
    #Mutation changes a single gene in each offspring randomly.
    for i in range(offspring_crossover.shape[0]):
        #The random value to be added to the gene.
        new_num = random.randint(0,num_of_letters_1)
        new_num_2 = random.randint(0,num_of_letters_1)
        random_value = numpy.random.choice(list(alphabet))
        random_value_2 = numpy.random.choice(list(alphabet))
        offspring_crossover[i][new_num] = random_value
        offspring_crossover[i][new_num_2] = random_value_2
    return offspring_crossover
