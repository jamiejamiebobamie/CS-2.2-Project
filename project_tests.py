"""For this project I mainly used two functions:
    the find_path() function
    and
    the primMST() function

    I also used the read_graph() function.

    Below are the tests for said methods.
"""

from graph_reader import *
from graph_adt_list import *
from DFS import *
from prims import *

filepath = "graph_data.txt"
filepath2 = "graph_data1.txt"
vertices,edges = read_graph(filepath)
vertices2,edges2 = read_graph(filepath2)

# testing readGraph method
assert vertices == ['Location A', 'Location B', 'Location C', 'Location D',
                    'Location E', 'Location F', 'Location G', 'Location H',
                    'Sewage Treatment Plant']

assert vertices2 == ['Location A', 'Location B', 'Location C', 'Location D',
                    'Location E', 'Location F', 'Location G', 'Location H',
                    'Sewage Treatment Plant']
assert edges == [('Location A', 'Location A', '4'),
                ('Location B', 'Location A', '4'),
                ('Location A', 'Location D', '4'),
                ('Location B', 'Location C', '4'),
                ('Location D', 'Location B', '1'),
                ('Location E', 'Location F', '4'),
                ('Location F', 'Location F', '4'),
                ('Location C', 'Location D', '5'),
                ('Location A', 'Location B', '2'),
                ('Location A', 'Location B', '52'),
                ('Location F', 'Location H', '10'),
                ('Location G', 'Location H', '4'),
                ('Location F', 'Sewage Treatment Plant', '90'),
                ('Location C', 'Sewage Treatment Plant', '35'),
                ('Location A', 'Sewage Treatment Plant', '35')]
assert edges2 == [('Location A', 'Location A', '4'),
                    ('Location A', 'Location B', '2'),
                    ('Location A', 'Location D', '52'),
                    ('Location A', 'Location C', '4'),
                    ('Location B', 'Location B', '4'),
                    ('Location B', 'Location C', '4'),
                    ('Location B', 'Location D', '4'),
                    ('Location B', 'Location E', '4'),
                    ('Location C', 'Location C', '5'),
                    ('Location C', 'Location D', '5'),
                    ('Location C', 'Location E', '5'),
                    ('Location C', 'Location F', '5'),
                    ('Location D', 'Location D', '1'),
                    ('Location D', 'Location E', '1'),
                    ('Location D', 'Location F', '1'),
                    ('Location D', 'Location G', '1'),
                    ('Location E', 'Location E', '4'),
                    ('Location E', 'Location G', '4'),
                    ('Location E', 'Location H', '4'),
                    ('Location E', 'Sewage Treatment Plant', '4'),
                    ('Location F', 'Location F', '4'),
                    ('Location F', 'Location G', '4'),
                    ('Location F', 'Location H', '4'),
                    ('Location F', 'Sewage Treatment Plant', '4'),
                    ('Location F', 'Location A', '10'),
                    ('Location G', 'Location G', '4'),
                    ('Location G', 'Location H', '4'),
                    ('Location G', 'Sewage Treatment Plant', '4'),
                    ('Location G', 'Location A', '4'),
                    ('Location H', 'Location H', '4'),
                    ('Location H', 'Sewage Treatment Plant', '10'),
                    ('Location H', 'Location A', '4'),
                    ('Location H', 'Location B', '10'),
                    ('Sewage Treatment Plant', 'Location A', '35'),
                    ('Sewage Treatment Plant', 'Location B', '35'),
                    ('Sewage Treatment Plant', 'Location C', '35'),
                    ('Sewage Treatment Plant', 'Location D', '35')]

new_graph = LLGraph(vertices)
new_graph.addEdges(edges)

newer_graph = LLGraph(vertices2)
newer_graph.addEdges(edges2)

# testing the getEdges method to ensure edges have been added correctly.
# looking at the first vertex in the graph.vertices array
assert new_graph.getEdges(1) == [('Location A', 'Location A', '4'),
                                ('Location A', 'Location D', '4'),
                                ('Location A', 'Location B', '2'),
                                ('Location A', 'Location B', '52'),
                                ('Location A', 'Sewage Treatment Plant', '35')]

assert newer_graph.getEdges(1) == [('Location A', 'Location A', '4'),
                                    ('Location A', 'Location B', '2'),
                                    ('Location A', 'Location D', '52'),
                                    ('Location A', 'Location C', '4')]

# testing basic find_path functionality
# testing paths to the same vertex with a path:
assert (find_path(new_graph, new_graph.vertices[0], new_graph.vertices[0])
        == ['Location A'])

# testing paths to the same vertex that DOES NOT have a path:
assert (find_path(new_graph, new_graph.vertices[1], new_graph.vertices[1])
== ["""The node_to and the node_from are the same node,
                but there is no self-pointing edges."""])

# testing the path from one vertex to another that are ADJACENT:
assert find_path(newer_graph, newer_graph.vertices[0],
newer_graph.vertices[1]) == ['Location A', 'Location B']
# testing the findpath method on vertices that are NOT ADJACENT:
assert (find_path(new_graph, new_graph.vertices[0],
new_graph.vertices[2])
== ['Location A', 'Sewage Treatment Plant', 'Location B', 'Location C'])
# testing the findpath method on vertices that DO NOT have a path to one another:
assert find_path(new_graph, new_graph.vertices[4],
new_graph.vertices[2]) == ['There is no path from Location E to Location C.']

# testing prim's on a graph with
# all vertices NOT present in both the to_vert and the from_vert positions
assert primMST(new_graph, edges) == """For this algorithm to work,
                each of your vertices need to be present at
                least once in both the to_vert and from_vert edges."""
