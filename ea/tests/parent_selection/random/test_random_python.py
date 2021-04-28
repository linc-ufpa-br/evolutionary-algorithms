# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:56:52 2020

@author: georg
"""
import unittest
import sys
sys.path.append("../")
from ga.parent_selection.random.random_python import RandomPython
import random
from unittest.mock import MagicMock

class TestRandomPython(unittest.TestCase):

    """
        inicialição de váriaveis e instâncias antes de cada execução de teste
    """
    def setUp(self):
        random_python = random
        value_between_0_and_1 = 0.5
        random_python.random = MagicMock(return_value = value_between_0_and_1)
        self.random = RandomPython(random_python)
    
    """
        deve retornar um numero aleatorio entre 0.0 e 1.0
    """
    def test_return_value_between_0_and_1(self):
        min_value = 0.0
        max_value = 1.0
        value = self.random.random()
        self.assertGreaterEqual(value, min_value)
        self.assertLessEqual(value, max_value)
    
    def test_randrange_function_return_value_between_min_value_and_max_value(self):
        min_value = 0
        max_value = 10
        value_between_min_and_max_value = 6
        random_python = random
        random_python.randrange = MagicMock(return_value = value_between_min_and_max_value)
        random_instance = RandomPython(random_python)
        value = random_instance.randrange(min_value, max_value)
        self.assertGreaterEqual(value, min_value)
        self.assertLessEqual(value, max_value)
        
if __name__ == '__main__':
    unittest.main()