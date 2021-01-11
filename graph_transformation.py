import networkx as nx
import matplotlib.pyplot as plt
from vertex_cover import *
from edge import *
from graph import *
from vertex import *

"""
.. module:: graph_transformation
   :platform: Unix, Windows
   :synopsis: Clase para transformar nuestro grafo en uno compatible de la librería networkx
              y mostrar por pantalla un gráfico creado usando matplotlib

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>


"""

class graph_transformation:
  """
    .. class:: graph_transformation
     
      Clase que dado un grafo del modulo :func:`graph` es capaz de transformarlo
      en uno de la librería :func:`networkx`
      
  """
  def __init__(self, graph):
    self.__original_graph = graph
    self.__networkx_graph = nx.Graph()
    super().__init__()
  
  def build_nodes(self):
    """
    .. method:: build_nodes()
      :noindex:

      Pasa los nodos del grafo original a un grafo de networkx
      
    """
    self.__networkx_graph.add_nodes_from(self.__original_graph.vertices)
    
  def build_edges(self):
    """
    .. method:: build_edges()
      :noindex:
      
      Pasa las aristas del grafo original a un grafo de networkx
      
    """
    networkx_edges = []
    original_edges = self.__original_graph.get_edges()
    for edge in original_edges:
      dummy_edge= (edge.start_vertex.id, edge.end_vertex.id)
      networkx_edges.append(dummy_edge)
    self.__networkx_graph.add_edges_from(networkx_edges)
    
  def print_graph(self):
    """
    .. method:: print_graph()
      :noindex:

      Crea el grafo de networkx y lo dibuja haciendo una gráfica con matplotlib
      
    """
    self.build_nodes()
    self.build_edges()
    pos=nx.spring_layout(self.__networkx_graph)
    nx.draw(self.__networkx_graph, pos, with_labels = True, node_size = 800, font_size = 8)
    plt.show()