import networkx as nx
import matplotlib.pyplot as plt
from vertex_cover import *
from edge import *
from graph import *
from vertex import *

class graph_transformation:
  def __init__(self, graph):
    self.__original_graph = graph
    self.__networkx_graph = nx.Graph()
    super().__init__()
  
  def build_nodes(self):
    self.__networkx_graph.add_nodes_from(self.__original_graph.vertices)
    
  def build_edges(self):
    networkx_edges = []
    original_edges = self.__original_graph.get_edges()
    for edge in original_edges:
      dummy_edge= (edge.start_vertex.id, edge.end_vertex.id)
      networkx_edges.append(dummy_edge)
    self.__networkx_graph.add_edges_from(networkx_edges)
    
  def print_graph(self):
    self.build_nodes()
    self.build_edges()
    pos=nx.spring_layout(self.__networkx_graph)
    nx.draw(self.__networkx_graph, pos, with_labels = True, node_size = 800, font_size = 8)
    plt.show()