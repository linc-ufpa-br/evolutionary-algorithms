from .survivor_selection import SurvivorSelection

class GenitorSurvivorSelection(SurvivorSelection):
    
    def replace_population(self, population, size_replace):
        population[0].sort(key=lambda x: x.fitness, reverse=True)
        survivors = population[1][:-1]
        survivors.append(population[0][0])
        return survivors