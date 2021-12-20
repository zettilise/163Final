from generate_polygon import *
from make_monotone import *
import sys


if __name__=='__main__':
    num = int(input("Enter bounds: "))

    p = generate_polygon(-num, num)

    plt.figure(1)
    graph = make_mono(p)

    plt.figure(2)
    nx.draw(graph, nx.get_node_attributes(graph, 'pos'), with_labels=True, node_size=0)
    plt.show()