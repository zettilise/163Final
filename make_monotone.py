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
       
        # print(v.name, " is the current node")
        if v.x < v.v_prev.x:
            if v.x < v.v_next.x:
                # print("Test print ", v.v_next.y, v.v_prev.y)
                # if v.v_next.y < v.v_prev.y:
                if Edge(v, v.v_next) < Edge(v, v.v_prev):
                    # Start vertex
                    v.type = "start"
                    # print("in start", v.type)

                    # lower edge of v
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

                    edge = status.find_nearest_edge_above(v.coord)
                    # edge = status.list[index]
                    # print(index)
                    # print(edge)
                    # print("names of edges we connect ", v.name, edge.helper.name)
                    graph.add_edge(v.name, edge.helper.name)

                    index = status.find_edge(edge)
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

                # Remove left edge, connect to merge vertex if it exists
                edge_next = status.remove_edge(Edge(v, v.v_next))
                # print("edge removed in upper, ", edge_next)

                if edge_next.helper is not None and edge_next.helper.type == "merge":
                    graph.add_edge(v.name, edge_next.helper.name )

                # V becomes helper of new edge (prev)
                edge_new = Edge(v, v.v_prev)
                edge_new.helper = v
                # print(edge_new.helper.type)
                status.insert_edge(edge_new)

        else:
            if v.x < v.v_next.x:
                # lower vertex
                v.type = "lower"
                # print("in lower")


                # find edge immediately above v
                edge = status.find_nearest_edge_above(v.coord)

                # Fix helper if necessary 
                if edge.helper is not None and edge.helper.type == "merge":
                # if edge.helper is not None:
                    # print("Need to fix in lower")
                    graph.add_edge(v.name, edge.helper.name )

                # Trying a thing to redirect helper
                index = status.find_edge(edge)
                status.list[index].helper = v

                # Replace left edge ( prev)
                edge_next = Edge(v, v.v_next)
                edge_next.helper = v
                index = status.find_edge(Edge(v, v.v_prev))
                status.list[index] = edge_next

         

            else:
                # if v.v_next.y < v.v_prev.y:
                if Edge(v, v.v_next) < Edge(v, v.v_prev):
                    # merge vertex
                    v.type = "merge"
                    # print("in merge")

                    # fix lower edge (next)
                    index = status.find_edge(Edge(v, v.v_next))
                    edge_next = status.list[index]
                    if edge_next.helper is not None and edge_next.helper.type == "merge":
                        graph.add_edge(v.name, edge_next.helper.name )


                    # delete edges
                    edge_next = status.remove_edge(edge_next)
                    edge_prev = status.remove_edge(Edge(v, v.v_prev))

                    # find edge above and fix if necessary 
                    edge = status.find_nearest_edge_above(v.coord)
                    # print("helper found for merge is ", edge.helper)
                    if edge.helper is not None and edge.helper.type == "merge":
                        graph.add_edge(v.name, edge.helper.name )
                    # attempting to redirect edge above to merge now
                    index = status.find_edge(edge)
                    status.list[index].helper = v


                    

                else:
                    # end vertex
                    v.type = "end"
                    # print("in end", v.name)
                    # print(v.v_prev.name, v.v_next.name)

                    # upper edge, which is (next)
                    index = status.find_edge(Edge(v, v.v_next))
                    edge_next = status.list[index]

                    if edge_next.helper is not None and edge_next.helper.type == "merge":
                        graph.add_edge(v.name, edge_next.helper.name )

                    # delete upper and lower
                    edge_next = status.remove_edge(edge_next)
                    edge_prev = status.remove_edge(Edge(v, v.v_prev))


        # print("Current: ", status)

    return graph
