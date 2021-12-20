from generate_polygon import *
from make_monotone import *
import sys


if __name__=='__main__':
    num = int(input("Enter bounds: "))

    p = generate_polygon(-num, num)

    graph = make_mono(p)
    colors = nx.get_edge_attributes(graph,'color').values()

    plt.figure(1)
    nx.draw(graph, nx.get_node_attributes(graph, 'pos'), with_labels=True, node_size=1, edge_color=colors,)
    plt.show()