# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:35:11 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiGraph()

pos={0:(1,1),1:(0,0),2:(2,0),3:(2,2),4:(0,2)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5'}

nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,1),(0,2),(0,3),(0,4),(1,4),(2,3),(3,4)],width=1)
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(1,2)],width=1,edge_color='b')
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[0,1,2,3],node_color='r')
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[4],node_color='g')
nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.savefig("Ejemplo9.eps")
plt.show()