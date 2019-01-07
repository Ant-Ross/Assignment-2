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
        rndm = random.random()
        #print(rndm)
        if rndm <= 0.75:
            self.x = (self.x + 1) % 300 # change the boundary rule
        elif 0.75 < rndm <= 0.85: 
            self.x = (self.x - 1) % 300 
        elif 0.85 < rndm <= 0.95:
            self.y = (self.y + 1) % 300
        elif 0.95 < rndm <= 1:
            self.y = (self.y - 1) % 300 
       
    def fall(self):
        if self.height > 75:
            rndm = random.random()
            #print(rndm)
            if rndm <= 0.20:
                self.height += 1
            elif 0.20 < rndm <= 0.30:
                self.height = self.height
            elif 0.30 < rndm <= 1:
                self.height -= 1
        else:
            self.height -= 1
            
          
   