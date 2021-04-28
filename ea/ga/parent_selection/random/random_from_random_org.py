from .random import Random

class RandomFromRandomOrg(Random):
    
    MAX_VALUE = 1000000000 # maior valor permitido do random org
    MIN_VALUE = 0
 
    def random(self):
        return self.random_generator.generate_decimal_fractions(1, 14)
    
    def randrange(self, min_value, max_value):
        return self.random_generator.generate_integers(1, min_value, max_value)
    
    def uniform(self, min_value, max_value):
        return self.random_generator.generate_integers(1, min_value, max_value) + self.clientRandomOrg().generate_decimal_fractions(1, 14)
    
    def gauss(self, mean, standart_desviation):
        return self.random_generator.generate_gaussians(1, mean, standart_desviation, 14)