# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:56:52 2020

@author: georg
"""
import unittest
import sys
sys.path.append("../../")
from ga.mutation.mutation_gaussiana import MutationGaussiana
from unittest.mock import MagicMock

class TestMutationGaussiana(unittest.TestCase):

    """
        inicialição de váriaveis e instâncias antes de cada execução de teste
    """
    def setUp(self):
        pass
        
        
    """
        deve lançar uma exerção IndexError quando não houver individuos na população
    """
    def test_chromossome_is_equal_then_chromossome_expected(self):
        random_generator = MagicMock
        random_numbers = [0.5, 0.5, 0.03, 0.5, 0.5] # lista contendo elementos aleatorios
        index_of_first_element = 0
        random_generator.gauss = MagicMock(return_value=0.3)
        random_generator.random = MagicMock(side_effect = lambda: random_numbers.pop(index_of_first_element))
        chromossome = [0, 1, 1, 1, 0]
        chromossome_expected = [0, 1, 0.3, 1, 0]
        probability = 0.05
        desviation= 9.0
        generation_actual = 1
        mutation = MutationGaussiana(random_generator, probability, desviation, generation_actual)
        chromossome_result = mutation.execute_mutation(chromossome)
        self.assertListEqual(chromossome_expected, chromossome_result)
        
        
        
if __name__ == '__main__':
    unittest.main()