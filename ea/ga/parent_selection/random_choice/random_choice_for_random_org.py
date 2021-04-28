#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:53:03 2020

@author: george
"""

from .random_choice import RandomChoice

class RandomChoiceForRandomOrg(RandomChoice):
    
    def __init__(self, request_random_org):
        self.__request_random_org = request_random_org
    
    def choice(self, items):
        super().choice(items)
        min_indice_value = 0
        max_indice_value = len(items) - 1
        random_indice = self.__request_random_org.integer_generator(min_indice_value, max_indice_value)
        return items[random_indice]
    
    