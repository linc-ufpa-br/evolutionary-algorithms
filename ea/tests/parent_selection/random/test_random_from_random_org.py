# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:56:52 2020

@author: georg
"""
import unittest
import sys
sys.path.append("../")
import requests
from ga.parent_selection.random.random_from_random_org import RandomFromRandomOrg
from rdoclient import RandomOrgClient

from unittest.mock import MagicMock

class TestRandomFromRandomOrg(unittest.TestCase):

    """
        inicialição de váriaveis e instâncias antes de cada execução de teste
    """
    def setUp(self):
        value_between_0_and_1000000000 = 3000
        request = RandomOrgClient('')
        request.integer_generator = MagicMock(return_value = value_between_0_and_1000000000)
        self.random = RandomFromRandomOrg(request)
    
    """
        deve retornar um numero aleatorio entre 0.0 e 1.0
    """
    def test_random_function_return_value_between_0_and_1(self):
        min_value = 0.0
        max_value = 1.0
        value = self.random.random()
        self.assertGreaterEqual(value, min_value)
        self.assertLessEqual(value, max_value)
    
    def test_randrange_function_return_value_between_min_value_and_max_value(self):
        min_value = 0
        max_value = 10
        value_between_min_and_max_value = 6
        request = RequestIntegerGeneratorRandomOrg(requests)
        request.integer_generator = MagicMock(return_value = value_between_min_and_max_value)
        random = RandomFromRandomOrg(request)
        value = random.randrange(min_value, max_value)
        self.assertGreaterEqual(value, min_value)
        self.assertLessEqual(value, max_value)
        
if __name__ == '__main__':
    unittest.main()