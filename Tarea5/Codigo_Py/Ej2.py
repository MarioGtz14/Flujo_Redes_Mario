import matplotlib.pyplot as plt
import networkx as nx

#Generador
G=nx.barabasi_albert_graph(8,2)
#Algoritmo de acomodo
nx.draw_networkx(G,nx.kamada_kawai_layout(G),with_labels=False)
#Implementacion para el problema de maximo flujo
Max_Flujo, Flujo_Arcos = nx.maximum_flow(G, 0,3)