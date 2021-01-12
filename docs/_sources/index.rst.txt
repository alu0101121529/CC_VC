.. Vertex Cover documentation master file, created by
   sphinx-quickstart on Mon Jan 11 17:36:41 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Vertex Cover's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Class graph 
========================================

.. automodule:: graph
.. autoclass:: Graph
.. automethod:: Graph.add_vertex
.. automethod:: Graph.insert_edge
.. automethod:: Graph.get_edges

Class graph_transformation
===================================================

.. automodule:: graph_transformation
.. autoclass:: graph_transformation
.. automethod:: graph_transformation.build_nodes
.. automethod:: graph_transformation.build_edges
.. automethod:: graph_transformation.print_graph

Class ThreeSAT 
=========================================================

.. automodule:: ThreeSAT
.. autoclass:: ThreeSAT
.. automethod:: ThreeSAT.clear
.. automethod:: ThreeSAT.add_literal
.. automethod:: ThreeSAT.add_clause
.. automethod:: ThreeSAT.to_string

Class vertex 
========================================

.. automodule:: vertex
.. autoclass:: Vertex
.. automethod:: Vertex.change_id
.. automethod:: Vertex.get_id
.. automethod:: Vertex.add_edge
.. automethod:: Vertex.visit
.. automethod:: Vertex.unvisit

Class edge 
========================================

.. automodule:: edge
.. autoclass:: Edge
.. automethod:: Edge.move_edge
.. automethod:: Edge.to_string

Class clause 
========================================

.. automodule:: clause
.. autoclass:: Clause
.. automethod:: Clause.set_clause
.. automethod:: Clause.add_literal
.. automethod:: Clause.add_literal_at_pos
.. automethod:: Clause.to_string


Class vertex_cover 
================================================================

.. automodule:: vertex_cover
.. autoclass:: VertexCoverFrom3SAT
.. automethod:: VertexCoverFrom3SAT.build_vc
.. automethod:: VertexCoverFrom3SAT.create_literals
.. automethod:: VertexCoverFrom3SAT.create_clauses
.. automethod:: VertexCoverFrom3SAT.print_vc


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
