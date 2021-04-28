from .factory_individual import FactoryIndividual
from ..individual.individual_real import IndividualReal

class FactoryIndividualReal(FactoryIndividual):
    
    def factory_method(self, random_generator, size_chromossome, min_value, max_value):
        individual = IndividualReal()
        individual.init_random_chromossome(random_generator, size_chromossome, min_value, max_value)
        return individual
    