# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:45:31 2019

@author: mcyitlr4
"""

import random
import matplotlib.pyplot
import matplotlib.animation
import csv
import agent_particle

# Reading environment
f = open('bomb.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:				
    rowlist = []	
    for value in row:
        rowlist.append(value)
        				 
    environment.append(rowlist)  
f.close() 

# Locating the building's coordinates.
row_counter = 0
for row in environment:
    row_counter += 1
    for value in row:
        if value != 0:
            x = row.index(value)
            y = row_counter
            print(x)
            print(row_counter)

# Parameters          
start_height = 75
num_of_particles = 50
particles = []

# Creating particles
for i in range(num_of_particles):
    particles.append(agent_particle.Particle(x, y, start_height))

particles[0].y
matplotlib.pyplot.imshow(environment) 
matplotlib.pyplot.scatter(50,160, marker="*", color='yellow')           

random.random()
