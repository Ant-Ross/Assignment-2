# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:59:47 2019

@author: mcyitlr4
"""

import random

class Particle:
    def __init__(self, x, y, start_height):
        self.x = x
        self.y = y
        self.height = start_height
    
    def direction(self) :
        if random.random() <= 0.75:
            self.x = (self.x + 1) % 300 # change the boundary rule
        elif 0.75 < random.random() <= 0.85: # You are generating new random numbers. We need to use the same one.
            self.x = (self.x - 1) % 300 
       