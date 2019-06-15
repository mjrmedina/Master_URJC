import networkx as nx
import os
os.system("clear")

Lista2 = [(1,2),(2,3),(1,3),(2,4),(2,5),(1,5),(4,5)]
Lista = []

for i in range (6,16):
    Lista.append((i,i+1))

NewList = Lista + Lista2
NewList.append((6,2))

G=nx.Graph(NewList)


nx.draw(G,with_labels=True)

print ("Number of nodes: " + str(G.number_of_nodes()))
print ("Number of connections: " + str(G.number_of_edges()))


