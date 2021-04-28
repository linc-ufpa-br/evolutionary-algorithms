from ga.interfaces.probability_execution import ProbabilityExecution
class Mutation(ProbabilityExecution):
    def __init__(self, random_generator, probability):
        super().__init__(random_generator, probability)
    
    def execute_mutation(self, chromossome):
        pass
            