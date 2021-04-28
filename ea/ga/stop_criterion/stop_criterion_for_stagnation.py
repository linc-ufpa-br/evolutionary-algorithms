from .stop_criterion import StopCriterion

class StopCriterionForStagnation(StopCriterion):
    
    def __init__(self, generation_stagnation_max, best_result):
        self.__generation_stagnation_max = generation_stagnation_max
        self.__best_result = best_result
        self.__generation_stagnation_actual = 0
    
    @property
    def best_result(self):
        return self.__generation_actual
    
    @best_result.setter
    def best_result(self, best_result):
        if best_result == self.__best_result:
            self.__generation_stagnation_actual = self.__generation_stagnation_actual + 1
        else:
            self.__generation_stagnation_actual = 0
            self.__best_result = best_result
    
    def continue_generation(self):
        return self.__generation_stagnation_actual < self.__generation_stagnation_max