# This program takes data from a NetCDF file and creates a network.
# This program does not use any distance functions, the edges are calculated randomly.

import netCDF4 as nc
import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np

#creating a dataset from files
fn = "air.inter.eof2.nc"
data_set = nc.Dataset(fn)
print(data_set)

print("\nprinting dimensions\n")
print(data_set.dimensions.items())


air_pressure = data_set.variables['air']


print(air_pressure[:][0][0][0])
print(len(air_pressure[:]))
print(len(air_pressure[:][0]))
print(len(air_pressure[:][0][0]))
print(len(air_pressure[:][0][0][0]))

levels = list()
for i in data_set.variables['level']:
    levels.append(int(i.item(0)))
print(levels)

t_series = list()
for i in air_pressure:
    series = list()
    for j in i:
        series.append(j[0][0])
    t_series.append(series)

print(t_series)
time_data = 0
ndes = dict()
for z in range(2):
    g = nx.Graph()
    for i in range(len(air_pressure[:][0])):
        ndes[levels[i]] = air_pressure[:][0][i][z][0]

    for i in ndes.keys():
        g.add_node(i)
    for i in ndes.keys():
        for j in ndes.keys():
            if i>j:
                if abs(ndes[i]-ndes[j]) < 0.03:
                    g.add_edge(i,j)
    print(g)
    print(ndes)
    plt.subplot()
    nx.draw(g,with_labels=True, pos = nx.circular_layout(g))
  
    plt.show()
    plt.close('all')
    time.sleep(1)

# 144 longitudes, 73 latitudes, 17 levels, 12 times



'''
there is an array of 12 element, each element belongs to a time instance. 
each time instance consists of 17 elements, each belongs to a level 
each level consists of 73 elements, each belongs to a latitude 
each latitude consists of 144 elements, each belongs to a longitude 
'''