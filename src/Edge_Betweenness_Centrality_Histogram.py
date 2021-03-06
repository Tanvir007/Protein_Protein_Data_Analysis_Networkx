import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Edge_Betweenness_Centrality_Output.txt")
edge_betweenness_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        edge_betweenness_list.append(float(s[2]))

fig, ax = plt.subplots()
ax.hist(edge_betweenness_list, bins=35)
plt.xlabel('Edge Betweenness Centrality Value')
plt.ylabel('Frequency')
plt.title('Edge Betweenness Centrality Histogram')
plt.savefig("Edge_Betweenness_Centrality_Histogram.png")