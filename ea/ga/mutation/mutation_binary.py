from .mutation import Mutation
class MutationBinary(Mutation):
    def __init__(self, random_generator, probability):
        super().__init__(random_generator, probability)
        
    def execute_mutation(self, chromossome):
        chromossome_mutated = []
        for i in range(len(chromossome)):
            if self.confirm_execution():
                if chromossome[i] == 0:
                    chromossome_mutated.append(1)
                else:
                    chromossome_mutated.append(0)
            else:
                chromossome_mutated.append(chromossome[i])
        return chromossome_mutated