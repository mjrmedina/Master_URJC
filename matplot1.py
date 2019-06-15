import networkx as nx
import matplotlib.pyplot as plt

G=nx.karate_club_graph()
N=nx.number_of_nodes(G)
Grnv=list(G.degree)
Gr=[]
for j in range(0,N):
    Gr.append(Grnv[j][1])

plt.figure(1,figsize=[6.4,4.8],dpi=100,facecolor='c',clear=True)

options = {
        'color':'r',
        'marker':'o',
        'markersize':6,
        'linestyle':'-',
        'linewidth':1.0,
        'label':'Grado',
        }



plt.axis([-1,N,0,18])
plt.xticks(range(0,N),fontsize=5)
plt.yticks(range(0,18),fontsize=12,color='b')
plt.xlabel('Nodos',fontsize=12,weight='bold')


plt.plot(range(0,N),Gr,**options)
plt.legend()

options_leyend = {
        'fontsize':20,
        'fontweoght':'bold',
        'color':'darkblue'
        }
plt.title('Grado de la red de Karate',**options_leyend)
plt.legend(loc=0,ncol=1,markerscale=0.3,fontsize=15,shadow=True)


###########################
plt.figure(2,figsize=[6.4,4.8],dpi=100,facecolor='orange',clear=True)
options = {
        'node_size':300,
        'node_color':'b',
        'node_shape':'p',
        'edge_color':'y',
        'style':'-.',
        'width':0.5,
        'with_labels':True,
        'font_size':10,
        'font_color':'y',
        'font_weight':'bold'
        }
nx.draw_networkx(G,**options)
############################

plt.figure(3,figsize=[6.4,4.8],dpi=100,facecolor='mintcream',clear=True)

nx.draw_networkx(G,nodelist=[32,33],edgelist=[(32,33)],**options)
plt.axis('off')
options = {
        'fontsize':20,
        'fontweight':'bold',
        'color':'darkblue'
        }

plt.title('Enlace del 32 y el 33',**options)

############################
plt.figure(4,figsize=[6.4,4.8],dpi=100,facecolor='w',clear=True)

LT=[]
LC=[]
for j in range(0,N):
    LT.append(Gr[j]*100)
    if j==0:
        LC.append('r')
    elif j==33:
        LC.append('b')
    elif j in G[0]:
        LC.append('lightsalmon')
    elif j in G[33]:
        LC.append('skyblue')
    else:
        LC.append('k')
   # if j in G[0] and j in G[33]:
   #     LC[j]='y'

options = {
        'node_size':LT,
        'node_color':LC,
        'node_shape':'p',
        'edge_color':'y',
        'style':'-.',
        'width':0.5,
        'with_labels':False
        }

nx.draw_networkx(G,**options)
plt.axis('off')
############################
plt.figure(4,figsize=[6.4,4.8],dpi=100,facecolor='w',clear=True)

LT=[]
LC=[]
for j in range(0,N):
    LT.append(Gr[j]*100)
    if j==0:
        LC.append('r')
    elif j==33:
        LC.append('b')
    elif j in G[0]:
        LC.append('lightsalmon')
    elif j in G[33]:
        LC.append('skyblue')
    else:
        LC.append('k')
   # if j in G[0] and j in G[33]:
   #     LC[j]='y'

options = {
        'node_size':LT,
        'node_color':LC,
        'node_shape':'p',
        'edge_color':'y',
        'style':'-.',
        'width':0.5,
        'with_labels':False
        }
#pos=nx.circular_layout(G)
pos=nx.spring_layout(G)
pos[0] = [-1,1]
pos[33] = [1,1]

nx.draw_networkx(G,pos,**options)
plt.axis('off')

