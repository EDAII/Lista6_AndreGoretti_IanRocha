import networkx as nx 
import matplotlib.pyplot as plt
import string
import random
import time




listaJ = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'A', 'J']
listaA = ['B', 'C', 'D', 'E', 'G', 'H', 'I', 'J']


def caminhosDFS(grafo, inicio, final):
    pilha = [(inicio, [inicio])]
    while pilha:
        (vertice, aresta) = pilha.pop()
        for vizinho in grafo[vertice] - set(aresta):
            if vizinho == final:
                yield aresta + [vizinho]
            else:
                pilha.append((vizinho, aresta + [vizinho]))

def caminhoBFS(grafo, inicio, final):
    pilha = [(inicio, [inicio])]
    while pilha:
        (vertice, caminho) = pilha.pop(0)
        for next in grafo[vertice] - set(caminho):
            if next == final:
                yield caminho + [next]
            else:
                pilha.append((next, caminho + [next]))

def shortest_path(grafo, inicio, final):
    try:
        return next(caminhoBFS(grafo, inicio, final))
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
    print(node)
    for i in range(ale):
        if node == 'A':
            grafo[node].add(random.choice(listaA))
        else :   
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
