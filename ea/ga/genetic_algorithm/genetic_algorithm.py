import copy
class GeneticAlgorithm():
    
    def __init__(self, population, individual_class, mutation, crossover, stop_criterion, survivor_selection, parent_selection, population_model, function_fitness, type_fitness):
        self.__population = population
        self.__individual_class = individual_class
        self.__mutation = mutation
        self.__crossover = crossover
        self.__stop_criterion = stop_criterion
        self.__survivor_selection = survivor_selection
        self.__parent_selection = parent_selection
        self.__population_model = population_model
        self.__function_fitness = function_fitness
        self.__result = []
        self.__type_fitness = type_fitness
        
    def execute(self):
        self.__calc_fitness(self.__population)
        self.__type_fitness.insert_fitness(self.__population)
        self.__population.sort(key=lambda x: x.fitness, reverse=True)
        self.__result.append(self.__population)
        while self.__stop_criterion.continue_generation():
            #print(self.__population)
            new_population = []
            parents = self.__parent_selection.selection(self.__population_model.size_replace(self.__population), self.__population)
            for parent in parents:
                children = self.__crossover.execute_crossover(parent[0].chromossome, parent[1].chromossome)
                for child in children:
                    muteted_child = self.__mutation.execute_mutation(child)
                    #print(muteted_child)
                    #print('pulou muteted')
                    new_individual = self.__individual_class(chromossome=muteted_child)
                    #print(new_individual)
                    #print('pulou indi')
                    new_population.append(new_individual)
                    del muteted_child
                    del new_individual
            total_population = copy.deepcopy(self.__population)
            self.__calc_fitness(new_population)
            self.__type_fitness.insert_fitness(new_population)
            survivors = self.__survivor_selection.replace_population([total_population, new_population],self.__population_model.size_replace(self.__population))
            self.__population = survivors
            self.__population.sort(key=lambda x: x.fitness, reverse=True)
            self.__result.append(self.__population)
            
    
    def __calc_fitness(self, individuals):
        for i in individuals:
            i.avaliation, i.decode = self.__function_fitness.calc_fitness(i.chromossome)
    
    def get_result(self):
        return self.__result
    
    
    