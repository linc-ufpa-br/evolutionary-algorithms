class Random:
    
    def __init__(self, random_generator):
        self.__random_generator = random_generator
        
    @property
    def random_generator(self):
        return self.__random_generator
    
    def random(self):
        pass
    
    def randrange(self, min_value, max_value):
        pass
    
    def uniform(self, min_value, max_value):
        pass
    
    def gauss(self, media, desviation):
        pass