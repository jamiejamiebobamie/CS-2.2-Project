"""What is the longest path that sewage can travel in the graph (diameter).
"""

from graph_reader import *
from graph_adt_list import *
from DFS import *

if __name__ == "__main__":
    vertices, edges = read_graph("graph_data.txt")
    new_graph = LLGraph(vertices)
    new_graph.addEdges(edges)

    current_max = float("-inf")
    max_path = []
    for NodeA in new_graph.vertices:
        for NodeB in new_graph.vertices:
            store_max = current_max
            test_path = find_path(new_graph, NodeA, NodeB)
            current_max = max(current_max,len(test_path))
            if store_max != current_max:
                max_path = test_path
    print("The max path that sewage can travel is " + str(current_max) + " and consists of the nodes " + ", ".join(max_path))
