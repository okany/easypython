# This script merges two sorted linked lists
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

class linklist():
    def __init__(self, alist, debug = False):
        self.alist = alist
        self.head = None

        if (alist == None or alist == []):
            None
        else:
            self.head = prev = linkNode(self.alist[0])
            for value in alist[1:]:
                prev.next = linkNode(value)
                prev = prev.next

    def merge(self, bll):
        merged = list()
        blist = bll.head
        alist = self.head

        if blist == None:
            merged = self.head
        elif alist == None:
            merged = blist
        else:
            if(self.head.value <= blist.value):
                prev = merged = alist
                alist = alist.next
            else:
                prev = merged = blist
                blist = blist.next
            while alist and blist:
                if debug:
                    print("alist={} alist.value={} blist={} blist.value={} prev={} prev.value={}".
                          format(alist, alist.value, blist, blist.value, prev, prev.value))
                if alist.value <= blist.value:
                    prev.next = alist
                    alist = alist.next
                else:
                    prev.next = blist
                    blist = blist.next
                prev = prev.next


            if alist:
                prev.next = alist
            else:
                prev.next = blist

        self.head = merged

    def print(self):

        if self.head:
            current = self.head
            while current:
                print("({})".format(current.value), end="")
                current = current.next
                if current:
                    print("->", end="")
            print()
        else:
            print("Nil")

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    alist = [1, 3, 5, 10, 15, 19, 25]
    blist = [0, 4, 6, 10, 11, 12, 27, 29]

    all = linklist(alist, debug)
    bll = linklist(blist, debug)

    print("TEST#{} LIST A:".format(tno))
    all.print()
    print("LIST B:".format(tno))
    bll.print()

    all.merge(bll)
    print("MERGED:".format(tno))
    all.print()

    tno += 1
    debug = False
    alist = []
    blist = [0, 4, 6, 10, 11, 12, 27, 29]

    all = linklist(alist, debug)
    bll = linklist(blist, debug)

    print("LIST A:".format(tno))
    all.print()
    print("LIST B:".format(tno))
    bll.print()

    all.merge(bll)
    print("MERGED:".format(tno))
    all.print()

    tno += 1
    debug = False
    alist = [1, 3, 5, 10, 15, 19, 25]
    blist = None

    all = linklist(alist, debug)
    bll = linklist(blist, debug)

    print("LIST A:".format(tno))
    all.print()
    print("LIST B:".format(tno))
    bll.print()

    all.merge(bll)
    print("MERGED:".format(tno))
    all.print()

    tno += 1
    debug = False
    alist = [1, 3, 5, 10, 15, 19, 25]
    blist = [30, 40, 45]

    all = linklist(alist, debug)
    bll = linklist(blist, debug)

    print("LIST A:".format(tno))
    all.print()
    print("LIST B:".format(tno))
    bll.print()

    all.merge(bll)
    print("MERGED:".format(tno))
    all.print()

    tno += 1
    debug = False
    alist = [50, 55, 56]
    blist = [30, 40, 45]

    all = linklist(alist, debug)
    bll = linklist(blist, debug)

    print("LIST A:".format(tno))
    all.print()
    print("LIST B:".format(tno))
    bll.print()

    all.merge(bll)
    print("MERGED:".format(tno))
    all.print()
