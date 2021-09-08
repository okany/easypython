# This script sorts a linked list by using insertion sort
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

class linkedList():
    def __init__(self, alist, debug = False):
        self.alist = alist
        self.debug = debug
        self.head = None
        self.create_linked_list()

    def create_linked_list(self):

        if(not self.alist or self.alist == []):
            return None

        self.head = prev = linkNode(self.alist[0])

        for value in self.alist[1:]:
            prev.next = linkNode(value)
            prev = prev.next

    def insertion_sort(self):

        iter = 0
        if(not self.head or not self.head.next):
            return

        current = self.head.next
        # disconnect the link lists to simplify the solution
        self.head.next = None

        while current:
            next = current.next
            if current.value <= self.head.value:
                current.next = self.head
                self.head = current
            else:
                newprev = self.head
                newnext = self.head.next
                while newnext:

                    if current.value <= newnext.value:
                        current.next = newnext
                        newprev.next = current
                        break
                    else:
                        newprev = newnext
                        newnext = newnext.next

                if not newnext:
                    current.next = None
                    newprev.next = current
            if debug:
                print("Iteration#{}: ".format(iter), end="")
                self.print()
            iter += 1
            current = next

    def print(self):

        if self.head == None:
            print("Nil", end="")
        else:

            current = self.head
            while current:
                print("({})".format(current.value),end ="")
                current = current.next
                if current:
                    print("->",end="")

        print()

if __name__=="__main__":

    tno = 0

    print("----------------------------------------------------------------")
    tno += 1
    debug = False
    alist = None

    ll = linkedList(alist, debug)

    print("TEST#{} Original Linked List : ".format(tno), end="")
    ll.print()

    ll.insertion_sort()
    print("TEST#{} Sorted Linked List   : ".format(tno), end="")
    ll.print()
    print("----------------------------------------------------------------")

    tno += 1
    debug = False
    alist = [1]

    ll = linkedList(alist, debug)

    print("TEST#{} Original Linked List : ".format(tno), end="")
    ll.print()

    ll.insertion_sort()
    print("TEST#{} Sorted Linked List   : ".format(tno), end="")
    ll.print()
    print("----------------------------------------------------------------")

    tno += 1
    debug = False
    alist = [1, 2]

    ll = linkedList(alist, debug)

    print("TEST#{} Original Linked List : ".format(tno), end="")
    ll.print()

    ll.insertion_sort()
    print("TEST#{} Sorted Linked List   : ".format(tno), end="")
    ll.print()
    print("----------------------------------------------------------------")

    tno += 1
    debug = False
    alist = [5, 2, 3, 6]

    ll = linkedList(alist, debug)

    print("TEST#{} Original Linked List : ".format(tno), end="")
    ll.print()

    ll.insertion_sort()
    print("TEST#{} Sorted Linked List   : ".format(tno), end="")
    ll.print()
    print("----------------------------------------------------------------")

    tno += 1
    debug = False
    alist = [6, 5, 4, 3, 2, 1, 0]

    ll = linkedList(alist, debug)

    print("TEST#{} Original Linked List : ".format(tno), end="")
    ll.print()

    ll.insertion_sort()
    print("TEST#{} Sorted Linked List   : ".format(tno), end="")
    ll.print()
    print("----------------------------------------------------------------")

