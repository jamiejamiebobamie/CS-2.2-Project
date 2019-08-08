"""Are there any locations where sewage does not travel to the "Sewage Treatment Plant?"
"""

from graph_reader import *
from graph_adt_list import *
from DFS import *

if __name__ == "__main__":
    vertices, edges = readGraph("graph_data.txt")
    new_graph = LLGraph(vertices)
    new_graph.addEdges(edges)
    sewage_plant = None
    for v in new_graph.vertices:
        if v.id == "Sewage Treatment Plant":
            sewage_plant = v

    results = []
    for NodeA in new_graph.vertices:
            test_path = find_path(new_graph, NodeA, sewage_plant)
            if test_path[0][:16] == 'There is no path':
                results.append(NodeA.id)
    if len(results):
        print("WARNING! WARNING!\nLOCATIONS:\n" + "\n".join(results) + "\nDO NOT HAVE A PATH TO THE SEWAGE TREATMENT PLANT!\nWARNING! WARNING!")
    else:
        print("All locations lead to the sewage treatment plant! Hooray!")

    vertices, edges = readGraph("graph_data1.txt")
    new_graph = LLGraph(vertices)
    new_graph.addEdges(edges)
    sewage_plant = None
    for v in new_graph.vertices:
        if v.id == "Sewage Treatment Plant":
            sewage_plant = v

    results = []
    for NodeA in new_graph.vertices:
            test_path = find_path(new_graph, NodeA, sewage_plant)
            if test_path[0][:16] == 'There is no path':
                results.append(NodeA.id)
    if len(results):
        print("WARNING! WARNING!\nLOCATIONS:\n" + "\n".join(results) + "\nDO NOT HAVE A PATH TO THE SEWAGE TREATMENT PLANT!\nWARNING! WARNING!")
    else:
        print("All locations lead to the sewage treatment plant! Hooray!")
