import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(5))
G.add_edges_from([(0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(2,3),(3,4),])

pos = nx.nx_pydot.graphviz_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=range(4),node_color='b',alpha=1,node_size=600)
nx.draw_networkx_nodes(G,pos,nodelist=[4],node_color='g',alpha=1,node_size=600)
nx.draw_networkx_edges(G,pos,edgelist=[(0,1),(0,2),(0,3),(0,4),(1,4),(2,3),(3,4)],edge_color='k',alpha=1,width=3)
nx.draw_networkx_edges(G,pos,edgelist=[(1,2)],edge_color='r',alpha=1,width=3)
nx.draw_networkx_labels(G,pos,labels={0:'A',1:'B',2:'C',3:'D',4:'E'},font_size=12,font_color='k')

plt.axis('off')
plt.savefig("Ejemplo9.eps")
plt.show()