from .type_fitness import TypeFitness
class FitnessNormalization:
    
    def __init__(self, max, min):
        self.__max = max
        self.__min = min
    
    def insert_fitness(self, population):
        population.sort(key=lambda x: x.avaliation, reverse=False)
        for i in range(len(population)):
            fitness = self.__min + ((self.__max - self.__min) / (len(population) - 1)) * ((i + 1) - 1)
            population[i].fitness = fitness
    
    