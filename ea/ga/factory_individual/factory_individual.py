from abc import ABC, abstractmethod
class FactoryIndividual(ABC):
    
    @abstractmethod
    def factory_method(self, random_generator, size_chromossome, min_value, max_value):
        pass
    
    def create_individuals(self, number_of_individuals, random_generator, size_chromossome, min_value, max_value):
        individuals = []
        for i in range(number_of_individuals):
            individual = self.factory_method(random_generator, size_chromossome, min_value, max_value)
            individuals.append(individual)
        return individuals