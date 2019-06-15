import networkx as nx
import matplotlib.pyplot as plt
import random as r


#G=nx.karate_club_graph()
#C=nx.eigenvector_centrality(G)
G=nx.barabasi_albert_graph(20,1)
PR=nx.pagerank(G,0.85)
#C=nx.eigenvector_centrality(G)
nx.draw_networkx(G)
print(PR)

