import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
col = 'k'

objects = ('Grafo 1', 'Grafo 2', 'Grafo 3', 'Grafo 4', 'Grafo 5')
y_pos = np.arange(len(objects))
performance = [0.0557,0.0555,0.0599,0.057,0.0568]
 
plt.bar(y_pos, performance,color=col, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Tiempo')
plt.xlabel('Grafos')
plt.title('Tiempo promedio para \n ALL_SHORTEST_PATHS')
plt.savefig("Algoritmo1.eps") 
plt.show()

objects = ('Grafo 1', 'Grafo 2', 'Grafo 3', 'Grafo 4', 'Grafo 5')
y_pos = np.arange(len(objects))
performance = [6.6604,6.2438,8.6077,8.1587,9.7803]
 
plt.bar(y_pos, performance,color=col, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Tiempo')
plt.xlabel('Grafos')
plt.title('Tiempo promedio para \n BETWEENNESS_CENTRALITY')
plt.savefig("Algoritmo2.eps") 
plt.show()

objects = ('Grafo 1', 'Grafo 2', 'Grafo 3', 'Grafo 4', 'Grafo 5')
y_pos = np.arange(len(objects))
performance = [1.8948,1.8768,1.9256,1.9256,2.1913]

plt.bar(y_pos, performance,color=col, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Tiempo')
plt.xlabel('Grafos')
plt.title('Tiempo promedio para \n COLORING.GREEDY_COLOR')
plt.savefig("Algoritmo3.eps")  
plt.show()

objects = ('Grafo 1', 'Grafo 2', 'Grafo 3', 'Grafo 4', 'Grafo 5')
y_pos = np.arange(len(objects))
performance = [21.0345,21.8238,21.2347,26.4565,28.7218]

plt.bar(y_pos, performance,color=col, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Tiempo')
plt.xlabel('Grafos')
plt.title('Tiempo promedio para \n MAXIMUM_FLOW')
plt.savefig("Algoritmo4.eps")  
plt.show()

objects = ('Grafo 1', 'Grafo 2', 'Grafo 3', 'Grafo 4', 'Grafo 5')
y_pos = np.arange(len(objects))
performance = [5.8499,5.6748,6.3996,6.0566,6.9847]


plt.bar(y_pos, performance,color=col, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Tiempo')
plt.xlabel('Grafos')
plt.title('Tiempo promedio para \n MINIMUM_SPANNING_TREE')
plt.savefig("Algoritmo5.eps") 
plt.show()