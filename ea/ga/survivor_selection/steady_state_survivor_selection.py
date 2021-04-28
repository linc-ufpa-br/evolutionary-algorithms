from .survivor_selection import SurvivorSelection

class SteadyStateSurvivorSelection(SurvivorSelection):
    
    def replace_population(self, population, size_replace):
        def duplicate(i):
            for j in population[0]:
                if i.chromossome == j.chromossome:
                    return False
            return True
        children = list(filter(duplicate, population[1][:size_replace]))
        size_replace_calc = len(population[0]) - (size_replace - (size_replace - len(children)))
        population_total = []
        population[0].sort(key=lambda x: x.fitness, reverse=True)
        population_total.extend(population[0][:size_replace_calc])
        population_total.extend(children)
        return population_total