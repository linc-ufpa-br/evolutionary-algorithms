from .population_model import PopulationModel
class PercentPopulationModel(PopulationModel):
    
    def __init__(self):
        self.__percent = 1.0;
    
    def set_percent(self, percent):
        self.__percent = percent
    
    def size_replace(self, individuals):
        value = round(len(individuals) * self.__percent)
        if value > 0:
            return value
        else: 
            return 1