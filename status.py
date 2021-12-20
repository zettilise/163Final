"""
Basically a BBST, which is such a pain to code, so I just made it a list
and used binary search. 

Python lists are nice to work with for removing elements, and I'm not
working with big graphs, so runtime is passable. 
"""

# helps with binary search
from bisect import bisect_left, insort_left

class Status:

    def __init__(self):
        self.list = []


    def find_edge(self, e):
        """ 
        Given a coordinate, find the corresponding position in the list for
        it — basically binary search
        """
        
        index = bisect_left(self.list, e)

        return index

    def insert_edge(self, e):
        """
        Inserts edge into Status DS
        This takes linear time b/c we're using a list
        """

        if self.list is []:
            self.list.append(e)
        else: 
            x = e.left.x

            insort_left(self.list, e, lo=0, hi=len(self.list))
    
    def remove_edge(self, e):
        """
        Assumes edge exists, removes from list
        """
        index = self.find_edge(e)
        self.list.pop(index)

    def __str__(self):
        return ', '.join([str(i) for i in self.list])
        # return "AHHHHH"

   