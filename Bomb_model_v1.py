# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:45:31 2019

@author: mcyitlr4
"""

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
    for value in row:
        if value != 0:
            x = row.index(value)
            y = row_counter
            #print("Weapon located at coordinates","x =", x, "y =", y)
            print(environment[y][x])
    row_counter += 1

# Parameters          
start_height = 76
num_of_particles = 5000
particles = []

# Creating particles
for i in range(num_of_particles):
    particles.append(agent_particle.Particle(x, y, start_height))

# Spreading the particles. The algorithm will move each particle, one by one, 
# until it reaches the ground.
    
for j in range(len(particles)):
    while particles[j].height != 0:
        particles[j].direction()
        particles[j].fall()
        #print("particle", j, particles[j].height, "m")

    
# Plotting particles
for z in range(len(particles)):
    environment[particles[z].y][particles[z].x] += 5

    
max(environment)


#for k in range(len(particles)):
#   matplotlib.pyplot.scatter(particles[k].x,particles[k].y, color='green')
#matplotlib.pyplot.scatter(x,y, color='red')
matplotlib.pyplot.imshow(environment)            
#matplotlib.pyplot.ylim(0, 300)
#matplotlib.pyplot.xlim(0, 300)


#environment[particles[0].y][particles[0].x] = 150
#print((particles[0].y),(particles[0].x))  

#print(environment[particles[0].y][particles[0].x])
#print(environment[159][99])