#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:51:53 2020

@author: george
"""


class RandomChoice:
    
    def choice(self, items):
        length_items = len(items)
        if(length_items == 0):
            raise ValueError('list dont have elements')
        if(length_items == 1):
            raise ValueError('list dont have only one element')