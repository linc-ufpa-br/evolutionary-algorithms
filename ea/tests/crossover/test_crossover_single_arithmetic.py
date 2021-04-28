# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:56:52 2020

@author: georg
"""
import unittest
import sys
sys.path.append("../../")
from ga.crossover.crossover_single_arithmetic import CrossoverSingleArithmetic
from unittest.mock import MagicMock

class TestCrossoverSingleArithmetic(unittest.TestCase):

    """
        inicialição de váriaveis e instâncias antes de cada execução de teste
    """
    def setUp(self):
        pass
        
        
    """
        deve lançar uma exerção IndexError quando não houver individuos na população
    """
    def test_children_list_is_equal_then_list_expected(self):
        random_generator = MagicMock
        random_numbers = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5] # lista contendo elementos aleatorios
        index_of_first_element = 0
        random_generator.random = MagicMock(side_effect = lambda: random_numbers.pop(index_of_first_element))
        position_gene = 2
        random_generator.randrange = MagicMock(return_value = position_gene)
        random_points = False
        parent_1 = [0, 1, 1, 1, 0]
        parent_2 = [1, 0, 1, 0, 1]
        child_1_expected = [0, 1, 1.0, 0.5, 0.5]
        child_2_expected = [1, 0, 1.0, 0.5, 0.5]
        list_expected = (child_1_expected, child_2_expected)
        probability = 0.9 # 90%
        crossover = CrossoverSingleArithmetic(random_generator, probability)
        children = crossover.execute_crossover(parent_1, parent_2)
        self.assertTupleEqual(list_expected, children)
        
        
        
if __name__ == '__main__':
    unittest.main()