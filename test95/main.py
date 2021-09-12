# This script finds the intersection of two linked lists in O(N) time and O(1) memory
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
    def __init__(self, llist, debug = False):
        self.llist = llist
        self.debug = debug
        self.head = self.create_linked_list()
        if self.debug:
            self.print()

    def create_linked_list(self):
        head = None

        if self.llist == None or self.llist == []:
            pass
        else:
            head = prev = linkNode(self.llist[0])
            if self.debug:
                print("({})".format(head.value), end="")

            for item in self.llist[1:]:
                if self.debug:
                    print("->", end="")
                prev.next = linkNode(item)
                prev = prev.next
                if self.debug:
                    print("({})".format(prev.value), end="")

        return head

    def append_list(self, list2):
        if self.head == None:
            self.head = list2.head
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = list2.head

    def print(self):

        current = None
        if self.head == None:
            print("Nil", end="")
        else:
            current = self.head
            while current:
                print("({})".format(current.value), end ="")
                current = current.next
                if(current):
                    print("->", end="")

        print()

class intersection():
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.len1 = self.len(list1)
        self.len2 = self.len(list2)

    def len(self, alist):
        length = 0
        current = alist.head
        while current:
            current = current.next
            length += 1

        return length

    def intersect(self):
        ind1 = ind2 = 0
        current1 = self.list1.head
        current2 = self.list2.head
        if(self.len1 > self.len2):
            dif = self.len1 - self.len2
            while dif != 0:
                current1 = current1.next
                dif -= 1
        elif(self.len1 < self.len2):
            dif = self.len2 - self.len1
            while dif != 0:
                current2 = current2.next
                dif -= 1

        while current1 and current2:
            if current1.value == current2.value:
                # we found the intersection node
                return current1.value
            else:
                current1 = current1.next
                current2 = current2.next

        # current1 and current2 must be Nil
        return None

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    l1 = [1, 2, 3, 4, 5]
    l2 = [15, 14, 13, 12]
    lint = [6, 7, 8, 9, 10, 11]

    ll1 = linkedList(l1, debug)
    ll2 = linkedList(l2, debug)
    llint = linkedList(lint, debug)

    ll1.append_list(llint)
    ll2.append_list(llint)

    print("------------------------------------------------------------")
    print("TEST#{} List #1:".format(tno))
    ll1.print()

    print("TEST#{} List #2:".format(tno))
    ll2.print()

    inter = intersection(ll1, ll2)

    print("TEST#{} intersection = {}".format(tno, inter.intersect()))
    print("------------------------------------------------------------")

    tno += 1
    debug = False
    l1 = [2, 3]
    l2 = [15, 14, 13, 12]
    lint = [7, 8, 9, 10, 11]

    ll1 = linkedList(l1, debug)
    ll2 = linkedList(l2, debug)
    llint = linkedList(lint, debug)

    ll1.append_list(llint)
    ll2.append_list(llint)

    print("TEST#{} List #1:".format(tno))
    ll1.print()

    print("TEST#{} List #2:".format(tno))
    ll2.print()

    inter = intersection(ll1, ll2)

    print("TEST#{} intersection = {}".format(tno, inter.intersect()))
    print("------------------------------------------------------------")

    tno += 1
    debug = False
    l1 = []
    l2 = [15, 14, 13, 12]
    lint = [5, 6, 7, 8, 9, 10, 11]

    ll1 = linkedList(l1, debug)
    ll2 = linkedList(l2, debug)
    llint = linkedList(lint, debug)

    ll1.append_list(llint)
    ll2.append_list(llint)

    print("TEST#{} List #1:".format(tno))
    ll1.print()

    print("TEST#{} List #2:".format(tno))
    ll2.print()

    inter = intersection(ll1, ll2)

    print("TEST#{} intersection = {}".format(tno, inter.intersect()))
    print("------------------------------------------------------------")

    tno += 1
    debug = False
    l1 = [5, 6, 7, 8]
    l2 = [15, 16, 17, 18]
    lint = [9, 10, 11, 12, 13, 14]

    ll1 = linkedList(l1, debug)
    ll2 = linkedList(l2, debug)
    llint = linkedList(lint, debug)

    ll1.append_list(llint)
    ll2.append_list(llint)

    print("TEST#{} List #1:".format(tno))
    ll1.print()

    print("TEST#{} List #2:".format(tno))
    ll2.print()

    inter = intersection(ll1, ll2)

    print("TEST#{} intersection = {}".format(tno, inter.intersect()))
    print("------------------------------------------------------------")

    tno += 1
    debug = False
    l1 = [1, 2, 3, 4, 5, 6, 7, 8]
    l2 = [15, 14, 13, 12]
    lint = []

    ll1 = linkedList(l1, debug)
    ll2 = linkedList(l2, debug)
    llint = linkedList(lint, debug)

    ll1.append_list(llint)
    ll2.append_list(llint)

    print("TEST#{} List #1:".format(tno))
    ll1.print()

    print("TEST#{} List #2:".format(tno))
    ll2.print()

    inter = intersection(ll1, ll2)

    print("TEST#{} intersection = {}".format(tno, inter.intersect()))
    print("------------------------------------------------------------")

