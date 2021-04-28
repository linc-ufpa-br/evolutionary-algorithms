#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:53:03 2020

@author: george
"""
import random

from .random_choice import RandomChoice

class RandomChoiceForPythonRandom(RandomChoice):
    
    def choice(self, items):
        super().choice(items)
        return random.choice(items)