# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:25:58 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiGraph()

pos={0:(1,.4),1:(2,.4),2:(2,0),3:(2,.8),4:(3.5,.8)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5'}

nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(1,2),(3,4)],width=1,edge_color='b')
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,1),(1,3)],width=1)
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=range(5),node_color='r')
nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.savefig("Ejemplo7.eps")
plt.show()