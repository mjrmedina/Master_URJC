import networkx as nx

G=nx.Graph()

G.add_node('David')
G.add_node('Santiago')

G.add_edge('David','Santiago')
G.add_edge('David','Mario')
G.add_edge('David','Patricia')
G.add_edge('David','Patricia')
G.add_edge('David','Rafael')


nx.draw(G,with_labels=True)

print ("Number of nodes: " + str(G.number_of_nodes()))
print ("Number of connections: " + str(G.number_of_edges()))