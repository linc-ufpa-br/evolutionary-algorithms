from .crossover import Crossover

class CrossoverNPointRandom(Crossover):
    def __init__(self, random_generator, probability):
        super().__init__(random_generator, probability)
    
    
    def execute_crossover(self, parent_1, parent_2):
        if self.confirm_execution():
            index_last = -1
            index_first = 0
            n_points_min = 1
            n_points = self.random_generator.randrange(n_points_min, len(parent_1))
            points = []
            for i in range(n_points):
                point = self.random_generator.randrange(index_first, len(parent_1) + index_last)
                points.append(point)
            points.sort()
            child_1 = []
            child_2 = []
            point = points.pop(index_first)
            inverse = False
            for i in (range(len(parent_1))):
                if i == point:
                    inverse = not inverse
                    if len(points) != 0:
                        point = points.pop(index_first)
                if inverse:
                    child_1.append(parent_2[i])
                    child_2.append(parent_1[i])
                else:
                    child_1.append(parent_1[i])
                    child_2.append(parent_2[i])
            return child_1, child_2
        return parent_1, parent_2