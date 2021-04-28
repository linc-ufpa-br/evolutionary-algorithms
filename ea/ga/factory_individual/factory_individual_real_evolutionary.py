from .factory_individual import FactoryIndividual
from ..individual.individual_real_evolutionary import IndividualRealEvolutionary

class FactoryIndividualRealEvolutionary(FactoryIndividual):
    
    def factory_method(self, random_generator, size_chromossome, min_value, max_value):
        individual = IndividualRealEvolutionary()
        individual.init_random_chromossome(random_generator, size_chromossome, min_value, max_value)
        return individual
    