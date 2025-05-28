#Change colors of terminal
green = '\033[92m'
end = '\033[0m'

def depth_first_search(graph, initial_vertex, labels = None):
    if labels is None:
        labels = {vertex: False for vertex in graph.get_vertices()}

    labels[initial_vertex] = True

    print(green + initial_vertex + ", ", end=f"{end}")

    for edge in graph.edges():
        if initial_vertex in edge:
            for next_vertex in edge:
                if initial_vertex != next_vertex:
                    if not labels[next_vertex]:
                        depth_first_search(graph, next_vertex, labels)