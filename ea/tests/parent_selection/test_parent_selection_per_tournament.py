# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:56:52 2020

@author: georg
"""
import unittest
import sys
sys.path.append("../")
from ga.parent_selection.parent_selection_per_tournament import ParentSelectionPerTournament
from ga.parent_selection.subgroup.subgroup import Subgroup
from unittest.mock import MagicMock

class TestParentSelectionPerTournament(unittest.TestCase):

    """
        inicialição de váriaveis e instâncias antes de cada execução de teste
    """
    def setUp(self):
        length_population = 4
        length_subgroup = 4
        self.individuals = []
        for x in range(length_population):
            individual = MagicMock(fitness=x)
            self.individuals.append(individual)
        self.subgroup = Subgroup()
        self.subgroup.create_subgroup = MagicMock(return_value=self.individuals)
        self.parent_selection = ParentSelectionPerTournament(self.individuals, self.subgroup)
        
        
    """
        deve lançar uma exerção IndexError quando não houver individuos na população
    """
    def test_dont_have_individuals(self):
        subgroup = Subgroup()
        subgroup.create_subgroup = MagicMock(return_value=self.individuals)
        with self.assertRaises(IndexError):
            parent_selection = ParentSelectionPerTournament([], subgroup)
            

    """
        deve retornar o melhor individuo do subgrupo
    """
    def test_have_return_the_best_individual_of_subgroup(self):
        best_individual = self.individuals[-1]
        selected_individual = self.parent_selection.selection()
        self.assertEqual(best_individual, selected_individual)
        

        
        
        
if __name__ == '__main__':
    unittest.main()