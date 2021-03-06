import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Information_Centrality_Output.txt")
information_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        information_list.append(float(s[1]))

fig, ax = plt.subplots()
ax.hist(information_list, bins=35)
plt.xlabel('Information Centrality Value')
plt.ylabel('Frequency')
plt.title('Information Centrality Histogram')
plt.savefig("Information_Centrality_Histogram.png")