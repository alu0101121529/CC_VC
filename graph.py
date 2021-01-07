from edge import *

class Graph:
    def __init__(self, file_name = ''):
        self.file_name = file_name
        self.vertices = {}

    def load_graph():
        if (file_name != ''):
            my_file = open(file_name)
            number_of_vertex = my_file.readline()
            while True:
                line = my_file.readline()
                line = line.split('|')
                point1 = line[0].split()
                point2 = line[1].split()
                vertex1 = Vertex(Point(point1[0], point1[1]))
                vertex2 = Vertex(Point(point2[0], point2[1]))
                insert_vertex(vertex1)
                insert_vertex(vertex2)
                edge = Edge(vertex1, vertex2)
                insert_edge(edge)
                if ("" == line):
                    print ("file finished")
                    break


    def insert_vertex(self, new_vertex):
        self.vertices[new_vertex.get_id()] = new_vertex
    
    def insert_edge(self, new_edge):
        first_vertex = new_edge.start_vertex
        second_vertex = new_edge.end_vertex
        for vertex in self.vertices.values():
            if vertex == first_vertex:
                vertex.edges.append(Edge(first_vertex, second_vertex))
            if vertex == second_vertex:
                vertex.edges.append(Edge(second_vertex, first_vertex))

    def get_edges(self):
        my_edges = set()
        for vertex in self.vertices.values():
            for edge in vertex.edges :
                my_edges.add(edge)
        return my_edges