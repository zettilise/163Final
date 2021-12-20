"""
File containing classes defined Vertices and Edges in Graph
By Zetty Cho

I am very much not obeying Python naming conventions.... I just want
this to work ;-;

"""
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


    def add_vertex(self, v):
        v.v_prev = self.head.v_prev 
        self.head.v_prev.v_next = v 

        v.v_next = self.head 
        self.head.v_prev = v 
        self.vertices.append(v)


    # def print_vertices(obj):
    #     print(obj.head)
    #     curr_vertex = obj.head.v_next

    #     while curr_vertex != obj.head:
    #         print(curr_vertex)
    #         curr_vertex = curr_vertex.v_next



class Vertex:

    def __init__(self, x, y):
        """
        Defines vertex by x and y coordinate. 
        In this program each vertex will only have two edges.
        Initializes edges to be None
        """
        self.x = x
        self.y = y

        # These are specifically for the polygon
        self.v_next = None          # vertex coming in from ccw direction
        self.v_prev = None          # vertex exiting from ccw direction

        # This is for the DCEL
        self.edges = []

    # def print_vertex(obj):
    #     print("(",  obj.x,  ",", obj.y, ")")

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



