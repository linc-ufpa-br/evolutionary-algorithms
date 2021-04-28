from .abstract_factory_type import AbstractFactoryType
from ..individual.individual_binary import IndividualBinary
from ..mutation.mutation_binary import MutationBinary
from ..crossover.crossover_uniform import CrossoverUniform

class ConcreteFactoryTypeBinary(AbstractFactoryType):
    """
    Implement the operations to create concrete product objects.
    """
    
    def create_individual(self):
        return IndividualBinary

    def create_mutation(self):
        return MutationBinary

    def create_crossover(self):
        return CrossoverUniform