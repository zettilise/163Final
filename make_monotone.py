import numpy as np

from graph_struct import * 
from stopping_points import *
from status import Status
from generate_polygon import *
from matplotlib.animation import FuncAnimation

# Status DS. It's global. It's spaghetti code.
status = Status()


def make_mono(v):
    if v.x < v.v_prev.x:
        if v.x < v.v_next.x:
    
            if Edge(v, v.v_next) < Edge(v, v.v_prev):
                # Start vertex
                v.type = "start"

                # lower edge of v
                status.insert_edge(Edge(v, v.v_next))

                # Upper edge of v
                edge = Edge(v, v.v_prev)
                edge.helper = v
           
                status.insert_edge(edge) # Upper edge

            else:
                # split vertex
                v.type = "split"
               

                edge = status.find_nearest_edge_above(v.coord)
             
                graph.add_edge(v.name, edge.helper.name, color='r')

                index = status.find_edge(edge)
                # put 3 edges into status
               
                status.list[index].helper = v
                
                edge_below = Edge(v, v.v_prev)
                edge_below.helper = v
               
                status.insert_edge(edge_below)

                status.insert_edge(Edge(v, v.v_next))

                

        else:
            # upper vertex
            v.type = "upper"
           

            # Remove left edge, connect to merge vertex if it exists
            edge_next = status.remove_edge(Edge(v, v.v_next))
            

            if edge_next.helper is not None and edge_next.helper.type == "merge":
                graph.add_edge(v.name, edge_next.helper.name, color='r')

            # V becomes helper of new edge (prev)
            edge_new = Edge(v, v.v_prev)
            edge_new.helper = v
          
            status.insert_edge(edge_new)

    else:
        if v.x < v.v_next.x:
            # lower vertex
            v.type = "lower"
           
            # find edge immediately above v
            edge = status.find_nearest_edge_above(v.coord)

            # Fix helper if necessary 
            if edge.helper is not None and edge.helper.type == "merge":
           
                graph.add_edge(v.name, edge.helper.name, color='r')

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

                # fix lower edge (next)
                index = status.find_edge(Edge(v, v.v_next))
                edge_next = status.list[index]
                if edge_next.helper is not None and edge_next.helper.type == "merge":
                    graph.add_edge(v.name, edge_next.helper.name, color='r')


                # delete edges
                edge_next = status.remove_edge(edge_next)
                edge_prev = status.remove_edge(Edge(v, v.v_prev))

                # find edge above and fix if necessary 
                edge = status.find_nearest_edge_above(v.coord)
                
                if edge.helper is not None and edge.helper.type == "merge":
                    graph.add_edge(v.name, edge.helper.name, color='r')
                # attempting to redirect edge above to merge now
                index = status.find_edge(edge)
                status.list[index].helper = v


                

            else:
                # end vertex
                v.type = "end"
                

                # upper edge, which is (next)
                index = status.find_edge(Edge(v, v.v_next))
                edge_next = status.list[index]

                if edge_next.helper is not None and edge_next.helper.type == "merge":
                    graph.add_edge(v.name, edge_next.helper.name, color='r')

                # delete upper and lower
                edge_next = status.remove_edge(edge_next)
                edge_prev = status.remove_edge(Edge(v, v.v_prev))


    # This is what plots the line and edges at a given moment. 
    vert.set_data(plotVert(v.x))
    colors = nx.get_edge_attributes(graph,'color').values()
    nx.draw(graph, nx.get_node_attributes(graph, 'pos'), with_labels=True, node_size=1, edge_color=colors,)


# Borrowed from online.... can't recall the source :(
def plotVert(x):
        """ Plots a vertical line at the given x-coordinate"""
        x_vals = [x, x]
        y_vals = [-100, 100]
        return (x_vals, y_vals)



""" Code for running the project in General. """

# Gets the bounding box limits. 
num = int(input("Enter bounds: "))


fig = plt.figure()
p = generate_polygon(-num, num)
graph = p.graph
vert, = plt.plot([], [], 'k-.')

stopping = get_stopping_points(p.vertices)

# This is what iterates through the stopping points data structure. 
# This is also what allows us to have animations. 
anim = FuncAnimation(fig, make_mono,frames=stopping, init_func=lambda : ..., interval=500, repeat=False)

# Can toggle between these two, probably not on the hw server tho. 
anim.save('sweep.gif', fps=5)
# plt.show()



