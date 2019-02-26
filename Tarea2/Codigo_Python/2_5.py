import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from(range(5))

pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G,pos,node_size=600,nodelist=range(5),node_color='b')
nx.draw_networkx_edges(G,pos,edgelist=[(0,1),(1,2),(2,3),(2,4),(4,0)],edge_color='k',alpha=1,width=3,arrowsize=20)
nx.draw_networkx_labels(G,pos,{0:'A',1:'B',2:'C',3:'D',4:'E'},font_size=8,font_color='w')
nx.draw_networkx_edge_labels(G,pos,edge_labels={(0,1):'Calle1',(1,2):'Calle2',(2,3):'Calle3',(2,4):'Calle4',(4,0):'Calle5'})

plt.axis('off')
plt.savefig("Ejemplo5.eps")
plt.show()
