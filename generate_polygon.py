import random

from numpy.core.function_base import add_newdoc 
from graph_struct import *
import numpy as np

def order_vertices(x, y):
    """ 
    Orders in CCW order 
    taken from https://stackoverflow.com/questions/58377015/counterclockwise-sorting-of-x-y-data
    """

    x0 = np.mean(x)
    y0 = np.mean(y)

    r = np.sqrt((x-x0)**2 + (y-y0)**2)

    angles = np.where((y-y0) > 0, np.arccos((x-x0)/r), 2*np.pi-np.arccos((x-x0)/r))

    mask = np.argsort(angles)

    x_sorted = np.array(x)[mask]
    y_sorted = np.array(y)[mask]

    return (x_sorted, y_sorted)


def make_vertex(x, y, index):
    return Vertex(x, y, index)

def generate_vertices(min, max):
    """
    Generates random set of points in 2D plane. 
    Parameters create bounding region to do so. 
    """

    random.seed(2)


    x = list(range(min, max))
    y = x.copy()
    random.shuffle(y)

    x_sorted, y_sorted = order_vertices(x,y)

    vertices = []
    for index, (x, y) in enumerate(zip(x_sorted, y_sorted)):
        vertices.append(make_vertex(x, y, index + 1))

    return vertices



def generate_polygon(min, max):
    """
    Initializes our polygon
    """
    vertices = generate_vertices(min, max)
    p = Polygon(vertices[0], vertices[1], vertices[2])

    for i in range(3, len(vertices)):
        p.add_vertex(vertices[i])

    p.create_graph()

    return p