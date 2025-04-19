class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    def get_vertices(self):
        return list(self.gdict.keys())
    def edges(self):
        return self.find_edges()
    def find_edges(self):
        edge_name = []
        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if {next_vertex, vertex} not in edge_name:
                    edge_name.append({vertex, next_vertex})
        return edge_name