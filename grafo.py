import networkx as nx 
import matplotlib.pyplot as plt
import string
import random



listaA = ['B', 'C', 'D', 'E', 'G', 'H', 'I', 'J']
listaB = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
listaC = ['B', 'A', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
listaD = ['B', 'C', 'A', 'E', 'F', 'G', 'H', 'I', 'J']
listaE = ['B', 'C', 'D', 'A', 'F', 'G', 'H', 'I', 'J']
listaF = ['B', 'C', 'D', 'E', 'A', 'G', 'H', 'I', 'J']
listaG = ['B', 'C', 'D', 'E', 'F', 'A', 'H', 'I', 'J']
listaH = ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'I', 'J']
listaI = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'A', 'J']
listaJ = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'A']


def caminhosDFS(grafo, start, goal):
    pilha = [(start, [start])]
    while pilha:
        (vertice, aresta) = pilha.pop()
        for vizinho in grafo[vertice] - set(aresta):
            if vizinho == goal:
                yield aresta + [vizinho]
            else:
                pilha.append((vizinho, aresta + [vizinho]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return []          


 




grafo = {'A': set([random.choice(listaA), random.choice(listaA)]),
         'B': set([random.choice(listaB), random.choice(listaB), random.choice(listaB)]),
         'C': set([random.choice(listaC), random.choice(listaC)]),
         'D': set([random.choice(listaD)]),
         'E': set([random.choice(listaE), random.choice(listaE)]),
         'F': set([random.choice(listaF)]),
         'G': set([random.choice(listaG), random.choice(listaG), random.choice(listaG)]),
         'H': set([random.choice(listaH)]),
         'I': set([random.choice(listaH), random.choice(listaH)]),
         'J': set([random.choice(listaI)]),
         }

# shortest_path(grafo, 'A', 'F')
temp = list(shortest_path(grafo, 'A', 'F'))
if temp is None:
    caminhos = []
else:   
    caminhos = temp
    # caminhos = list(shortest_path(grafo, 'A', 'F'))


# numero = 40
# caminho_menor = []
# for x in caminhos:
#     if len(x) < numero:
#         caminho_menor = x
#         numero = len(x)

print(caminhos)
# print(caminho_menor)

G = nx.DiGraph(grafo)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)


plt.show()
lst = []
n = int(input("Entre o numero de nós: "))
print("Digite os nós em ordem com letra maiuscula: ")
for i in range(0, n):
    no = str(input())

    lst.append(no)

print(lst)

if caminhos == lst:
    print("você acertou")

else:
    print("você errou")    
