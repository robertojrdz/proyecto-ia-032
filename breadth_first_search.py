from collections import deque

#Change colors of terminal
green = '\033[92m'
end = '\033[0m'

def breadth_first_search(graph, initial_vertex):
    visited = {vertex: False for vertex in graph.get_vertices()}
    queue = deque()

    visited[initial_vertex] = True
    queue.append(initial_vertex)

    while queue:
        current = queue.popleft()
        print(green + current + ", ", end=f"{end}")

        for edge in graph.edges():
            if current in edge:
                for neighbor in edge:
                    if neighbor != current and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)