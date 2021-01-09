from ThreeSAT import *
from clause import *
from edge import *
from graph import *
from vertex import *
from vertex_cover import *
from fileManager import *

three_sat = ThreeSAT()
vtx_cover = VertexCover(three_sat)
file_loader = FileManager(three_sat, "file.sat3")
file_loader.loadFile()
print(three_sat.to_string())
vtx_cover.build_vc()
vtx_cover.print_vc()