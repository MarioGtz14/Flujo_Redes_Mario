# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:36:34 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.DiGraph()

pos={0:(0,1),1:(1,0),2:(2,0),3:(2,1),4:(1,1)}
labels={0:'$1$',1:'2',2:'3',3:'4',4:'5'}
Conexion=[(0,1),(1,0),(1,2),(1,4),(2,3),(3,4),(4,3),(4,0)]

nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[0,1,2,4],node_color='r')
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[3],node_color='g')
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=Conexion,width=1)
nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.savefig("Ejemplo6.eps")
plt.show()