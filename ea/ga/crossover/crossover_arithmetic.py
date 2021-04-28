from .crossover import Crossover

class CrossoverArithmetic(Crossover):
    def __init__(self, random_generator, probability, alfa = None):
        super().__init__(random_generator, probability)
        self.__alfa = alfa
        
    @property
    def alfa(self):
        return self.__alfa