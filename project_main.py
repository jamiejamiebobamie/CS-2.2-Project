from DFS import *
from graph_adt_list import *
from graph_reader import *
from prims import *

"""
Implement:

diameter:
"What is the longest path that sewage can travel in the graph (diameter)?"

minimum spanning tree:
"What is the shortest path that sewage can travel through the system that
connects the entire system (minimum spanning tree)?"

check all from_vert to_vert paths:
"Are there any locations where sewage does not travel to the "Sewage Treatment
Plant?"
"""

if __name__ == "__main__":
    # checks to see if a file path was included in the command line
    # if not use graph_data.txt
    if len(sys.argv)> 1:
        file_path = sys.argv[1]
    else:
        file_path = "graph_data.txt"

    # problem 1: What is the longest path
    # that sewage can travel in the graph (diameter)?
    print("\nproblem1. \n\nusing graph: " + file_path)

    vertices, edges = read_graph(file_path)
    new_graph = LLGraph(vertices)
    new_graph.addEdges(edges)

    current_max = float("-inf")
    max_path = []
    # Iterates through all of the paths
    # between each node and finds the longest
    # route that can be taken.
    for NodeA in new_graph.vertices:
        for NodeB in new_graph.vertices:
            store_max = current_max
            test_path = find_path(new_graph, NodeA, NodeB)
            current_max = max(current_max,len(test_path))
            if store_max != current_max:
                max_path = test_path
    print("The max path that sewage can travel is: " + str(current_max)+".")
    print("The path consists of the nodes:")
    for path in max_path:
        print(path)

    # problem 2: What is the minimum spanning tree of the graph?
    print("\nproblem2.\n")
    print("using data from: "+file_path)

    vertices, edges = read_graph(file_path)
    new_graph = LLGraph(vertices)
    new_graph.addEdges(edges)

    mst_edges = primMST(new_graph, edges)

    if len(mst_edges[0]) > 1:
        print("The edges of the minimum spanning tree for this graph are: ")
        for mst_edge in mst_edges:
            print(mst_edge)
    else:
        # print error message if the input graph is not correct
        print(mst_edges)

    if file_path != "graph_data1.txt":

        vertices, edges = read_graph("graph_data1.txt")
        new_graph = LLGraph(vertices)
        new_graph.addEdges(edges)

        # showing the algorithm works on a graph that is "robust"
        print("\nusing data from: graph_data1.txt")
        mst_edges = primMST(new_graph, edges)
        if len(mst_edges[0]) > 1:
            print("The edges of the minimum spanning tree for this graph are: ")
            for mst_edge in mst_edges:
                print(mst_edge)
        else:
            # print error message if the input graph is not correct
            print(mst_edges)

    # problem 3: Are there any paths not to the Sewage Treatmen Plant?
    print("\nproblem3. \n\nusing data from: "+file_path)

    vertices, edges = read_graph(file_path)
    new_graph = LLGraph(vertices)
    new_graph.addEdges(edges)

    # get a refeence to the LinkedList object
    # that is the sewage treatment plant
    sewage_plant = None
    for v in new_graph.vertices:
        if v.id == "Sewage Treatment Plant":
            sewage_plant = v

    # iterate through all of the nodes and determine
    # if they have a path to the sewage treament plant
    results = []
    for NodeA in new_graph.vertices:
            test_path = find_path(new_graph, NodeA, sewage_plant)
            if test_path[0][:16] == 'There is no path':
                results.append(NodeA.id)

    # print results
    if len(results):
        print("WARNING! WARNING!\nLOCATIONS:")
        print("\n".join(results))
        print("DO NOT HAVE A PATH TO THE SEWAGE TREATMENT PLANT!")
        print("WARNING! WARNING!")
    else:
        print("All locations lead to the sewage treatment plant! Hooray!")

    # showing the algorithm works on different types of graphs.
    if file_path != "graph_data1.txt":
        vertices, edges = read_graph("graph_data1.txt")
        new_graph = LLGraph(vertices)
        new_graph.addEdges(edges)
        print("\nusing data from: graph_data1.txt")
    else:
        vertices, edges = read_graph("graph_data.txt")
        new_graph = LLGraph(vertices)
        new_graph.addEdges(edges)
        print("\nusing data from: graph_data.txt")

    # get a refeence to the LinkedList object
    # that is the sewage treatment plant
    sewage_plant = None
    for v in new_graph.vertices:
        if v.id == "Sewage Treatment Plant":
            sewage_plant = v

    # iterate through all of the nodes and determine
    # if they have a path to the sewage treament plant
    results = []
    for NodeA in new_graph.vertices:
            test_path = find_path(new_graph, NodeA, sewage_plant)
            if test_path[0][:16] == 'There is no path':
                results.append(NodeA.id)

    # print results
    if len(results):
        print("WARNING! WARNING!\nLOCATIONS:")
        print("\n".join(results))
        print("DO NOT HAVE A PATH TO THE SEWAGE TREATMENT PLANT!")
        print("WARNING! WARNING!")
    else:
        print("All locations lead to the sewage treatment plant! Hooray!")
