import networkx as nx
import random as r

def grado_medio(lista):
    L = len(Grado)
    
    sum = 0
    
    for k in Grado:
        sum = sum + k[1]
        
    return(sum/L)



G=nx.Graph()
Garate=nx.karate_club_graph()
G=nx.florentine_families_graph()
nx.draw(G,node_size=10)

print("Numero de nodos: " + str(G.number_of_nodes()))
print("Numero de aristas: " + str(G.size()))
Grado = list(G.degree)
#print("Grado de Medici: " + str(nx.betweenness_centrality(G)['Medici']))

print("Grado medio: "+ str(grado_medio(Grado)))
#print("Promedio de camino mas corto entre 0 y 1: " + str(nx.shortest_path_length(G,0,1)))
print("Promedio de camino mas corto entre Medici y Pazzi: " + str(nx.shortest_path_length(G,'Medici','Pazzi')))
print("Promedio de camino mas corto: " + str(nx.average_shortest_path_length(G)))
print("Diametro: " + str(nx.diameter(G)))
#print("Centralidad: " + str(nx.betweenness_centrality(G)[0]))
print("Centralidad Medici: " + str(nx.betweenness_centrality(G)['Medici']))

Graux=[]
for a in Garate:
    x=a[1]
    Graux.append(x)
nx.draw(Garate, node_size=Graux)

