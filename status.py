"""
Basically a BBST, which is such a pain to code, so I just made it a list
and used binary search. 

Python lists are nice to work with for removing elements, and I'm not
working with big graphs, so runtime is passable. 
"""

# helps with binary search
from bisect import bisect_left, insort_left

from graph_struct import Edge

class Status:

    def __init__(self):
        self.list = []



    # binary search algo for this method was taken from https://www.techiedelight.com/binary-search/
    def find_nearest_edge_above(self, coord):
        """
        Given a y coord, find the nearest edge above it
        Binary search was buggy, so ended up just iterating through
        """
        
        x, y = coord
        index = 0

        for index, lower_line in enumerate(self.list[:-1]):
            y_low = lower_line.slope * x + lower_line.b 
            y_high = self.list[index + 1].slope * x + self.list[index + 1].b
            # print("testing ", lower_line, self.list[index + 1])
            if y_low <= y and y < y_high:

                # print('Returning', index + 1, self.list[index + 1])
                return self.list[index + 1]

        return self.list[index]


    def find_edge(self, e):
        """ 
        Given an edge , find the corresponding position in the list for
        it — basically binary search
        """
        
        index = bisect_left(self.list, e)
        if index >= len(self.list):
            index = len(self.list) - 1

        edge = self.list[index]

        if edge == e:
            return index
        else:
            # print(index, edge, e)
            # print(index - 1, self.list[index - 1])
            if e < edge:
                # print("less")
                while e != edge:
                    index -= 1
                    print(index)
                    edge = self.list[index]
                    print(edge)
                 
            else: 
                # print("greater")
                while e != edge:
                    index += 1
                    edge = self.list[index]
                    # print(edge)

        return index

    def insert_edge(self, e):
        """
        Inserts edge into Status DS
        This takes linear time b/c we're using a list
        """
        # print(type(e))
        # print("edges type in status insert" + e.helper)

        if self.list is []:
            self.list.append(e)
        else: 

            insort_left(self.list, e, lo=0, hi=len(self.list))
    
    def remove_edge(self, e):
        """
        Assumes edge exists, removes from list
        No sanity checks here

        Returns the edge so we can get good data
        """
        index = self.find_edge(e)
        edge = self.list[index]
        
        self.list.pop(index)

        # print("edges type in status" + edge.helper.type)
        return edge

    def __str__(self):
        return ', '.join([str(i) for i in self.list])
        # return "AHHHHH"

   