from .crossover import Crossover

class CrossoverUniform(Crossover):
    def __init__(self, random_generator, probability):
        super().__init__(random_generator, probability)
    
    
    def execute_crossover(self, parent_1, parent_2):
        if self.confirm_execution():
            value_head = 0
            value_tail = 1
            child_1 = []
            child_2 = []
            for i in (range(len(parent_1))):
                random_value = self.random_generator.randrange(value_head, value_tail)
                if random_value == value_head:
                    child_1.append(parent_1[i])
                    child_2.append(parent_2[i])
                else:
                    child_1.append(parent_2[i])
                    child_2.append(parent_1[i])
            return child_1, child_2
        else:
            return parent_1, parent_2