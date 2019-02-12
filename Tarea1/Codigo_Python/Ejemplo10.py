# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:10:38 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiDiGraph()

pos={0:(0,1),1:(1,0),2:(1,2),3:(2,0),4:(2,2)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5'}

nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,1),(1,3),(1,2),(2,3),(2,4),(3,4)],width=1)
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,2)],width=1,edge_color='b')
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[0,1,2,3,4],node_color='r')
nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.savefig("Ejemplo10.eps")
plt.show()