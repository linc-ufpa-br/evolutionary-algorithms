from .population_model import PopulationModel
class SGAPopulationModel(PopulationModel):
    
    def size_replace(self, population):
        return len(population)