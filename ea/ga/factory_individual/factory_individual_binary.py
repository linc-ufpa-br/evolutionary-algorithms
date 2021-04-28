from .factory_individual import FactoryIndividual
from ..individual.individual_binary import IndividualBinary

class FactoryIndividualBinary(FactoryIndividual):
    
    def factory_method(self, random_generator, size_chromossome, min_value, max_value):
        individual = IndividualBinary()
        individual.init_random_chromossome(random_generator, size_chromossome)
        return individual
    