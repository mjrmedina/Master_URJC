import networkx as nx
import random as r

def grado_medio(lista):
    L = len(Grado)
    
    sum = 0
    
    for k in Grado:
        sum = sum + k[1]
        
    return(sum/L)

p=1
N=1000
k=4

G=nx.Graph()
#G.add_nodes_from(range(0,N))

#for k in range(0,N):
#    for i in range(k+1,N):
#        if r.random() <= p:
#            G.add_edge(k,i)

#nx.draw(G,node_size=50)

#G=nx.erdos_renyi_graph(N,p)
#nx.draw(G,node_size=50)


G=nx.barabasi_albert_graph(N,p)
nx.draw(G,node_size=10)

Grado = list(G.degree)
print("Grado medio: "+ str(grado_medio(Grado)))

#G=nx.watts_strogatz_graph(N,k,p)
#nx.draw(G,node_size=50)

