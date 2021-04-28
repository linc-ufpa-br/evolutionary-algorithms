from .population_model import PopulationModel
class SSGAPopulationModel(PopulationModel):
    
    def size_replace(self, individuals):
        return round(1 / len(self.individuals) * 100)