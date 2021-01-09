class Clause: 

  def __init__(self) :
    self.literals = []
  
  def set_clause(self, new_clause):
    self.literals = new_clause
  

  def add_literal(self, new_literal):
    self.literals.append(new_literal)
  
  def add_literal_at_pos(self, literal, index):
    self.literals.insert(index, literal)

  def to_string(self):
    string = "{"

    for literal in self.literals:
      string += literal + ", "
    
    string += "}"
    return string