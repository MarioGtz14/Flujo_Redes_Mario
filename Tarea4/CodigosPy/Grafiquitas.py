# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:44:11 2019

@author: maari
"""

import networkx as nx
import matplotlib.pyplot as plt


#Grafo con el generador 1
G = nx.circular_ladder_graph(8)

nx.draw_networkx(G,
                 node_color='b',node_size=200,
                 edge_color='k',arrowsize=10,width=1,
                 font_size=0)


plt.axis('off')
plt.savefig("G1.eps")
plt.show()


#Grafo con el generador 2
H = nx.grid_graph(dim=[4,4])

nx.draw_networkx(H,
                 node_color='b',node_size=200,
                 edge_color='k',arrowsize=10,width=1,
                 font_size=0)
                 
plt.axis('off')
plt.savefig("G2.eps")
plt.show()


#Grafo con el generador 3

I = nx.complete_graph(5)

nx.draw_networkx(I,
                 node_color='b',node_size=200,
                 edge_color='k',arrowsize=10,width=1,
                 font_size=0)
                 
plt.axis('off')
plt.savefig("G3.eps")
plt.show()

#nx.draw_networkx_labels()
#nx.draw_networkx_edges()
#nx.draw_networkx_nodes()