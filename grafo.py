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


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
 





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
caminhos = list(bfs_shortest_path(grafo, 'A', 'F'))


numero = 40
caminho_menor = []
for x in caminhos:
    if len(x) < numero:
        caminho_menor = x
        numero = len(x)

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
