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
        information_list.append(s[1])

fig, ax = plt.subplots()
ax.hist(information_list, bins=35, orientation="horizontal")
plt.xlabel('Information Centrality Value')
plt.ylabel('Frequency')
plt.title('Information Centrality Histogram')
labels = [item.get_text() for item in ax.get_xticklabels()]
for tick in ax.get_xticklabels():
    tick.set_rotation(80)
plt.savefig("Information_Centrality_Histogram.png"