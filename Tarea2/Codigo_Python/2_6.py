import networkx as nx
import matplotlib.pyplot as plt


G = nx.MultiDiGraph()
G.add_nodes_from(range(5))
G.add_edges_from([(0,1),(1,0),(1,2),(1,4),(2,3),(3,4),(4,0),(4,3)])

pos = nx.nx_pydot.pydot_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=[0,1,2,4],node_color='b',alpha=1,node_size=600)
nx.draw_networkx_nodes(G,pos,nodelist=[3],node_color='g',alpha=1,node_size=600)
nx.draw_networkx_edges(G,pos,edgelist=[(0,1),(1,0),(1,2),(1,4),(2,3),(3,4),(4,0),(4,3)],edge_color='k',alpha=1,width=3,arrowsize=30)
nx.draw_networkx_labels(G,pos,labels={0:'A',1:'B',2:'C',3:'D',4:'E'},font_size=12,font_color='k')

plt.axis('off')
plt.savefig("Ejemplo6.eps")
plt.show()