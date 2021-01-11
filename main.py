from ThreeSAT import *
from clause import *
from edge import *
from graph import *
from vertex import *
from vertex_cover import *
from fileManager import *
from graph_transformation import *
import networkx as nx
import matplotlib.pyplot as plt


three_sat = ThreeSAT()
vtx_cover = VertexCoverFrom3SAT(three_sat)
file_loader = FileManager(three_sat, "file.sat3")
file_loader.loadFile()
vtx_cover.build_vc()
visual_graph = graph_transformation(vtx_cover.graph)
visual_graph.print_graph()
