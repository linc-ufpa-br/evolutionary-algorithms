from .parent_selection import ParentSelection

class ParentSelectionPerRoulette(ParentSelection):
    
    def __init__(self, random):
        self.__fractions = []
        self.__random = random
    
    @property
    def fractions(self):
        return self.__fractions
    
    def selection(self, quantity, items):
        self.__init_roulette(items)
        parents = []
        total_quantity = quantity // 2
        if total_quantity == 0:
            total_quantity = 1
        for j in range(total_quantity):
            parent_group = []
            for k in range(2):
                random = self.__random.random() # valor entre 0.0 e 1.0
                acumulator = 0.0
                selected = 0
                for i in range(len(self.__fractions)):
                    acumulator = acumulator + self.__fractions[i]
                    if acumulator > random:
                        selected = i
                        break
                parent_group.append(items[selected])
            parents.append(parent_group)
        self.__fractions = []
        return parents
        
    def __init_roulette(self, items):
        sum_fitness = 0
        for i in items:
            sum_fitness = sum_fitness + i.fitness
        for i in items:
            value = i.fitness / sum_fitness
            self.__fractions.append(value)
        