from .mutation import Mutation
import math
class MutationGaussianaEvolutionary(Mutation):
    def __init__(self, random_generator, probability):
        super().__init__(random_generator, probability)
        
    def execute_mutation(self, chromossome):
        chromossome_mutated = []
        lenght = len(chromossome) // 2
        for i in range(lenght):
            chromossome_mutated.append(chromossome[i] + self.random_generator.gauss(0, chromossome[i+lenght]))
        for i in range(lenght, len(chromossome)):
            chromossome_mutated.append(chromossome[i] * math.exp(self.random_generator.gauss(0, (1/math.sqrt(2*math.sqrt(lenght))))) * math.exp(self.random_generator.gauss(0, (1/math.sqrt(2*lenght)))))
            
        return chromossome_mutated