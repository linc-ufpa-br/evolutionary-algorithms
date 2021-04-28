class ProbabilityExecution:
    def __init__(self, random_generator, probability):
        self.__random_generator = random_generator
        self.__probability = probability
        
    @property
    def random_generator(self):
        return self.__random_generator
    
    def confirm_execution(self):
        random_value = self.__random_generator.random()
        if random_value <= self.__probability:
            return True
        else:
            return False
    
