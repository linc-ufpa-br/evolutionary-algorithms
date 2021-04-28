from .stop_criterion import StopCriterion

class StopCriterionForGeneration(StopCriterion):
    
    def __init__(self, generation_max):
        self.__generation_max = generation_max
        self.__generation_actual = 0
    
    @property
    def generation_actual(self):
        return self.__generation_actual
    
    def continue_generation(self):
        
        if self.__generation_actual < self.__generation_max:
            self.__generation_actual = self.__generation_actual + 1
            return True
        else:
            return False