import numpy as np

from graph_struct import * 
from stopping_points import *
from status import Status



def make_mono(poly):
    """
    EEEEEEEEEEEE
    
    Please make monotone :(
    
    """
    graph = poly.graph
    stopping = get_stopping_points(poly.vertices)

    status = Status()

    # This loop takes each vertex in the stopping points DS and processes it
    for v in stopping:
       
        print(v.name, " is the current node")
        if v.x < v.v_prev.x:
            if v.x < v.v_next.x:
                # print("Test print ", v.v_next.y, v.v_prev.y)
                # if v.v_next.y < v.v_prev.y:
                if Edge(v, v.v_next) < Edge(v, v.v_prev):
                    # Start vertex
                    v.type = "start"
                    # print("in start", v.type)
                    status.insert_edge(Edge(v, v.v_next))

                    # Upper edge of v
                    edge = Edge(v, v.v_prev)
                    edge.helper = v
                    # print(edge.helper.type)
                    status.insert_edge(edge) # Upper edge

                else:
                    # split vertex
                    v.type = "split"
                    # print("in split")

                    index = status.find_nearest_edge_above(v.coord)
                    edge = status.list[index]
                    # print(index)
                    # print(edge)
                    # print(edge.helper.name)
                    graph.add_edge(v.name, edge.helper.name )

                    # put 3 edges into status
                    # edge.helper = v
                    status.list[index].helper = v
                    # print(edge.helper.type)
                    # status.insert_edge(edge)
                    edge_below = Edge(v, v.v_prev)
                    edge_below.helper = v
                    # print("here ",edge_below.helper.type)
                    status.insert_edge(edge_below)

                    status.insert_edge(Edge(v, v.v_next))

                    

            else:
                # upper vertex
                v.type = "upper"
                # print("in upper")
                edge_next = status.remove_edge(Edge(v, v.v_next))

                if edge_next.helper is not None and edge_next.helper.type == "merge":
                    graph.add_edge(v.name, edge_next.helper.name )

                # v becomes helper of new edge (prev)
                edge_new = Edge(v, v.v_prev)
                edge_new.helper = v
                # print(edge_new.helper.type)
                status.insert_edge(edge_new)

        else:
            if v.x < v.v_next.x:
                # lower vertex
                v.type = "lower"
                print("in lower")

                # fix v, e, where e is v.v_prev with v
                # swap edges
                edge_find = Edge(v, v.v_prev)
                index = status.find_edge(edge_find)
                edge_prev = status.remove_edge(edge_find)
                index2 = status.find_nearest_edge_above(v.coord)
                edge = status.list[index2]
                # print("should find edge", edge)
                # print("checking " + edge_prev.helper)
                # print("edge helper", edge.helper.name, edge.helper.type)
                if edge.helper is not None and edge.helper.type == "merge":
                # if edge.helper is not None:
                    # print("Need to fix in lower")
                    graph.add_edge(v.name, edge.helper.name )

                # v becomes helper of new edge (next)
                edge_new = Edge(v, v.v_next)
                edge_new.helper = v
                # print(edge_new.helper.type)
                status.insert_edge(edge_new)

            else:
                # if v.v_next.y < v.v_prev.y:
                if Edge(v, v.v_next) < Edge(v, v.v_prev):
                    # merge vertex
                    v.type = "merge"
                    print("in merge")

                    # above
                    edge_prev = status.remove_edge(Edge(v, v.v_prev)) 
                    index = status.find_nearest_edge_above(v.coord)
                    edge = status.list[index]
                    print("merge found ", edge)
                    # print("test " + edge.helper.type)

                    # status.list[index].helper = v

                    

                    if edge.helper is not None and edge.helper.type == "merge":
                        graph.add_edge(v.name, edge.helper.name )
                    
                    # status.list[index].helper = v

                    # below
                    edge_next = status.remove_edge(Edge(v, v.v_next))

                    if edge_next.helper is not None and edge_next.helper.type == "merge":
                        graph.add_edge(v.name, edge_next.helper.name )

                    
                    # Debugging, make this vertex the helper of edge
                    # status.list[index].helper = v

                else:
                    # end vertex
                    v.type = "end"
                    # print("in end", v.name)
                    # print(v.v_prev.name, v.v_next.name)

                    # upper
                    edge_next = status.remove_edge(Edge(v, v.v_next))
                    if edge_next.helper is not None and edge_next.helper.type == "merge":
                        graph.add_edge(v.name, edge_next.helper.name )

                    # lower
                    edge_prev = status.remove_edge(Edge(v, v.v_prev))


        print("Current: ", status)

    return graph
