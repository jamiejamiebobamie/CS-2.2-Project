"""What is the shortest path that sewage can travel through the system
that connects the entire system (minimum spanning tree)?
"""

from graph_reader import *
from graph_adt_list import *
from prims import *



if __name__ == "__main__":
    vertices, edges = read_graph("graph_data1.txt")
    new_graph = LLGraph(vertices)
    new_graph.addEdges(edges)

    print(primMST(new_graph, edges))
