from .survivor_selection import SurvivorSelection

class SGASurvivorSelection(SurvivorSelection):
    
    def replace_population(self, populations, size_replace):
        return populations[1]