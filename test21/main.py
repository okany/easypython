# This script reverses a singly linked list
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

def createlinkedlist(alist):
    if alist == None or alist == []:
        return None

    llist = linkedlist(alist[0])
    trv = llist
    for item in alist[1:]:
        trv.next = linkedlist(item)
        trv = trv.next
    return llist

def rec_reverse(ll):

    rev = head = None
    if ll == None: pass
    elif ll.next == None:
        rev =  head = linkedlist(ll.data)
    else:
        rev, head = rec_reverse(ll.next)
        rev.next = linkedlist(ll.data)
        rev = rev.next

    return rev, head

class linkedlist():
    def __init__(self, data):
        self.data = data
        self.next = None

    def setnext(self, ll):
        self.next = ll

    def sefdata(self, data):
        self.data = data

    def reverse(self):
        if(self == None):
            rev = None
        else:
            trv = self
            rev = prev = linkedlist(self.data)
            while trv.next:
                next = linkedlist(trv.next.data)
                next.setnext(prev)
                rev = prev = next
                trv = trv.next

        return rev

    def tolist(self):
        alist = []
        trv = self

        while trv != None:
            alist.append(trv.data)
            trv = trv.next
        return(alist)

if __name__ == "__main__":

    alist = ["a", "s", "d", "a", "s", "d", "a", "s", "f", "d", "s", "g", "g", "d", "f", "g", "d", "f", "f", "g", "h", "j",
         "f", "g", "h", "j", "g", "h", "j"]
    ml = createlinkedlist(alist)

    print("reverse of list           {} is {}".format(ml.tolist(), ml.reverse().tolist()))
    rev, head = rec_reverse(ml)
    print("recursive reverse of list {} is {}".format(alist, head.tolist()))

    ml = createlinkedlist(["a", "s", "d", "a", "s", "d", "a", "s", "f", "g", "h", "j", "g", "h", "j"])
    print("reverse of list {} is {}".format(ml.tolist(), ml.reverse().tolist()))

    ml = createlinkedlist([])
    print("reverse of list {} is {}".format(ml, ml))

    ml = createlinkedlist([1])
    print("reverse of list {} is {}".format(ml.tolist(), ml.reverse().tolist()))

    ml = createlinkedlist(["a", "s", "d", "a", "s", "d", "a", "s", "f", "g", "h", "j", "g", "h", "j"])
    print("reverse of list {} is {}".format(ml.tolist(), ml.reverse().tolist()))
