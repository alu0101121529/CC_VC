from point import *
from edge import *
from graph import *
from vertex import *
from vertex_cover import *

point1 = Point(3, 4)
point2 = Point(5, 10)

vertex1 = Vertex(point1)
vertex2 = Vertex(point2)

graph1 = Graph()

graph1.insert_vertex(vertex1)
graph1.insert_vertex(vertex2)

edge1 = Edge(vertex1, vertex2)

graph1.insert_edge(edge1)

# print(graph1.vertices['3 4'].edges[0].start_vertex.x)

VC = Vertex_cover(graph1)
VC.solve()