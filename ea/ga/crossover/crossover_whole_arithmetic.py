from .crossover_arithmetic import CrossoverArithmetic

class CrossoverWholeArithmetic(CrossoverArithmetic):
    def __init__(self, random_generator, probability, alfa = None):
        super().__init__(random_generator, probability, alfa)
    
    
    def execute_crossover(self, parent_1, parent_2):
        if self.confirm_execution():
            child_1 = []
            child_2 = []
            for i in (range(len(parent_1))):
                if self.alfa == None:
                    alfa = self.random_generator.random()
                else: 
                    alfa = self.alfa
                new_gene_child_1 = parent_1[i] * alfa + (1 - alfa) * parent_2[i]
                new_gene_child_2 = parent_2[i] * alfa + (1 - alfa) * parent_1[i]
                child_1.append(new_gene_child_1)
                child_2.append(new_gene_child_2)
                
            return child_1, child_2
        else: 
            return parent_1, parent_2