import networkx as nx
import matplotlib.pyplot as plt

G=nx.MultiDiGraph()

G.add_nodes_from(range(5))
pos = nx.fruchterman_reingold_layout(G)

nx.draw_networkx_nodes(G,pos,node_size=500,nodelist=[0],node_color='g')
nx.draw_networkx_nodes(G,pos,node_size=500,nodelist=[1,2,3,4],node_color='b')
nx.draw_networkx_edges(G,pos,edgelist=[(1,2),(2,1),(2,3),(3,2),(4,0)],edge_color='k',alpha=1,width=3,arrowsize=20)
nx.draw_networkx_edges(G,pos,edgelist=[(3,4),(0,1),(1,0)],edge_color='r',alpha=1,width=3)

nx.draw_networkx_labels(G,pos,{0:'A',1:'B',2:'C',3:'D',4:'E'},font_size=8,font_color='w')

plt.axis('off')

plot_margin = 0.05

x0, x1, y0, y1 = plt.axis()
plt.axis((x0 - plot_margin,
          x1 + plot_margin,
          y0 - plot_margin,
          y1 + plot_margin))

plt.savefig("Ejemplo8.eps")
plt.tight_layout()
plt.show()