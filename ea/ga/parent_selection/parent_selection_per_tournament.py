from .parent_selection import ParentSelection
from functools import reduce
class ParentSelectionPerTournament(ParentSelection):
    
    def __init__(self, subgroup):
        self.__subgroup = subgroup
    
    def selection(self, individuals):
        subgroup = self.__subgroup.create_subgroup(individuals)
        best_individual = reduce(ParentSelectionPerTournament.__get_best_individual, subgroup)
        return best_individual    
    
    @staticmethod
    def __get_best_individual(indi1, indi2): 
        return indi1 if indi1.fitness >= indi2.fitness else indi2