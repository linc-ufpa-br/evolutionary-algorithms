from .individual import Individual

class IndividualInteger(Individual):
    
    def __init__(self, fitness = 0.0, chromossome = [], age = 0):
        super().__init__(fitness, chromossome, age)

    def init_random_chromossome(self, random_generator, size_chromossome, min_value, max_value):
        chromossome = []
        for i in range(size_chromossome):
            random_value = random_generator.randrange(min_value, max_value)
            chromossome.append(random_value)
        self.chromossome = chromossome