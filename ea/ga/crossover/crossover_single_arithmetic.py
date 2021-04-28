from .crossover_arithmetic import CrossoverArithmetic

class CrossoverSingleArithmetic(CrossoverArithmetic):
    def __init__(self, random_generator, probability, alfa = None):
        super().__init__(random_generator, probability, alfa)
    
    
    def execute_crossover(self, parent_1, parent_2):
        if self.confirm_execution():
            child_1 = []
            child_2 = []
            first_index = 0
            last_index = len(parent_1) - 1
            position_gene = self.random_generator.randrange(first_index, last_index)
            for i in (range(len(parent_1))):
                if i >= position_gene:
                    if self.alfa == None:
                        alfa = self.random_generator.random()
                    else: 
                        alfa = self.alfa
                    new_gene_child_1 = parent_1[i] * alfa + (1 - alfa) * parent_2[i]
                    new_gene_child_2 = parent_2[i] * alfa + (1 - alfa) * parent_1[i]
                    child_1.append(new_gene_child_1)
                    child_2.append(new_gene_child_2)
                else:
                    child_1.append(parent_1[i])
                    child_2.append(parent_2[i])
            
            return child_1, child_2
        else:
            return parent_1, parent_2