import networkx as nx 
import matplotlib.pyplot as plt
import string
import random
import time




listaJ = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'A', 'J']


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


ligacoes = int(input("Selecione Ate quantos vertices terá em cada nó: "))




grafo = {'A': set([]),
         'B': set([]),
         'C': set([]),
         'D': set([]),
         'E': set([]),
         'F': set([]),
         'G': set([]),
         'H': set([]),
         'I': set([]),
         'J': set([]),
         }

for node in grafo:
    ale = random.randint(1, ligacoes)
    for i in range(ale):
        grafo[node].add(random.choice(listaJ))        


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

inicio = time.time()
plt.show()
fim = time.time()
lst = []
n = int(input("Entre o numero de nós: "))
print("Digite os nós em ordem com letra maiuscula: ")
for i in range(0, n):
    no = str(input())

    lst.append(no)

print(lst)

if caminhos == lst:
    print("você acertou")
    print("Seu tempo: ",)
    print(fim - inicio)

else:
    print("você errou")    
