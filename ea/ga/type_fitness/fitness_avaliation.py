from .type_fitness import TypeFitness
class FitnessAvaliation:
    
    def insert_fitness(self, population):
        for i in population:
            i.fitness = i.avaliation