from edge import *
from vertex import *

class Graph:
  def __init__(self, file_name = ''):
    self.file_name = file_name
    self.vertices = {}
    self.clauses = []

  def add_vertex(self, vertex):
    if not vertex.id in self.vertices:
      self.vertices[vertex.id] = vertex


  def insert_edge(self, vertex1, vertex2):
    self.add_vertex(Vertex(vertex1))
    self.add_vertex(Vertex(vertex2))

    nv1 = self.vertices[vertex1]
    nv2 = self.vertices[vertex2]

    edge1 = Edge(nv1, nv2)
    edge2 = Edge(nv2, nv1)
    
    self.vertices[vertex1].add_edge(edge1)
    self.vertices[vertex2].add_edge(edge2)



  def get_edges(self):
    my_edges = set()
    for vertex in self.vertices.values():
      for edge in vertex.edges :
        my_edges.add(edge)
    return my_edges
  
    