import networkx as nx
import matplotlib.pyplot as plt
import random as r

color=[]
for j in range(0,15):
    color0='#'
    for k in range(0,6):
        color0=color0+r.choice('0123456789ABCDEF')
    color.append(color0)

print(color)

G=nx.Graph()
G=nx.florentine_families_graph()

print(G.nodes)

plt.figure(1,figsize=[6.4,4.8],dpi=100,facecolor='c',clear=True)

pos=nx.circular_layout(G)
#pos=nx.spring_layout(G)
#pos[0] = [-1,1]
#pos[33] = [1,1]

options = {
        'node_size':500,
        'node_color':color,
        'node_shape':'p',
        'edge_color':'k',
        'style':'-.',
        'width':0.5,
        'with_labels':True,
        'font_size':10,
        'font_color':'k',
        'font_weight':'bold'
        }

nx.draw_networkx(G,pos,**options)
plt.axis('off')




