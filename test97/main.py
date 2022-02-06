# This script adds two non-negative numbers stored in two linked lists where
# digits are stored in reverse order and each node contains a single digit.
# It returns the result as a reverse order linked list too.
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
class ListNode():
    def __init__(self, val):

        self.val = val
        self.next = None

    def clone(self):
        NList = ListNode(val)

        if self.next != None:
            NList.next = self.next.clone()

        return NList

class LinkedList():
    def __init__(self, alist):

        self.head = None
        prev = None

        for val in alist:
            lnode = ListNode(val)
            if not self.head:
                self.head = lnode
            else:
                prev.next = lnode
            prev = lnode

    def clone(self):
        newll = None

        if not self.head:
            return newll

        curnode = self.head
        while curnode:
            nnode = ListNode(curnode.val)
            if not newll:
                newll = nnode

            curnode = curnode.next

        return newll

    def print(self):
        curnode = self.head
        print("(",end="")
        while curnode:
            print("{}".format(curnode.val), end="")
            curnode = curnode.next
            if curnode:
                print("->", end="")
        print(")",end="")

class Solution():
    def addTwoNumbers(self, A, B):
        alist = []
        blist = []
        itrA = itrB = None
        alen = blen = 0
        tot = []

        if B == None:
            return A.clone() # clone the list
        else:
            itrB = B

        if A == None:
            return B.clone()
        else:
            itrA = A

        carry = 0
        linkTot = None
        lastNode = None
        # create alist with the digits in the linked list A
        while (itrA or itrB):
            valA = itrA.val if itrA else 0
            valB = itrB.val if itrB else 0
            valTot = valA + valB + carry
            carry = 1 if valTot>=10 else 0
            valTot = valTot % 10
            # print("valA = {} valB = {} valTot = {} carry = {}".format(valA, valB, valTot, carry))
            if not linkTot:
                linkTot = LinkedList([valTot])
                lastNode = linkTot.head
            else:
                lastNode.next = ListNode(valTot)
                lastNode = lastNode.next

            itrA = itrA.next if itrA else None
            itrB = itrB.next if itrB else None

        if carry == 1:
            lastNode.next = ListNode(carry)

        return linkTot

def test():

    sol = Solution()
    tnum = 0

    tnum += 1

    alist = [8, 4, 7, 9]
    blist = [6, 2, 5, 7, 7, 3]

    A = LinkedList(alist)
    B = LinkedList(blist)

    tot = sol.addTwoNumbers(A.head, B.head)

    print("TEST#{}: A is ".format(tnum), end="")
    A.print()
    print(" B is ", end="")
    B.print()
    print(" and A+B is ", end="")
    tot.print()
    print()

    tnum += 1

    alist = [9, 9, 9, 9, 9, 9, 9, 9, 9]
    blist = [9, 9, 9, 9, 9, 9]

    A = LinkedList(alist)
    B = LinkedList(blist)

    tot = sol.addTwoNumbers(A.head, B.head)

    print("TEST#{}: A is ".format(tnum), end="")
    A.print()
    print(" B is ", end="")
    B.print()
    print(" and A+B is ", end="")
    tot.print()
    print()

    tnum += 1

    alist = [9, 9, 9, 9, 9, 9, 9, 9, 9]
    blist = [1]

    A = LinkedList(alist)
    B = LinkedList(blist)

    tot = sol.addTwoNumbers(A.head, B.head)

    print("TEST#{}: A is ".format(tnum), end="")
    A.print()
    print(" B is ", end="")
    B.print()
    print(" and A+B is ", end="")
    tot.print()
    print()


if __name__ == '__main__':

    test()