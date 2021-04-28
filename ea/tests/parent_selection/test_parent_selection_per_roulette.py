# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:56:52 2020

@author: georg
"""
import unittest
import sys
sys.path.append("../")
from ga.parent_selection.parent_selection_per_roulette import ParentSelectionPerRoulette
from ga.parent_selection.random.random import Random
from unittest.mock import MagicMock

class TestParentSelectionPerRoulette(unittest.TestCase):

    """
        inicialição de váriaveis e instâncias antes de cada execução de teste
    """
    def setUp(self):
        self.length_population = 4
        self.individuals = []
        for x in range(self.length_population):
            individual = MagicMock(fitness=x)
            individual.__add__ = lambda a, b: a.fitness + b.fitness
            self.individuals.append(individual)
        random = Random(MagicMock())
        self.random_number = 0.75
        random.random = MagicMock(return_value = self.random_number)
        self.parent_selection = ParentSelectionPerRoulette(self.individuals, random)
        
        
    """
        deve lançar uma exerção IndexError quando não houver individuos na população
    """
    def test_dont_have_individuals(self):
        random = Random(MagicMock)
        random.random = MagicMock(return_value = 0.5)
        with self.assertRaises(IndexError):
            parent_selection = ParentSelectionPerRoulette([], random)
    
    """
        o elemento deve possuir a fração na roleta de acordo com seu fitness
    """
    def test_element_have_exactly_value_fraction_in_roulette(self):
        element_index = 0
        element_fraction_expected = self.individuals[element_index].fitness / (sum(range(self.length_population)))
        self.assertAlmostEqual(element_fraction_expected, self.parent_selection.fractions[element_index])
    
    """
        a soma das frações deve ser igual a 100%
    """
    def test_fractions_must_be_equal_hundred_percent(self):
        sum_expected = 1.0
        sum_fractions = sum(self.parent_selection.fractions)
        self.assertAlmostEqual(sum_expected, sum_fractions)
        
    """
        o elemento da lista selecionado deve ser o que tiver um valor de fração que somado com 
        os anteriores (se houver) seja igual ou maior que o valor aleatorio. 
    """
    def test_selected_have_value_almost_or_equal_then_random_number(self):
        fractions = self.parent_selection.fractions
        acumulator = 0.0
        selected = 0
        for i in range(len(fractions)):
            acumulator = acumulator + fractions[i]
            if acumulator > self.random_number:
                selected = i
                break
        element_expected = self.individuals[selected]
        element_selected = self.parent_selection.selection()
        self.assertEqual(element_expected, element_selected)
        
if __name__ == '__main__':
    unittest.main()