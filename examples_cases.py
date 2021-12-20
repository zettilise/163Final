from make_monotone import make_mono
from stopping_points import *
from status import Status
from graph_struct import *

# first set
v1 = Vertex(-3,1, 1)
v2 = Vertex(0,0, 2)
v3 = Vertex(3,4, 3)
v4 = Vertex(-2,5, 4)
v5 = Vertex(-1,2, 5)


p = Polygon(v1, v2, v3)
p.add_vertex(v4)
p.add_vertex(v5)



# Second set 
v1 = Vertex(-8,0, 1)
v2 = Vertex(-7,-4, 2)
v3 = Vertex(-1,-9, 3)
v4 = Vertex(-4,-4, 4)
v5 = Vertex(2,-10, 5)
v6 = Vertex(4, -8, 6)
v7 = Vertex(1,-7,7)
v8 = Vertex(8, -6, 8)
v9 = Vertex(3,-3,9)
v10 = Vertex(2,2,10)
v11 = Vertex(-4,4,11)
v12 = Vertex(-3, -1, 12)
v13 = Vertex(-5,1,13)

p = Polygon(v1, v2, v3)
p.add_vertex(v4)
p.add_vertex(v5)
p.add_vertex(v6)
p.add_vertex(v7)
p.add_vertex(v8)
p.add_vertex(v9)
p.add_vertex(v10)
p.add_vertex(v11)
p.add_vertex(v12)
p.add_vertex(v13)