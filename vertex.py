class Vertex:
    def __init__(self, point):
        self.x = point.x
        self.y = point.y
        self.edges = []
        self.visited = False
    
    def move_vertex(self, new_point):
        self.point = new_point

    def get_id(self):
        string = str(self.x) + ' ' + str(self.y)
        return string
