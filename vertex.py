"""
.. module:: vertex
   :platform: Unix, Windows
   :synopsis: Clase para representar un vértice en el grafo
   :noindex:

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>


"""

class Vertex:
  """
  .. class:: Vertex
  
    Clase vértice.
    
  """
  def __init__(self, literal):
    """
    .. method:: constructor(literal)
      :noindex:
      
    :param Literal literal: Clausura que queremos meter en el vértice
    
      Constructor a partir de un literal.
      Un vértice vendrá definido por el id del
      vértice, su conjunto de aristas, y por si
      está definido o no (necesario para resolver
      el problema del vertex cover)
      
    """
    self.id = literal
    self.edges = []
    self.visited = False

  def change_id(self, new_literal):
    """
    .. method:: change_id(new_literal)
      :noindex:
      
    :param String new_literal: nuevo literal que queremos en el vértice

      Función que nos permite cambiar el id del
      nodo.
      
    """
    self.id = new_literal

  def get_id(self):
    """
    .. method:: get_id()
      :noindex:
      
      Funcion que retorna el id del nodo.
    
    """
    return self.id

  def add_edge(self, edge):
    """
    .. method:: add_edge(edge)
      :noindex:
      
    :param Edge edge: Arista a añadir
    
      Funcion que añade una arista al conjunto de
      aristas del nodo.
    
    """
    self.edges.append(edge)

  def visit(self):
    """
    .. method:: visit()
      :noindex:
      
      Funcion que cambia el estado del nodo a visitado
    
    """
    self.visited = True
  
  def unvisit(self):
    """
    .. method:: unvisit()
      :noindex:
      
      Funcion que cambia el estado del nodo a no visitado
    
    """
    self.visited = False