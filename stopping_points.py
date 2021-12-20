from graph_struct import *


# Sorts list of vertices by their x coordinates

def get_stopping_points(vertices):
    return sorted(vertices)

# I'm making this a class so I can print things nicely :) It doesn't have to be

# class StoppingPoints:

#     def __init__(self, vertices):
#         self.points = vertices.sort()

#     def __str__(self):
#         ', '.join([str(i) for i in self.points])