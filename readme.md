This repo contains the final project for my CS-2.2-Graphs class at Make School.

Given graph:
Given an input file of sewage origin points and sewage end points (vertices) and pipes (directed weighted edges):

D
("Location A", "Location B", "Location C", "Location D", "Location E", "Location F", "Location G", "Location H", "Sewage Treatment Plant")
("Location A", "Location A", 4)
("Location D", "Location B", 1)
("Location C", "Location D", 5)
("Location A", "Location B", 2)
("Location C", "Sewage Treatment Plant", 35)
("Location A", "Location B", 52)
("Location F", "Location H", 10)
("Location F", "Sewage Treatment Plant", 90)

...model the flow sewage.

Possible algorithms and problems to solve:
What is the longest path that sewage can travel in the graph (diameter).
What is the shortest path that sewage can travel through the system that connects the entire system (minimum spanning tree)?
Are there any locations where sewage does not travel to the "Sewage Treatment Plant?"

NOTE: The sewage treatment plant is the last vertex in the list of vertices on the second line of the graph file.
