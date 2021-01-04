import igraph
from igraph import *

g = Graph()
g.add_vertices(6)
g.add_edges([(0,1), (1,2), (2,0), (2, 3), (3, 4), (4, 5), (5, 3)])
print(g)
layout = g.layout("kk")
plot(g, layout = layout)