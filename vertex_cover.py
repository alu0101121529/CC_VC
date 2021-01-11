from ThreeSAT import *
from graph import *

"""
.. module:: vertex_cover
   :noindex:
   :platform: Unix, Windows
   :synopsis: Clase para representar el cubrimiento de vértices a partir de 3SAT

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>


"""

class VertexCoverFrom3SAT :
  """
    .. class:: VertexCoverFrom3Sat
    
      Clase cubrimiento de vertices a partir de 3SAT. 
      Esta clase crea una instancia del problema del cubrimiento minimo
      a partir de uno del problema de satisfactibilidad con clausulas
      de 3 literales. Contendrá como resultado de la conversion un grafo,
      donde cada nodo será o bien uno de los literales o bien una de las
      partes de las clausulas.
  
  """
  def __init__(self, threeSAT):
    """
    .. method:: constructor(threeSat)
      :noindex:
    
    :param ThreeSAT threeSAT: instancia del problema de satisfactibilidad 3SAT
    
      Constructor a partir de una instancia del 3SAT.
    
    """
    self.three_sat = threeSAT
    self.graph = Graph()
  
  def build_vc(self):
    """
    .. method:: build_vc()
      :noindex:

      Funcion encargada de crear el grafo. Se crearán los ditintos 
      nodos y sus aristas a partir de los literales y las clausulas
      del 3SAT.
    
    """
    self.create_literals()
    self.create_clauses()
  
  def create_literals(self):
    """
    .. method:: create_literals()
      :noindex:
    
      Funcion que creará los nodos de los distintos literales y sus
      negados unidos por una arista en el grafo
    
    """
    for literal in self.three_sat.literals:
      self.graph.insert_edge(literal, "!" + literal)  

  def create_clauses(self):
    """
    .. method:: create_clauses()
      :noindex:
    
      Función que añadirá los nodos de los literales de las distintas
      clausulas al grafo y añadirá aristas entre los de la misma clausula
      y además los literales que representan.
    
    """
    aux = 1
    for clause in self.three_sat.clauses:
      for i in range(len(clause.literals)):
        self.graph.insert_edge("a" + str(aux) + "[" + str(i) + "]", clause.literals[i])
        if (i > 0):
          self.graph.insert_edge("a" + str(aux) + "[" + str(i - 1) + "]", "a" + str(aux) + "[" + str(i) + "]")
      self.graph.insert_edge("a" + str(aux) + "[0]", "a" + str(aux) + "[" + str((len(clause.literals) - 1)) + "]")
      aux += 1
  
  def print_vc(self):
    """
    .. method:: print_vc()
      :noindex:
    
      Funcion de impresion que imprime los distintos vertices del grafo
      y las aristas que tienen cada uno.
    
    """
    for vertex in self.graph.vertices.values():
      print(vertex.id)
      for edge in vertex.edges:
        print(edge.to_string())
      print()
