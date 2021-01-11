from edge import *
from vertex import *

"""
.. module:: graph
   :platform: Unix, Windows
   :synopsis: Clase para representar un grafo

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>

"""

class Graph:
  """
  .. class:: Graph
  
    Clase grafo
    Esta clase contiene un conjunto de vertices que
    definen el grafo.
    
  """
  def __init__(self):
    """
    .. method:: contructor()
    
      Constructor por defecto 
     
    """
    self.vertices = {}

  def add_vertex(self, vertex):
    """
    .. method:: add_vertex(vertex)
      :noindex:
    
    :param Vertex vertex:  Vertice que quieres añadir
        
      Función que añade un vértice si aún no existe.
    
    """
    if not vertex.id in self.vertices:
      self.vertices[vertex.id] = vertex


  def insert_edge(self, vertex1, vertex2):
    """
    .. method:: insert_edge(vertex)
      :noindex:
      
    :param Vertex vertex1: Primer vértice de la arista
    
    :param Vertex vertex2: Segundo vértice de la arista

      Función que añade un nuevo vértice al grafo.
      Para ello necesita los 2 vértices que lo componen,
      los añade al grafo y genera un vértice del nodo 1
      al 2 y del 2 al 1 (para que ambos contengan la información)
    
    """
    self.add_vertex(Vertex(vertex1))
    self.add_vertex(Vertex(vertex2))

    nv1 = self.vertices[vertex1]
    nv2 = self.vertices[vertex2]

    edge1 = Edge(nv1, nv2)
    edge2 = Edge(nv2, nv1)
    
    self.vertices[vertex1].add_edge(edge1)
    self.vertices[vertex2].add_edge(edge2)


  def get_edges(self):
    """
    .. method:: get_edges()
      :noindex:
      
      Función que retorna el conjunto de todas las 
      aristas que conforman el grafo
    
    """
    my_edges = set()
    for vertex in self.vertices.values():
      for edge in vertex.edges :
        my_edges.add(edge)
    return my_edges
  
    