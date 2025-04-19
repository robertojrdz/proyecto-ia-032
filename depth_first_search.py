import graph as g

def depth_first_search(graph, initial_vertex, labels = {}):
    if labels == {}:
        for vertex in graph.get_vertices():
            labels[vertex] = False
    labels[initial_vertex] = True
    print(initial_vertex + ", ", end="")
    for edge in graph.edges():
        if initial_vertex in edge:
            for next_vertex in edge:
                if initial_vertex != next_vertex:
                    if not labels[next_vertex]:
                        depth_first_search(graph, next_vertex, labels)

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

#Ejemplo DFS
depth_first_search(g, "A")