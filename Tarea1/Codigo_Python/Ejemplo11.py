# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:28:21 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiDiGraph()

pos={0:(0,1),1:(1,0),2:(1,2),3:(2,0),4:(2,2),5:(3,1)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5',5:'6'}

nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,2),(1,0),(1,3),(1,2),(2,3),(2,4),(3,1),(3,4),(3,5),(4,2),(4,5)],width=1)
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,1)],width=1,edge_color='b')
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[0,1,2,3,4,5],node_color='r')

nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.savefig("Ejemplo11.eps")
plt.show()