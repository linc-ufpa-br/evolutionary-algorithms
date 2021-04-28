import numpy as np
import math
class Result:
    
    def return_fitness(self, individuals):
        data_fitness = []
        for geracao in individuals:
            generation_fitness = []
            for individual in geracao:
                generation_fitness.append(individual.avaliation)
            data_fitness.append(generation_fitness)
        
        return np.array(data_fitness)
        
    def return_best_fitness(self, data_fitness):
        data_best = []
        for geracao in data_fitness:
            data_best.append(geracao[0])
        return np.array(data_best)
    
    def return_lowest_fitness(self, data_fitness):
        data_lowest = []
        for geracao in data_fitness:
            data_lowest.append(geracao[-1])
        return np.array(data_lowest)
    
    def return_media(self, data_fitness):
        return np.mean(data_fitness, axis=1)
    
    def return_std(self, data_fitness):
        return np.std(data_fitness, axis=1)
    
    def return_mdf(self, media, best):
        return media/best
    
    def return_euclidian(self, individuals):
        data = []
        pairs = ( len(individuals[0]) * ( len(individuals[0]) - 1) ) / 2
        for geracao in individuals:
            sum_euclidian = 0
            for x in range(len(geracao)):
                for j in range((x + 1), len(geracao)):
                    for k in range(len(geracao[0].chromossome) // 2):
                        sum_euclidian = sum_euclidian + math.sqrt((geracao[x].chromossome[k] - geracao[j].chromossome[k]) ** 2)
            data.append((sum_euclidian / pairs))
        return np.array(data)

    def return_hamming(self, individuals):
        data = []
        pairs = ( len(individuals[0]) * ( len(individuals[0]) - 1) ) / 2
        for geracao in individuals:
            sum_hamming = 0
            for x in range(len(geracao)):
                for j in range((x + 1), len(geracao)):
                    for k in range(len(geracao[0].chromossome)):
                        if geracao[x].chromossome[k] != geracao[j].chromossome[k]:
                            sum_hamming = sum_hamming + 1
            data.append((sum_hamming / pairs))
        return np.array(data)    
    