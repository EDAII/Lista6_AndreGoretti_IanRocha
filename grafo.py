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


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))




graph = {'A': set([random.choice(listaA), random.choice(listaA)]),
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

print(graph)
caminhos = list(dfs_paths(graph, 'A', 'F'))
print(caminhos)

#print(path)
numero = 40
caminho_menor = []
for x in caminhos:
    if len(x) < numero:
        caminho_menor = x
        numero = len(x)

print(caminho_menor)
G = nx.DiGraph(graph)
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

if caminho_menor == lst:
    print("você acertou")

else:
    print("você errou")    
