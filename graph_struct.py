"""
File containing classes defined Vertices and Edges in Graph
By Zetty Cho

I am very much not obeying Python naming conventions.... I just want
this to work ;-;

"""


class Vertex:

    def __init__(self, x, y):
        """
        Defines vertex by x and y coordinate. 
        In this program each vertex will only have two edges.
        Initializes edges to be None
        """
        self.x = x
        self.y = y
        self.e1 = None
        self.e2 = None

    

        

class Edge:

    def __init__(self, left, right):
        """
        Defines an edge by its left and right endpoints.
        We assume general position, so don't need to worry about horizontal lines.

        """
        self.left = left
        self.right = right

        # requires python 3
        self.slope = (left.y - right.y) / (left.x - right.x)

        # y-intercept
        self.b = left.y - (self.slope * left.x)
