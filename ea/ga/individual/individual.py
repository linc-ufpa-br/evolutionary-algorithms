# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:37:06 2020

@author: georg
"""
import numpy as np

class Individual:
    
    def __init__(self, fitness = 0.0, chromossome = [], age = 0):
        self.__fitness = fitness
        self.__chromossome = chromossome
        self.__age = age
        self.__decode = []
        self.__avaliation = 0.0

    @property
    def fitness(self):
        return self.__fitness
    
    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness
        
    @property
    def decode(self):
        return self.__decode
    
    @decode.setter
    def decode(self, decode):
        self.__decode = decode
    
    @property
    def avaliation(self):
        return self.__avaliation
    
    @avaliation.setter
    def avaliation(self, avaliation):
        self.__avaliation = avaliation
    
    @property
    def age(self):
        return self.__age
    
    def increment_age(self):
        self.__age = self.__age + 1
    
    @property
    def chromossome(self):
        return self.__chromossome

    @chromossome.setter
    def chromossome(self, chromossome):
        self.__chromossome = chromossome
    
    def init_random_chromossome(self, random_generator, size_chromossome, min_value, max_value):
        pass

    def __str__(self):
        return "fitness {} avaliacao {} chromossome {} {}, decode {}".format(self.__fitness, self.__avaliation, self.__chromossome, super.__str__(self), self.__decode)

    
        
        
    