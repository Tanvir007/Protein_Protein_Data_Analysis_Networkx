import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Load_Centrality_Output.txt")
load_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        load_list.append(float(s[1]))

fig, ax = plt.subplots()
ax.hist(load_list, bins=35)
plt.xlabel('Load Centrality Value')
plt.ylabel('Frequency')
plt.title('Load Centrality Histogram')
plt.savefig("Load_Centrality_Histogram.png")