from ThreeSAT import *
from clause import *

"""
.. module:: FileManager
   :platform: Unix, Windows
   :synopsis: `Clase que sirve para el tratamiento de los ficheros de entrada
              que trae la instancia del problema`

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>


"""

class FileManager:
  """
    :class:`FileManager`
    Clase controlador de fichero. 
    Esta será la clase encargada de leer de fichero la instancia
    del problema 3SAT y almacenarla para cualquier otra clase que
    necesite hacer uso de esta.
  """

  def __init__(self, three_sat, file_name = ''):
    """
      .. function:: constructor(three_sat, filename)
      :param three_sat Variable donde se almacenará la instancia
      del 3SAT
      :type three_sat: ThreeSAT
      :param file_name Fichero del que leeremos que contendrá
      presuntamente la información del problema 3SAT
      :type file_name: String
    """
    self.three_sat = three_sat
    self.file_name = file_name

  def loadFile(self):
    """
      .. function:: loadFile()
      Función que se encargará de leer del fichero introducido
      Primero leerá el número de literales que componene nuestro 3SAT.
      A continuación leerá y almacenará estos literales, y por último
      leerá las clausulas y por último calcula el k-valor para el problema.
      Al final del proceso ya tendrá creada la instancia del 3SAT almacenada
      en la variable self.three_sat.
    """ 
    my_file = open(self.file_name)
    self.three_sat.number_of_literals = int(my_file.readline())
    file_information = my_file.readlines()
    i = 0
    clauses = []
    literals = []
    for line in file_information:
      if i >= self.three_sat.number_of_literals:
        clauses.append(line.rstrip('\n'))
      else:
        literals.append(line.rstrip('\n'))
        i += 1   
    self.add_all_literals(literals)
    self.create_all_clauses(clauses) 
    self.compute_k_value()
    my_file.close()
      
  def add_all_literals(self, literals):
    """
      .. function:: add_all_literals()
      Función que recibe todo el conjunto de literales y los almacena
      en el 3SAT.
    """
    for literal in literals:
      self.three_sat.add_literal(literal)

  def create_all_clauses(self, clauses):
    """
    .. function:: create_all_clauses(clauses)
    Función encargada de recibir el conjunto de clausulas
    y almacenarlas como clausulas individuales.
    :param clauses Array con todas las cláusulas
    :type clauses: Array(Clauses)
    """
    for x in clauses:
        line = x.split()
        clause = Clause()
        for literal in range(self.three_sat.clause_size):
          clause.add_literal(line[literal])
        
        self.three_sat.clauses.append(clause)

  def compute_k_value(self):
    """
      .. function:: compute_k_value()
      Función para calcular el k-valor del problema
    """
    self.three_sat.k = len(self.three_sat.literals) + 2 * len(self.three_sat.clauses)
    