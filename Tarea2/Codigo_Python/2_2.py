import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(6))
G.add_edges_from([(0,1),(1,2),(3,4),(1,5),(2,4),(4,5)])

pos = nx.bipartite_layout(G, {1,4})

labels={0:'Ana',1:'Juan',2:'Paty',3:'Dany',4:'Jose',5:'Zoe'}

nx.draw_networkx_nodes(G,pos,node_color='b',alpha=1,node_size=600)
nx.draw_networkx_edges(G,pos,edge_color='k',alpha=1,width=3)
nx.draw_networkx_labels(G,pos,labels,font_size=10,font_color='w')

plt.axis('off')
plt.savefig("Ejemplo2.eps")
plt.show()