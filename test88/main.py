# This script partitions a linked list such that all nodes with a value
# less than X come before all nodes with value greater than or equal to X
# while preserving the relative order of nodes
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
class linkNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class linkList():
    def __init__(self, alist, x, debug = False):
        self.alist = alist
        self.x = x
        self.head = None
        self.create_link_list()

    def create_link_list(self):

        if self.alist == None or self.alist == []:
            return

        self.head = prev = linkNode(self.alist[0])
        for value in self.alist[1:]:
            prev.next = linkNode(value)
            prev = prev.next

    def partition(self):
        pivot = last = prev = None

        if self.head == None:
            return

        current = self.head
        while current:
            if current.value < self.x:
                if pivot:
                    # we found a lower one after the pivot so move this before the pivot
                    prev.next = current.next # skip this node
                    if last:
                        last.next = current # insert this after the last node before the pivot
                    else:
                        last = current
                        self.head = current

                    current.next = pivot # point the pivot as the next node

                last = current # set this node as the last node before the pivot
            else:
                if pivot:
                    # we found a node greater than X after the pivot just skip this
                    pass
                else:
                    pivot = current # set the pivot node

            prev = current
            current = current.next

    def print(self):

        if self.alist == None or self.alist == []:
            print("Nil", end="")

        current = self.head
        while current:
            print("({})".format(current.value), end="")
            current = current.next
            if current:
                print("->", end="")
        print()

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    alist = []
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()

    tno += 1
    debug = False
    alist = [4]
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()

    tno += 1
    debug = False
    alist = [1]
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()

    tno += 1
    debug = False
    alist = None
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()

    tno += 1
    debug = False
    alist = [1, 2, 2, 5, 4, 3, 2, 6, 1, 2, 8, 2]
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()

    tno += 1
    debug = False
    alist = [3, 1, 2, 2, 5, 4, 3, 2, 6, 1, 2, 8]
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()

    tno += 1
    debug = False
    alist = [1, 2, 2, 0, 1, 3, 2, 1, 2, 0, 2, 1]
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()

    tno += 1
    debug = False
    alist = [4, 5, 3, 4, 6, 7, 8, 3, 9, 8, 3, 4]
    x = 3

    all = linkList(alist, x, debug)
    print("-----------------------------------------------------------")
    print("TEST#{} Linked List             : ".format(tno), end="")
    all.print()
    all.partition()
    print("TEST#{} Partitioned Linked List : ".format(tno), end="")
    all.print()
