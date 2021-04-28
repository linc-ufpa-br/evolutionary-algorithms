from .survivor_selection import SurvivorSelection

class MiPlusLambdaSurvivorSelection(SurvivorSelection):
    
    def replace_population(self, population, size_replace):
        population_total = []
        population_total.extend(population[0])
        population_total.extend(population[1])
        population_total.sort(key=lambda x: x.fitness, reverse=True)
        return population_total[:size_replace]