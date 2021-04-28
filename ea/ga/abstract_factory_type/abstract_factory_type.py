"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

import abc


class AbstractFactoryType(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract product
    objects.
    """

    @abc.abstractmethod
    def create_individual(self):
        pass

    @abc.abstractmethod
    def create_mutation(self):
        pass
    
    @abc.abstractmethod
    def create_crossover(self):
        pass