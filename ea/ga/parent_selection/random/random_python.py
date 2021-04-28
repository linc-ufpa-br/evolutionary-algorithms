from .random import Random
class RandomPython(Random):
    
    def __init__(self, random_generator):
        super().__init__(random_generator)
    
    def random(self):
        return self.random_generator.random()
    
    def randrange(self, min_value, max_value):
        return self.random_generator.randrange(min_value, max_value)
    
    def uniform(self, min_value, max_value):
        return self.random_generator.uniform(min_value, max_value)
    
    def gauss(self, media, desviation):
        return self.random_generator.gauss(media, desviation)