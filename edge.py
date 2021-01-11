"""
.. module:: edge
   :noindex:
   :platform: Unix, Windows
   :synopsis: Clase para representar una arista en el grafo

.. moduleauthor:: Guillermo Hernández González <alu0101121529@ull.edu.es>
.. moduleauthor:: Manuel Andrés Carrera Galafate <alu0101132020@ull.edu.es>
.. moduleauthor:: Victoria Manrique Rolo <alu0101122083@ull.edu.es>
.. moduleauthor:: Carlos Díaz Calzadilla <alu0101102726@ull.edu.es>


"""

class Edge:
    """
    .. class:: Edge
    
        Clase arista. Esta vendrá definida por las 2
        aristas que la forman.
    
    """
    def __init__(self, start_vertex, end_vertex):
        """
        .. method:: constructor(start_vertex, end_vertex)
            :noindex:
        
        :param Vertex start_vertex: Vértice inicial

        :param Vertex end_vertex: Vértice final
        
            Constructor a partir de 2 vértices. Almacena
            la referencia ambas.
        
        """
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
    
    def move_edge(self, new_start_vertex, new_end_vertex):
        """
        .. method(new_start_vertex, new_end_vertex)
            :noindex:
        
        :param Vertex start_vertex: Vértice inicial
        
        :param Vertex end_vertex: Vértice final
        
            Funcion que nos permite mover una arista. Para ello
            recibe las 2 nuevas aristas que la compondrán.
        
        """
        self.start_vertex = new_start_vertex
        self.end_vertex = new_end_vertex

    def to_string(self):
        """
        .. method:: to_string()
            :noindex:
        
            Funcion que retorna una cadena que representa la arista.
        
        """
        return self.start_vertex.id + " -> " + self.end_vertex.id