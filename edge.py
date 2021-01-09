class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
    
    def move_edge(self, new_start_vertex, new_end_vertex):
        self.start_vertex = new_start_vertex
        self.end_vertex = new_end_vertex

    def to_string(self):
        return self.start_vertex.id + " -> " + self.end_vertex.id