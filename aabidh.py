class Graph:
    """
    A class representing an arbitrary sized graph.
    """
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v):
        """
        Add an edge between vertices u and v.
        """
        if 0 <= u < self.size and 0 <= v < self.size:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1

    def is_edge(self, u, v):
        """
        Check if there is an edge between vertices u and v.
        """
        if 0 <= u < self.size and 0 <= v < self.size:
            return self.matrix[u][v] == 1
        return False

    def bfs(self, start_vertex):
        """
        Perform breadth-first search starting from the given vertex.
        """
        visited = [False] * self.size
        queue = [start_vertex]
        visited[start_vertex] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for i in range(self.size):
                if self.matrix[vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, start_vertex):
        """
        Perform depth-first search starting from the given vertex.
        """
        visited = [False] * self.size
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        """
        Helper function for recursive depth-first search.
        """
        visited[vertex] = True
        print(vertex, end=' ')

        for i in range(self.size):
            if self.matrix[vertex][i] == 1 and not visited[i]:
                self._dfs_recursive(i, visited)


# Example Usage:
graph = Graph(11)  # Change the size to 11

# Adding edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(1, 5)
graph.add_edge(1, 6)
graph.add_edge(2, 7)
graph.add_edge(3, 8)
graph.add_edge(4, 9)
graph.add_edge(5, 10)

print("bfs")
graph.bfs(0)
print("\n")

print("dfs")
graph.dfs(0)
print("\n")