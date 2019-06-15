import networkx as nx
import os
os.system("clear")

Lista2 = [(1,2),(2,3),(1,3),(2,4),(2,5),(1,5),(4,5)]
Lista = []

G=nx.Graph()
G.add_nodes_from(range(0,100))

L = list(G.nodes)

for i in L :
    if i%2 != 0:
        G.remove_node(i)

L=G.nodes()

for i in range(0,11) :
    for k in range (i+1,11) :
        N1=i*10
        N2=k*10
        G.add_edge(N1,N2)
    for j in range(1,10) :
        N3=N1+j
        if N3 in G.nodes():
            G.add_edge(N1,N3)

for j in G[50]:
    G.add_edge(j,61)
    

nx.draw(G,with_labels=True)

print ("Number of nodes: " + str(G.number_of_nodes()))
print ("Number of connections: " + str(G.number_of_edges()))

print("Nodos: " + str(G.nodes))
print("Aristas: " + str(G.edges))
print("Vecinos: " + str(G.neighbors(1)))

