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

class Polygon:
    # This won't be able to remove vertices bc that's too much work

    def __init__(self, v1, v2, v3):
        """
        Initializes polygon with at least 3 vertices, connected in the order
        they are listed (please pass in CCW order)
        """

        # start of DLL of linked list of vertices
        
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
            self.graph.add_edge(i, i + 1)
        
        self.graph.add_edge(1, self.count)

        nx.draw(self.graph, nx.get_node_attributes(self.graph, 'pos'), with_labels=True, node_size=0)
        plt.show()



    # def display_graph(self):
    #     nx.draw(self.graph, nx.get_node_attributes(self.graph, 'pos'), with_labels=True, node_size=0)
    #     plt.show()

    def __str__(self):
        return [str(i) for i in self.vertices]


 

class Vertex:

    def __init__(self, x, y):
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

        # This is for the DCEL
        self.edges = []


    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __eq__(self, other):
        """ self comparison of vertex objects """
        return self.x == other.x and self.y == other.y

        

class Edge:

    def __init__(self, left, right):
        """
        Defines an edge
        We assume general position, so don't need to worry about horizontal lines.
        Setting it up to use it in DCEL
        """
        self.left = left
        self.right = right

        # requires python 3
        self.slope = (left.y - right.y) / (left.x - right.x)

        # y-intercept
        self.b = left.y - (self.slope * left.x)


