# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:08:47 2020

@author: sasayamoma
"""
import abc

class ParentSelection(abc.ABC):
    
    @abc.abstractmethod
    def selection(self, quantity, items):
        pass