# This script swaps all two adjacent nodes in a linked list and returns its head
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
    def __init__(self, alist, debug = False):
        self.alist = alist
        self.head = None
        self.create_list()

    def create_list(self):

        self.head = None

        if self.alist == None or self.alist == []:
            return

        self.head = prev = linkNode(self.alist[0])
        for value in alist[1:]:
            prev.next = linkNode(value)
            prev = prev.next

    def print(self):
        if self.head == None:
            print("Nil")
        else:
            current = self.head
            while current:
                print("({})".format(current.value), end="")
                current = current.next
                if current:
                    print("->", end="")
            print()

    def swap_nodes(self):

        newfirst = newsecond = prev = next = None
        first = self.head

        while first and first.next:
            newfirst = first.next
            newsecond = first
            if prev:
                prev.next = newfirst
            else:
                self.head = newfirst
            prev = newsecond
            next = newfirst.next
            newfirst.next = newsecond
            newsecond.next = first = next

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = True
    alist = [1, 2, 3, 4, 6, 9, 3, 2, 1, 9, 8]

    all = linkList(alist, debug)
    print("TEST#{} Linked List         : ".format(tno), end="")
    all.print()
    all.swap_nodes()
    print("TEST#{} Swapped Linked List : ".format(tno), end="")
    all.print()
    print("-------------------------------------------------------------")

    tno += 1
    debug = True
    alist = []

    all = linkList(alist, debug)
    print("TEST#{} Linked List         : ".format(tno), end="")
    all.print()
    all.swap_nodes()
    print("TEST#{} Swapped Linked List : ".format(tno), end="")
    all.print()
    print("-------------------------------------------------------------")

    tno += 1
    debug = True
    alist = [1]

    all = linkList(alist, debug)
    print("TEST#{} Linked List         : ".format(tno), end="")
    all.print()
    all.swap_nodes()
    print("TEST#{} Swapped Linked List : ".format(tno), end="")
    all.print()
    print("-------------------------------------------------------------")

    tno += 1
    debug = True
    alist = [1, 2, 3, 4, 6, 9, 3, 2, 1, 9, 8, 10]

    all = linkList(alist, debug)
    print("TEST#{} Linked List         : ".format(tno), end="")
    all.print()
    all.swap_nodes()
    print("TEST#{} Swapped Linked List : ".format(tno), end="")
    all.print()
    print("-------------------------------------------------------------")



