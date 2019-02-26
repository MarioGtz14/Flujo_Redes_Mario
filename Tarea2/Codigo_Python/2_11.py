import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiDiGraph()
G.add_nodes_from(range(6))

pos = nx.spring_layout(G,iterations=300)

nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,2),(1,3),(1,2),(2,3),(2,4),(3,1),(3,4),(3,5),(4,2),(4,5)],width=1,arrowsize=20)
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,1),(1,0)],width=1,edge_color='r',arrowsize=20)
nx.draw_networkx_nodes(G,pos,node_size=400,nodelist=[0,1,2,3,4,5],node_color='b')
nx.draw_networkx_labels(G,pos,{0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'},font_size=8,font_color='w')

plt.axis('off')
plt.savefig("Ejemplo11.eps")
plt.show()