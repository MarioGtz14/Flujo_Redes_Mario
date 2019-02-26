import networkx as nx
import matplotlib.pyplot as plt


G = nx.MultiDiGraph()
G.add_nodes_from(range(5))

pos = nx.kamada_kawai_layout(G)

nx.draw_networkx_nodes(G,pos,node_size=400,nodelist=range(5),node_color='b')
nx.draw_networkx_edges(G,pos,edgelist=[(1,2),(1,3),(3,4)],edge_color='r',alpha=1,width=3)
nx.draw_networkx_edges(G,pos,edgelist=[(0,1),(0,2),(2,3),(2,4)],edge_color='k',alpha=1,width=3)
nx.draw_networkx_labels(G,pos,labels={0:'A',1:'B',2:'C',3:'D',4:'E'},font_size=12,font_color='w')

plt.axis('off')
plot_margin = 0.05

x0, x1, y0, y1 = plt.axis()
plt.axis((x0 - plot_margin,
          x1 + plot_margin,
          y0 - plot_margin,
          y1 + plot_margin))
plt.savefig("Ejemplo10.eps")
plt.show()