
class Vertex_cover:
    def __init__(self, graph):
        self.graph = graph

    def change_graph(new_graph):
        self.graph = new_graph
    
    def solve(self):
        my_vertices = set()
        my_edges = self.graph.get_edges()
        for edge in my_edges:
            if not U.visited:
                for edge in U.edges:
                    U.visited = True
                    self.graph.vertices[edge.end_vertex.get_id()].visited = True
                    break
        
