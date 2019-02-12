# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:17:59 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiGraph()

pos={0:(0,0),1:(2,0),2:(2,2),3:(0,2),4:(0,1)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5'}

nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,1),(1,2),(2,3)],width=1)
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,4),(3,4)],width=1,edge_color='b')
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=range(5),node_color='r')
nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.savefig("Ejemplo8.eps")
plt.show()