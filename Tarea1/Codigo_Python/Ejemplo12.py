import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiDiGraph()

pos={0:(0,2),1:(1,2),2:(1,1),3:(2,1),4:(2,2)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5'}

nx.draw_networkx_nodes(G,pos,node_size=400,nodelist=[1],node_color='g')
nx.draw_networkx_nodes(G,pos,node_size=400,nodelist=[0,2,3,4],node_color='r')
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(0,1)],width=1,edge_color='b')
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=[(1,2),(1,3),(1,4)],width=1,edge_color='k')
nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.savefig("Ejemplo12.eps")
plt.show()