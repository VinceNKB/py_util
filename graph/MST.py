#!/usr/bin/env python3

from graph import graph_matrix
from Union import UF


# Kruskal   time: O(ElgV)
def Kruskal(graph):
    A = set()
    uf = UF(graph.nodenum)
    sorted_edge = sorted([(z, (x, y)) for x,y,z in graph.getEdge()])

    for val, (u, v) in sorted_edge:
        if uf.find(u) != uf.find(v):
            A.add((u, v))
            uf.union(u, v)
    return A

'''
graph = graph_matrix.Graph_matrix(maps=[[float('inf')] * 5 for _ in range(5)] , directed=False)
graph.addEdge(0,1,1)
graph.addEdge(1,2,2)
graph.addEdge(2,3,3)
graph.addEdge(3,4,4)
graph.addEdge(0,4,100)
graph.addEdge(2,4,100)
print(Kruskal(graph))
'''

def Prim(graph, start = 0):
    vector_info = {}
    for i in range(graph.nodenum):
        vector_info[i] = [float('inf'), None]

    vector_info[start][0] = 0

    Q = vector_info
    A = []

    while Q:
        u = min(Q.items(), key=lambda x:x[1][0])
        A.append((u[0], u[1][1]))
        Q.pop(u[0])
        u_adj = graph.getOutNode(u[0])
        for v in u_adj:
            if v in Q and graph.getWeight(u[0], v) < Q[v][0]:
                Q[v][1] = u[0]
                Q[v][0] = graph.getWeight(u[0], v)
    return A

'''
graph = graph_matrix.Graph_matrix(maps=[[float('inf')] * 5 for _ in range(5)] , directed=False)
graph.addEdge(0,1,1)
graph.addEdge(1,2,2)
graph.addEdge(2,3,3)
graph.addEdge(3,4,4)
graph.addEdge(0,4,100)
graph.addEdge(2,4,100)
print(Prim(graph, 2))
'''




