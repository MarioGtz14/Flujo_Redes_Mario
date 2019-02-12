# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:20:20 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
pos={0:(0,1),1:(1,0),2:(1,1),3:(2,1),4:(1,2)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5'}
Conexion=[(0,2),(1,2),(3,2),(4,2)]

nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[2],node_color='g')
nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=[0,1,3,4],node_color='r')
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=Conexion,width=1)
nx.draw_networkx_labels(G,pos,labels,font_size=12)
plt.axis('off')
plt.savefig("Ejemplo3.eps")
plt.show()