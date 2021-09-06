# This script reorders a linked list L1->L2->...->LN-1->LN into L1->LN->L2->LN-1->...
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright (c) 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
class listNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList():
    def __init__(self, alist, debug = False):
        # keeps the original list
        self.alist = alist
        # keeps the pointers to list nodes
        self.olist = list()
        # head ot the linked list
        self.head = None
        # create the linked list
        self.create_linked_list()
        self.last = 0

    def create_linked_list(self):

        if (self.alist == None or self.alist == []):
            return

        # set the head
        self.head = prev = listNode(self.alist[0])

        for value in alist[1:]:
            prev.next = listNode(value)
            prev = prev.next

    def process(self, current):
        index = previndex = 0

        if current:
            self.last += 1
            index = self.last
            self.olist.append(current)
            self.process(current.next)

            # move the nodes after the midpoint
            if index > ((self.last + 1) >> 1):
                if debug:
                    print("processing node {} with value {}".format(current, current.value))
                # calculate the node to be set as the previous to this node
                previndex = self.last - index
                # set the next element as the precious node as this node
                self.olist[previndex].next = current
                # set the next node of this node as the next node of previndex node in the original object list
                current.next = self.olist[previndex+1]
                # set the next node of the previous element to None
                self.olist[index-1].next = None
        else:
            return

    def reorder(self):
        self.olist = list()
        self.last = -1

        if (not self.head):
            return

        self.process(self.head)


    def print(self):

        if (self.alist == None or self.alist == []):
            print("Nil", end="")

        current = self.head

        while current:
            print("({})".format(current.value), end="")
            current = current.next

            if current:
                print("->", end="")
        print()

if __name__ =="__main__":

    tno = 0

    tno +=1
    debug = False
    alist = None

    all = linkedList(alist)
    print("TEST#{} Original Linked List  : ".format(tno), end="")
    all.print()
    all.reorder()
    print("TEST#{} Reordered Linked List : ".format(tno), end="")
    all.print()

    tno +=1
    debug = False
    alist = []

    all = linkedList(alist)
    print("TEST#{} Original Linked List  : ".format(tno), end="")
    all.print()
    all.reorder()
    print("TEST#{} Reordered Linked List : ".format(tno), end="")
    all.print()

    tno +=1
    debug = False
    alist = [0]

    all = linkedList(alist)
    print("TEST#{} Original Linked List  : ".format(tno), end="")
    all.print()
    all.reorder()
    print("TEST#{} Reordered Linked List : ".format(tno), end="")
    all.print()

    tno +=1
    debug = False
    alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    all = linkedList(alist)
    print("TEST#{} Original Linked List  : ".format(tno), end="")
    all.print()
    all.reorder()
    print("TEST#{} Reordered Linked List : ".format(tno), end="")
    all.print()

    tno +=1
    debug = False
    alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    all = linkedList(alist)
    print("TEST#{} Original Linked List  : ".format(tno), end="")
    all.print()
    all.reorder()
    print("TEST#{} Reordered Linked List : ".format(tno), end="")
    all.print()

