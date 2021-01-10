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
vtx_cover = VertexCover(three_sat)
file_loader = FileManager(three_sat, "file.sat3")
file_loader.loadFile()
print(three_sat.to_string())
vtx_cover.build_vc()
#vtx_cover.print_vc()
visual_graph = graph_transformation(vtx_cover.graph)
visual_graph.print_graph()


# original_graph = vtx_cover.graph

# G = nx.Graph()
# G.add_nodes_from(original_graph.vertices)
# G.add_edges_from(original_graph.get_edges()) 
# plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()
