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
        """
        (l, r) = (0, len(self.list) - 1)

        x, y = coord

        # loop till the search space is exhausted
        while l <= r:
    
            # find the mid-value in the search space and
            # compares it with the target
    
            mid = (l + r) // 2
    
            # overflow can happen. Use:
            # mid = left + (right - left) / 2
            # mid = right - (right - left) // 2
    
            # target is found
            edge_val = self.list[mid]
            middle = edge_val.slope * x + edge_val.b

            if y == middle:
                return mid
    
            # discard all elements in the right search space,
            # including the middle element
            elif y < middle:
                r = mid - 1
    
            # discard all elements in the left search space,
            # including the middle element
            else:
                l = mid + 1
    
        # `target` doesn't exist in the list
        return -1



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
            print(index, edge, e)
            # print(index - 1, self.list[index - 1])
            if e < edge:
                print("less")
                while e != edge:
                    index -= 1
                    print(index)
                    edge = self.list[index]
                    print(edge)
                 
            else: 
                print("greater")
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

   