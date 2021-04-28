from ga.interfaces.probability_execution import ProbabilityExecution
class Crossover(ProbabilityExecution):
    def __init__(self, random_generator, probability):
        super().__init__(random_generator, probability)
    
    def execute_crossover(self, parent_1, parent_2):
        pass
            