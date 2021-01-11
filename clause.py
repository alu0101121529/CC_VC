"""
.. module:: clause
   :platform: Unix, Windows
   :synopsis: Clase para representar una cláusula
   :noindex:

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>

"""
class Clause:
  """
    .. class:: Clause
    
      Clase Cláusula. Una claásula estará definida
      como una lista de literales
  
  """

  def __init__(self) :
    """
    .. method:: constructor()
      :noindex:
    
      Constructor por defecto. Instancia la lista de
      literales
    
    """
    self.literals = []
  
  def set_clause(self, new_clause):
    """
    .. method:: set_clause(new_clause)
      :noindex:
    
    :param List new_clause: Cláusula a añadir

      Función que nos permite cambiar la lista que define la
      clausula
   
    """
    self.literals = new_clause

  def add_literal(self, new_literal):
    """
    .. method:: add_literal(new_literal)
      :noindex:
    
    :param String new_literal Literal a añadir

      Función que nos permite añadir un literal a la lista
      actual de la clausula.
    
    """
    self.literals.append(new_literal)
  
  def add_literal_at_pos(self, literal, index):
    """
    .. method:: add_literal_at_pos(literal, index)
      :noindex:
    
    :param String literal: Literal a añadir
    
    :param Int index: Posición en la que se debe insertar el literal
    
      Función para añadir un literal a una posición concetra.
    
    """
    self.literals.insert(index, literal)

  def to_string(self):
    """
    .. method:: to_string()
      :noindex:
    
    :returns: 
      String 
    
      Funcion que retorna una cadena que representa la clausula.
    
    """
    string = "{"

    for literal in self.literals:
      string += literal + ", "
    
    string += "}"
    return string