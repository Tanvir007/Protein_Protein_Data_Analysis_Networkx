import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Clustering_Coefficient_Output.txt")
clustering_coefficient_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        clustering_coefficient_list.append(float(s[1]))

fig, ax = plt.subplots()
ax.hist(clustering_coefficient_list, bins=35)
plt.xlabel('Clestering Coefficient Value')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Histogram')
plt.savefig("Clustering_Coefficient_Histogram.png")