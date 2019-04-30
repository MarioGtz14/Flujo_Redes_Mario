import networkx as nx

G=nx.barabasi_albert_graph(9,3)

V1=[i for i in nx.degree_centrality(G).values()]
V2=[i for i in nx.closeness_centrality(G).values()]
V3=[i for i in nx.clustering(G).values()]
V4=[i for i in nx.load_centrality(G).values()]
V5=[i for i in nx.eccentricity(G).values()]
V6=[i for i in nx.pagerank(G).values()]

#values, keys, acceder a los elementos