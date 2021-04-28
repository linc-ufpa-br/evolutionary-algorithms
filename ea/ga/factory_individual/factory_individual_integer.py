from .factory_individual import FactoryIndividual
from ..individual.individual_integer import IndividualInteger


class FactoryIndividualInteger(FactoryIndividual):

    def factory_method(self, random_generator, size_chromossome, min_value, max_value):
        individual = IndividualInteger()
        individual.init_random_chromossome(random_generator, size_chromossome, min_value, max_value)
        return individual