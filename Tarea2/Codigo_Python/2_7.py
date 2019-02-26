import networkx as nx
import matplotlib.pyplot as plt


G = nx.MultiGraph()
G.add_nodes_from(range(5))

pos = nx.shell_layout(G)

nx.draw_networkx_nodes(G,pos,node_size=700,nodelist=[0],node_color='y',node_shape='s')
nx.draw_networkx_nodes(G,pos,node_size=700,nodelist=[1,2,3,4],node_color='b')
nx.draw_networkx_edges(G,pos,edgelist=[(0,1),(1,3)],edge_color='k',alpha=1,width=3)
nx.draw_networkx_edges(G,pos,edgelist=[(1,2),(3,4)],edge_color='r',alpha=1,width=3)
nx.draw_networkx_labels(G,pos,{0:'Dep',1:'A',2:'Suc \n#1',3:'B',4:'Suc \n#2'},font_size=8,font_color='w')

plt.axis('off')

plot_margin = 0.05

x0, x1, y0, y1 = plt.axis()
plt.axis((x0 - plot_margin,
          x1 + plot_margin,
          y0 - plot_margin,
          y1 + plot_margin))

plt.savefig("Ejemplo7.eps")
plt.tight_layout()
plt.show()
