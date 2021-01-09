from ThreeSAT import *
from clause import *

class FileManager:
  def __init__(self, three_sat, file_name = ''):
    self.file_name = file_name
    self.three_sat = three_sat

  def loadFile(self):    
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
      self.set_k_value()
      my_file.close()
      
  def add_all_literals(self, line):
    for i in range(self.three_sat.number_of_literals):
      self.three_sat.add_literal(line[i])

  def create_all_clauses(self, clauses):
    for x in clauses:
        line = x.split()
        clause = Clause()
        for literal in range(self.three_sat.clause_size):
          clause.add_literal(line[literal])
        
        self.three_sat.clauses.append(clause)

  def set_k_value(self):
    self.three_sat.k = len(self.three_sat.literals) + 2 * len(self.three_sat.clauses)
    