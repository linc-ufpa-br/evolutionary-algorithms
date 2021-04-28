from .mutation import Mutation
class MutationReal(Mutation):
    def __init__(self, random_generator, probability, min_value, max_value):
        super().__init__(random_generator, probability)
        self.__min_value = min_value
        self.__max_value = max_value
        
    def execute_mutation(self, chromossome):
        chromossome_mutated = []
        for i in range(len(chromossome)):
            if self.confirm_execution():
                chromossome_mutated.append(self.random_generator.uniform(self.__min_value, self.__max_value))
            else:
                chromossome_mutated.append(chromossome[i])
        return chromossome_mutated