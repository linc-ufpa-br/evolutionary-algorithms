from .mutation import Mutation
class MutationGaussiana(Mutation):
    def __init__(self, random_generator, probability, desviation, generation_actual):
        super().__init__(random_generator, probability)
        self.__desviation = desviation
        self.__generation_actual = generation_actual
        
    def execute_mutation(self, chromossome):
        chromossome_mutated = []
        for i in range(len(chromossome)):
            if self.confirm_execution():
                desviation_actual = self.__desviation / self.__generation_actual
                chromossome_mutated.append(self.random_generator.gauss(chromossome[i], desviation_actual))
            else:
                chromossome_mutated.append(chromossome[i])
        return chromossome_mutated