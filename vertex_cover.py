from ThreeSAT import *
from graph import *

class VertexCover :
  def __init__(self, threeSAT):
    self.three_sat = threeSAT
    self.graph = Graph()
    
  def build_vc(self):
    self.create_literals()
    self.create_clauses()
  
  def create_literals(self):
    for i in range(len(self.three_sat.literals)):
      self.graph.insert_edge(self.three_sat.literals[i], "!" + self.three_sat.literals[i])
          

  def create_clauses(self):
    aux = 1
    for clause in self.three_sat.clauses:
      for i in range(len(clause.literals)):
        self.graph.insert_edge("a" + str(aux) + "[" + str(i) + "]", clause.literals[i])
        if (i > 0):
          self.graph.insert_edge("a" + str(aux) + "[" + str(i - 1) + "]", "a" + str(aux) + "[" + str(i) + "]")
      self.graph.insert_edge("a" + str(aux) + "[0]", "a" + str(aux) + "[" + str((len(clause.literals) - 1)) + "]")
      aux += 1
  
  def print_vc(self):
    # print(self.three_sat.to_string())
    for vertex in self.graph.vertices.values():
      print(vertex.id)
      for edge in vertex.edges:
        print(edge.to_string())
      print()
