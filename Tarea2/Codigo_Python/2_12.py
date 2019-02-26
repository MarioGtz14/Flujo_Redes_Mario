import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

G = nx.MultiDiGraph() 
G.add_nodes_from(range(5))

forceatlas2 = ForceAtlas2(
                        outboundAttractionDistribution=True,  
                        linLogMode=False,
                        adjustSizes=False,
                        edgeWeightInfluence=1.0,
                        
                        jitterTolerance=1.0,
                        barnesHutOptimize=True,
                        barnesHutTheta=1.2,
                        multiThreaded=False,

                        scalingRatio=2.0,
                        strongGravityMode=False,
                        gravity=1.0,

                        verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=200)




nx.draw_networkx_nodes(G, positions, nodelist=[0,2,3,4],node_size=100, with_labels=True, node_color="b")
nx.draw_networkx_nodes(G, positions, nodelist=[1],node_size=100, with_labels=True, node_color="g")
nx.draw_networkx_edges(G, positions,edgelist=[(0,1)], edge_color="k")
nx.draw_networkx_edges(G, positions,edgelist=[(1,2),(1,3),(1,4)], edge_color="k")
plt.axis('off')
plt.savefig("Ejemplo12.eps", format="EPS")
plt.show()