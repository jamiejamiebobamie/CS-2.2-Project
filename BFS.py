            Output: The vertices in a shortest path from from_vertex to to_vertex
                    and the number of edges in that path.

            Example graph output:
                Vertices in shortest path: 1,2,5
                Number of edges in shortest path: 3
        """
        if from_vert < 1 or from_vert > self.numberOfVertices:
            raise Exception("Vertex out of bounds.")

        if to_vert < 1 or to_vert > self.numberOfVertices:
            raise Exception("Vertex out of bounds.")

        if self.vertices[from_vert-1][to_vert-1] == 1: # exit early if the to_vertex is adjacent to the from_vertex
            return "Vertices in shortest path: " + str(from_vert) + "," + str(to_vert) + "\n" + "Number of edges in shortest path: 1"

        result = []
        queue = deque()
        checkedArray = self.numberOfVertices * [False] # to keep track of vertices that have been visited already.

        queue.append(from_vert)
        checkedArray[from_vert-1] = True

        while queue:

            current = queue.popleft()
            result.append(current)
            if current == to_vert:
                # a list comprehension that takes the 'result' array and casts it to a string w/o adding a comma after the last item.
                result = [str(entry)+"," if i != len(result)-1 else str(entry) for i, entry in enumerate(result)]
                return "Vertices in shortest path: " + "".join(result) + "\n" + "Number of edges in shortest path: " + str(len(result)-1)

            for i, vertex in enumerate(self.vertices[current-1]):
                if vertex != 0 and checkedArray[i] == False:
                    queue.append(i+1)
                    checkedArray[i] = True

        return result
