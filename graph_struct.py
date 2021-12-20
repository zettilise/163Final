"""
File containing classes defined Vertices and Edges in Graph
By Zetty Cho

I am very much not obeying Python naming conventions.... I just want
this to work ;-;


Extreme spaghetti code ahead

"""
# used for plotting graph
import networkx as nx
import matplotlib.pyplot as plt
from copy import copy, deepcopy

class Polygon:
    # This won't be able to remove vertices bc that's too much work

    def __init__(self, v1, v2, v3):
        """
        Initializes polygon with at least 3 vertices, connected in the order
        they are listed (please pass in CCW order)
        """

        # start of DLL of linked list of vertices
        # Honestly, I think this LL is useless rn... but for memory's sake...
        v1.v_next = v2
        v1.v_prev = v3

        v2.v_next = v3
        v2.v_prev = v1 

        v3.v_next = v1 
        v3.v_prev = v2 

        self.head = v1 
        self.vertices = [v1, v2, v3]

        # Initializes graph to make pretty picture
        self.graph = nx.Graph()
        self.count = 3
        self.graph.add_node(1, pos=v1.coord)
        self.graph.add_node(2, pos=v2.coord)
        self.graph.add_node(3, pos=v3.coord)


    def add_vertex(self, v):
        """ Adds to the DLL """
        v.v_prev = self.head.v_prev 
        self.head.v_prev.v_next = v 

        v.v_next = self.head 
        self.head.v_prev = v 

        # Reset the vertex list
        self.vertices[0] = self.head 
        self.vertices[self.count - 1] = v.v_prev
        self.vertices.append(v)
        self.count += 1

        # Now add to graph
        self.graph.add_node(self.count, pos=v.coord)
        return self

    def create_graph(self):
        """ 
        Initializes NX graph for plotting and stuff 
        Adds in all the edges
        """

        for i in range(1, self.count):
            self.graph.add_edge(i, i + 1, color='b')

        
        self.graph.add_edge(1, self.count, color='b')

        nx.draw(self.graph, nx.get_node_attributes(self.graph, 'pos'), with_labels=True, node_size=1)
        # plt.show()



    def __str__(self):
        return ', '.join([str(i) for i in self.vertices])


 

class Vertex:

    def __init__(self, x, y, label):
        """
        Defines vertex by x and y coordinate. 
        In this program each vertex will only have two edges.
        Initializes edges to be None
        """
        self.x = x
        self.y = y
        self.coord = (x, y)

        # These are specifically for the polygon
        self.v_next = None          # vertex coming in from ccw direction
        self.v_prev = None          # vertex exiting from ccw direction

        self.name = label
        
        # This is for when we define vertices in make monotone
        # This could be made nicer, but this is spaghetti code... so no
        # self.e_next = None
        # self.e_prev = None
        self.type = None


    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __eq__(self, other):
        """ self comparison of vertex objects """
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """ for sorting """

        return self.x < other.x

        

class Edge:

    def __init__(self, v1, v2):
        """
        Defines an edge
        We assume general position, so don't need to worry about horizontal lines.
        Setting it up to use it in DCEL
        """

        if v1.x < v2.x:
            left = v1
            right = v2 
        else:
            left = v2
            right = v1

        self.left = left
        self.right = right
        self.helper = None

        # requires python 3
        self.slope = (left.y - right.y) / (left.x - right.x)

        # y-intercept
        self.b = left.y - (self.slope * left.x)


    def __str__(self):
        # return "(%f, %f) to (%f, %f)" % (self.left.x, self.left.y, self.right.x, self.right.y)
        # return "(" + str(self.left) + ", " + str(self.right) + ")"
        return "(" + str(self.left.name) + ", " + str(self.right.name) + ")"

    def __eq__(self, other):
        """ self comparison of vertex objects """
        return self.left == other.left and self.right == other.right

    def __lt__(self, other):
        """ for sorting """
        x = other.left.x # get the x coord of the other one
        y = self.slope * x + self.b
        # print("self is ", self, " and other is ", other)
        if y == other.left.y:   # They share left endpoint
            # if self.right.y < other.right.y:
            #     return True
            # else:
            #     return self.right.x < other.right.x
            return self.slope < other.slope
        else:                   # They don't share left endpoint
            return y < other.left.y

  
        