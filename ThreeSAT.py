from clause import *

"""
.. module:: ThreeSAT
   :platform: Unix, Windows
   :synopsis: Clase para representar el problema de satisfactibilidad con 3 literales

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>

"""

class ThreeSAT:
  """
  .. class:: ThreeSAT
  
    Clase 3-satisfactibilidad.
    Representa el problema descrito, donde tendremos,
    un número de literales, un conjunto de literales,
    un tamaño de clausula, un conjunto de clausulas
    y un k-valor que representará el número de nodos
    que necesitaremos para crear el vertex cover.
  
  """
  def __init__(self) :
    self.literals = []
    self.clauses = []
    self.clause_size = 3
    self.number_of_literals = 0
    self.k = 0
  
  def clear(self):
    """
    .. method:: clear()
      :noindex:
    
      Función que reseteará aquellos atributos
      que puedan variar de una instancia a otra
      
    """
    self.literals = []
    self.clauses = []
    self.number_of_literals = 0
    self.k = 0
      
  def add_literal(self, literal):
    """
    .. method:: add_literal(literal)
      :noindex:
    
    :param Literal literal: que quieres añadir al conjunto
    
      Función que añade un literal al conjunto de
      literales del 3SAT
      
    """
    self.literals.append(literal)
  
  def add_clause(self, clause):
    """
    .. method:: add_clause(clause)
      :noindex:
    
    :param Clause clause: Cláusula que quieres añadir al conjunto

      Función que añade una clausula al conjunto de
      clausulas del 3SAT
      
    """
    self.clauses.append(clause)

  def to_string(self) :
    """
    .. method:: to_string()
      :noindex:
    
      Función que retorna una cadena que representa
      el problema 3SAT instanciado.
      
    :returns: 
      String
    
    """
    string = "U = {"

    for literal in self.literals:
        string += literal + ", "

    string += "} "
    string += "C = {"

    for clause in self.clauses: 
      string += clause.to_string() + ", "
    string += "} k = " + str(self.k)

    return string