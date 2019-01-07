# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:45:31 2019

@author: mcyitlr4
"""

import matplotlib.pyplot
import csv
import agent_particle

# 1.1 first we read the raster containing the map with the building where the weapon is placed.
f = open('bomb.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:				
    rowlist = []	
    for value in row:
        rowlist.append(value)
        				 
    environment.append(rowlist)  
f.close() 

# 1.2 This bit of code helps us to locate the building and returns its position as a meesage.
row_counter = 0
for row in environment:
    for value in row:
        if value != 0:
            x = row.index(value)
            y = row_counter
            print("Weapon located at coordinates","x =", x, "y =", y)
            
    row_counter += 1

# 2.1 This section is used to specify the parameters of the model.        
start_height = 76
num_of_particles = 5000

# 2.2 Here we create each of the bacteria particles (agents)
particles = []
for i in range(num_of_particles):
    particles.append(agent_particle.Particle(x, y, start_height))

# 2.3 Spreading the particles. The algorithm will move each particle, one by one, 
# until it reaches the ground. 
    
for j in range(len(particles)):
    while particles[j].height != 0:
        particles[j].direction()
        particles[j].fall()
        
# 3.1 Creating a list with the coordinates of every particle (no. particle, x, y)
particle_location = []
for p in range(num_of_particles):
    no_part = [] 
    no_part.append(p + 1)
    no_part.append(particles[p].x)
    no_part.append(particles[p].y)   
    particle_location.append(no_part) 

# 3.2 Creating a text file with the coordinates of evety particle
with open('bacteria.coordinates.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(["Particle","x","y"])
    for row in particle_location:
        csvwriter.writerow(row)
    
# 3.3 Making the density map.
#Each particle will add a value of 5 into the x,y coordinates where it falls. Thus, density will be higher in certain coordinates
# if particles fall in the same spot.
for z in range(len(particles)):
    environment[particles[z].y][particles[z].x] += 5 

matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(environment)            

# 3.4 Writing a text file for the density map.
with open('bacteria.density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)


   
