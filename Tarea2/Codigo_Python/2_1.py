import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

G = nx.Graph()

Conexion=[('A', 'B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G')]
G.add_edges_from(Conexion)

labels={'A':'C','B':'F1','C':'F2','D':'SF1','E':'SF2','F':'SF4','G':'SF3'}

pos = nx.spectral_layout(G)

nx.draw_networkx_nodes(G,pos,node_color='b',alpha=1,node_size=500)
nx.draw_networkx_edges(G,pos,edge_color='k',alpha=1,width=3)
nx.draw_networkx_labels(G,pos,labels,font_size=10,font_color='w')

plt.axis('off')
plt.savefig("Ejemplo1.eps")
plt.show()