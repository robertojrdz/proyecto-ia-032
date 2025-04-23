import graph as g
from collections import deque

def breadth_first_search(graph, initial_vertex):
    visited = {vertex: False for vertex in graph.get_vertices()}
    queue = deque()

    visited[initial_vertex] = True
    queue.append(initial_vertex)

    while queue:
        current = queue.popleft()
        print(current + ", ", end="")

        for edge in graph.edges():
            if current in edge:
                for neighbor in edge:
                    if neighbor != current and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

# Ejemplo Grafo
graph_elements = {
    "A" : ["B", "C", "E"],
    "B" : ["A", "D", "F"],
    "C" : ["A", "G"],
    "D" : ["B"],
    "E" : ["A", "F"],
    "F" : ["B", "E"],
    "G" : ["C"]
}
g = g.Graph(graph_elements)
print('V=', g.get_vertices())
print('E=', g.edges())

# Ejemplo BFS
breadth_first_search(g, "A")
