# This script deletes all nodes with duplicate numbers in a sorted linked list
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

    def dump(self):
        pnode = self
        while pnode != None:
            print ("({})".format(pnode.value), end = "")
            pnode = pnode.next
            if pnode != None:
                print("->", end = "")
            else:
                print()

class Solution():
    def __init__(self, alist, debug = False):
        self.input = None
        self.create_linklist(alist)
        self.head = None

    def create_linklist(self, alist):
        if alist == None or alist == []:
            return None
        else:
            self.input = prev = listNode(alist[0])

        for value in alist[1:]:
            prev.next = listNode(value)
            prev = prev.next

        if debug == True:
            self.input.dump()


    def solve(self):

        if self.input == None:
            return None
        elif self.input.next == None:
            return self.input

        prev = self.input
        state = "good"
        this = prev.next
        last = None

        while this != None:
            while this != None and prev.value == this.value:
                if debug == True:
                    print("found a dup = {}".format(prev.value))
                state = "skip"
                # skip until you find a different value or None
                prev = this
                this = prev.next

            if this == None:
                break
            elif state == "good":
                if self.head == None:
                    self.head = prev
                elif last != None:
                    last.next = prev

                last = prev

            prev = this
            this = prev.next
            state = "good"
            if debug == True:
                print("prev={}, this={}, last={}, state={}".format(prev, this, last, state))

        if last != None and last != prev:
            if state == "good":
                # include the last element
                last.next = prev
            else:
                # skip the remaining elements
                last.next = None

        # point the new head to have garbage collected for the skipped nodes
        self.input = self.head

        return self.head

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    alist = [1,1,2,2,3,3,3,3,4,5,6,6,6,6,7,8]

    sol = Solution(alist, debug)
    print ("TEST#{} Original linked list is: ".format(tno), end="")
    sol.input.dump()
    head = sol.solve()
    print ("TEST#{} De-dupped list is      : ".format(tno), end="")
    head.dump()

    tno += 1
    debug = False
    alist = [1,2,2,3,3,3,3,4,4,5,6,6,6,6,7,8,8,9]

    sol = Solution(alist, debug)
    print ("TEST#{} Original linked list is: ".format(tno), end="")
    sol.input.dump()
    head = sol.solve()
    print ("TEST#{} De-dupped list is      : ".format(tno), end="")
    head.dump()

    tno += 1
    debug = False
    alist = [1,2,2,3,3,3,3,4,4,5,6,6,6,6,7,8,8,9,9]

    sol = Solution(alist, debug)
    print ("TEST#{} Original linked list is: ".format(tno), end="")
    sol.input.dump()
    head = sol.solve()
    print ("TEST#{} De-dupped list is      : ".format(tno), end="")
    head.dump()

