def find_path(graph, nodeA, nodeB):
    """Iterative DFS to find the path from nodeA to nodeB.
       Returns an array of index.ids starting from nodeA's id to nodeB's id.
       Returns error messages if nodeA or nodeB is not in the graph, if there
       is graph entered or if there is no path from nodeA to nodeB
    """

    def findVertexIndex(vertex_id):
        """vertex argument is a string that is
        the label or id of the vertex , NOT a linkedlist object
        returns the vertices index in the graph if present
        otherwise returns False"""
        for i, v in enumerate(graph.vertices):
            if v.id == vertex_id:
                return i
        return -1 # -1 is equivalent to false in this context


    #nodeA and nodeB are the same.
    if nodeA == nodeB:
        # check to see if the vertex has a path to itself
        for v in nodeA.getNeighbors():
            if v == nodeA.id:
                return [nodeA.id]
        return ["""The node_to and the node_from are the same node,
                but there is no self-pointing edges."""]

    # check to see if the nodes are in the graph.
    nodeA_index = findVertexIndex(nodeA.id)
    nodeB_index = findVertexIndex(nodeB.id)
    if not nodeA_index > -1:
        return nodeA.id + " not in graph."
    if not nodeB_index > -1:
        return nodeB.id + " not in graph."

    # intialize result array, stack, and checkedSet
    result = []
    stack = []
    checkedSet = set()

    # append the starting vertex to the stack
    # to be iterated through and add it to the set of checked vertices
    stack.append(nodeA)
    checkedSet.add(nodeA)

    # while items exist in the stack
    while stack:

        # pop the top item added to the element as is customary with DFS.
        current = stack.pop()
        # add the item's id to the result.
        result.append(current.id)

        # getNeighbors returns an array of vertex ids to look up...
        for vertex in current.getNeighbors():

            # look up the index into graph.vertices
            # array based on the vertex's id.
            index = findVertexIndex(vertex)

            # if the item has an index of 0 or greater.
            # check to see if the linkedlist object at
            # that index in the graph.vertices array is the target (nodeB).
            if index > -1:
                if graph.vertices[index] == nodeB:
                    result.append(graph.vertices[index].id)
                    return result
                elif graph.vertices[index] not in checkedSet:
                    stack.append(graph.vertices[index])
                    checkedSet.add(graph.vertices[index])
            else:
                return str(vertex) + " is not in the graph."
    else:
        return ["There is no path from "+ nodeA.id +" to " + nodeB.id +"."]

    return "Empty graph." # the program should not run this code.
