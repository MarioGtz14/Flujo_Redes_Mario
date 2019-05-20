import matplotlib.pyplot as plt
import networkx as nx

#Parametros
#-----------------------------------------------
Equipos = [i+1 for i in range(4)]
equipo = 2
cap=[[6,1,1],[0,5,6]]

P=[i for i in Equipos if i!=equipo]
Q=[(i,j) for i in P for j in P if i<j]
#-----------------------------------------------

G = nx.DiGraph()
O=0
G.add_nodes_from([O])
G.add_nodes_from(Q)
for i in range(len(Q)):
   G.add_edge(O,Q[i],capacity=cap[0][i])
G.add_nodes_from(P)
for i in range(len(Q)):
   for j in range(2):
      G.add_edge(Q[i],Q[i][j],capacity=cap[0][i])    
T=len(P)+len(Q)+1
G.add_nodes_from([T])
for j in range(len(P)):
   G.add_edge(P[j],T,capacity=cap[1][j])
   
pos = {O:(0,0) , Q[0]:(2,2), Q[1]:(2,0),
       Q[2]:(2,-2), P[0]:(4,2), P[1]:(4,0),
       P[2]:(4,-2),T:(6,0)}

nx.draw_networkx_nodes(G,pos,node_shape='o',node_size=400)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edge_labels(G,pos,label_pos=0.7,font_size=8,edge_labels=nx.get_edge_attributes(G,'capacity'),font_color='b')

plt.axis('off')
plt.savefig('Instancia.eps')
plt.show()

solucion = nx.maximum_flow(G,O,T)

arcos = solucion[1].copy()

Grosor_capacidad=[]
Grosor_flujo=[]


#Capacidad de cada arco
Capacidad=nx.get_edge_attributes(G,'capacity')
#print(Capacidad,'\n\n')
#Capacidad usada de cada arco
#print(arcos)

dic_solcap={}
for (i,j) in nx.get_edge_attributes(G,'capacity').keys():
   a = Capacidad[(i,j)] #Lo que puede pasar
   b = arcos[i][j]      #Lo que pasa
   dic_solcap[(i,j)]=(a,b)
   
#print(dic_solcap)

nx.draw_networkx_nodes(G,pos,node_shape='o',node_size=400)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edge_labels(G,pos,label_pos=0.7,font_size=8,edge_labels=dic_solcap,font_color='b')

plt.axis('off')
plt.savefig('Solucion.eps')
plt.show()
