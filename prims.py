import sys # Library for INT_MAX

import random


from graph_reader import *
from graph_adt_list import *


def primMST(graph,edges):
    """If it's a digraph all vertices must be represented
    in both to_vert and from_vert positions in:
    [to_vert, from_vert, weight]
    """

    # choose a random index
    index = random.randint(0, graph.numberOfVertices-1)
    vertex = graph.vertices[index].id

    MST = []
    visited = []
    minEdge = [None,None,float('inf')] # [to_vert, from_vert, weight]

    minEdge_index = 0

    # number of edges in a minimum spanning tree is graph.numberOfVertices-1
    while len(MST) < graph.numberOfVertices-1:

        visited.append(vertex) # append the new vertex to the visited array

        for i, edge in enumerate(edges):
            if float(edge[2]) < float(minEdge[2]) and edge[1] not in visited and edge[0] in visited and edge[0] != edge[1]:
                minEdge = edge
                minEdge_index = i

        edges.pop(minEdge_index-1)

        MST.append(minEdge)

        vertex = minEdge[1]
        minEdge = [None,None,float('inf')]

    return MST


if __name__ == "__main__":

    filePath = "graph_data.txt"
    vertices, edges = readGraph(filePath)

    graph = LLGraph(vertices)
    graph.addEdges(edges)

    print(primMST(graph, edges))
