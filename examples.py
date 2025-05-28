import graph as g
import breadth_first_search as bfs
import depth_first_search as dfs

#Change colors of terminal
green = '\033[92m'
head = '\033[95m'
end = '\033[0m'

graph1 = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "F"],
    "C": ["A", "G"],
    "D": ["B"],
    "E": ["A", "F"],
    "F": ["B", "E"],
    "G": ["C"]
}

graph2 = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
    "D": ["E", "F"],
    "E": ["D", "F"],
    "F": ["D", "E"],
    "G": []  # Isolated node
}

graph3 = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "E"],
    "E": ["B", "D", "F"],
    "F": ["C", "E", "A"]  # Creates a cycle A->F->A
}

graph4 = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G", "H"],
    "F": [],
    "G": [],
    "H": []
}

graph5 = {
    "A": ["B", "C", "D", "E"],
    "B": ["A", "C", "D", "E"],
    "C": ["A", "B", "D", "E"],
    "D": ["A", "B", "C", "E"],
    "E": ["A", "B", "C", "D"]
}

graph6 = {
    "Center": ["A", "B", "C", "D", "E", "F"],
    "A": ["Center"],
    "B": ["Center"],
    "C": ["Center"],
    "D": ["Center"],
    "E": ["Center"],
    "F": ["Center"]
}

graph7 = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C", "E"],
    "E": ["D", "F"],
    "F": ["E", "G"],
    "G": ["F"]
}

graph8 = {
    "A1": ["B1", "B2", "B3"],
    "A2": ["B1", "B3"],
    "A3": ["B2"],
    "B1": ["A1", "A2"],
    "B2": ["A1", "A3"],
    "B3": ["A1", "A2"]
}

graph9 = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": [],
    "F": ["E"],
    "G": []
}

graph10 = {
    "1": ["2", "3", "4"],
    "2": ["1", "5", "6"],
    "3": ["1", "7", "8"],
    "4": ["1", "9", "10"],
    "5": ["2", "11"],
    "6": ["2", "11"],
    "7": ["3", "12"],
    "8": ["3", "12"],
    "9": ["4", "13"],
    "10": ["4", "13"],
    "11": ["5", "6", "14"],
    "12": ["7", "8", "14"],
    "13": ["9", "10", "14"],
    "14": ["11", "12", "13"]
}

g1 = g.Graph(graph1)
g2 = g.Graph(graph2)
g3 = g.Graph(graph3)
g4 = g.Graph(graph4)
g5 = g.Graph(graph5)
g6 = g.Graph(graph6)
g7 = g.Graph(graph7)
g8 = g.Graph(graph8)
g9 = g.Graph(graph9)
g10 = g.Graph(graph10)

print(f"\n\n{head}Grafo 1{end}")
print('Vertices=', g1.get_vertices())
print('Aristas =', g1.edges())
print("Depth First Search")
dfs.depth_first_search(g1, "A")
print("\nBreadth First Search")
bfs.breadth_first_search(g1, "A")

print(f"\n\n{head}Grafo 2{end}")
print('Vertices=', g2.get_vertices())
print('Aristas =', g2.edges())
print("Depth First Search")
dfs.depth_first_search(g2, "A")
print("\nBreadth First Search")
bfs.breadth_first_search(g2, "A")

print(f"\n\n{head}Grafo 3{end}")
print('Vertices=', g3.get_vertices())
print('Aristas =', g3.edges())
print("Depth First Search")
dfs.depth_first_search(g3, "A")
print("\nBreadth First Search")
bfs.breadth_first_search(g3, "A")

print(f"\n\n{head}Grafo 4{end}")
print('Vertices=', g4.get_vertices())
print('Aristas =', g4.edges())
print("Depth First Search")
dfs.depth_first_search(g4, "A")
print("\nBreadth First Search")
bfs.breadth_first_search(g4, "A")

print(f"\n\n{head}Grafo 5{end}")
print('Vertices=', g5.get_vertices())
print('Aristas =', g5.edges())
print("Depth First Search")
dfs.depth_first_search(g5, "A")
print("\nBreadth First Search")
bfs.breadth_first_search(g5, "A")

print(f"\n\n{head}Grafo 6{end}")
print('Vertices=', g6.get_vertices())
print('Aristas =', g6.edges())
print("Depth First Search")
dfs.depth_first_search(g6, "Center")
print("\nBreadth First Search")
bfs.breadth_first_search(g6, "Center")

print(f"\n\n{head}Grafo 7{end}")
print('Vertices=', g7.get_vertices())
print('Aristas =', g7.edges())
print("Depth First Search")
dfs.depth_first_search(g7, "A")
print("\nBreadth First Search")
bfs.breadth_first_search(g7, "A")

print(f"\n\n{head}Grafo 8{end}")
print('Vertices=', g8.get_vertices())
print('Aristas =', g8.edges())
print("Depth First Search")
dfs.depth_first_search(g8, "A1")
print("\nBreadth First Search")
bfs.breadth_first_search(g8, "A1")

print(f"\n\n{head}Grafo 9{end}")
print('Vertices=', g9.get_vertices())
print('Aristas =', g9.edges())
print("Depth First Search")
dfs.depth_first_search(g9, "A")
print("\nBreadth First Search")
bfs.breadth_first_search(g9, "A")

print(f"\n\n{head}Grafo 10{end}")
print('Vertices=', g10.get_vertices())
print('Aristas =', g10.edges())
print("Depth First Search")
dfs.depth_first_search(g10, "1")
print("\nBreadth First Search")
bfs.breadth_first_search(g10, "1")