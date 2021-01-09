from clause import *

class ThreeSAT:
  def __init__(self) :
    self.literals = []
    self.clauses = []
    self.clause_size = 3
    self.number_of_literals = 0
    self.k = 0
  
  def clear(self):
    self.literals = []
    self.clauses = []
    self.number_of_literals = 0
      
  def add_literal(self, literal):
    self.literals.append(literal)
  
  def add_clause(self, clause):
    self.clauses.append(clause)

  def to_string(self) :
    string = "U = {"
  

    for literal in self.literals:
        string += literal + ", "

    string += "} "
    string += "C = {"

    for clause in self.clauses: 
      string += clause.to_string() + ", "
    string += "} k = " + str(self.k)

    return string