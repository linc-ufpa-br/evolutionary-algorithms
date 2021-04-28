from .survivor_selection import SurvivorSelection

class AgeSurvivorSelection(SurvivorSelection):
    
    def replace_population(self, population, size_replace):
        population.sort(key=lambda x: x.age)
        survivors = len(population) - size_replace
        return population[0:survivors - 1]