class Vertex:
  def __init__(self, literal):
    self.id = literal
    self.edges = []
    self.visited = False

  def change_id(self, new_literal):
    self.id = new_literal

  def get_id(self):
    return self.id

  def add_edge(self, edge):
    self.edges.append(edge)

  def visit(self):
    self.visited = True
  
  def unvisit(self):
    self.visited = False