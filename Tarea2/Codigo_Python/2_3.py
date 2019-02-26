import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

Conexion=[('A', 'B'),('A','C'),('B','D'),('B','E')]
G.add_edges_from(Conexion)

labels={'A':'Esq\n #1','B':'Retorno','C':'Esq\n #2','D':'Esq\n #3','E':'Esq\n #4'}

pos = nx.random_layout(G)

nx.draw_networkx_nodes(G,pos,node_size=1000,nodelist=['B'],node_color='g')
nx.draw_networkx_nodes(G,pos,node_size=1000,nodelist=['A','C','D','E'],node_color='b')
nx.draw_networkx_edges(G,pos,edge_color='k',alpha=1,width=3)
nx.draw_networkx_labels(G,pos,labels,font_size=8,font_color='w')
nx.draw_networkx_edge_labels(G,pos,edge_labels={('A', 'B'):'Calle1',('B', 'D'):'Calle2',('B', 'E'):'Calle3',('A', 'C'):'Calle4'})

plt.axis('off')
plot_margin = 0.05

x0, x1, y0, y1 = plt.axis()
plt.axis((x0 - plot_margin,
          x1 + plot_margin,
          y0 - plot_margin,
          y1 + plot_margin))
plt.savefig("Ejemplo3.eps")
plt.show()


