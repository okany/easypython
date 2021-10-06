# This script finds the middle node in a linked list in one pass
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

def create_linkedlist(alist):
    if (alist == None or alist == []):
        return None
    else:
        head = linkedlist(alist[0])
        head.next = create_linkedlist(alist[1:])

    return head

def find_middle(ll):
    lldict = dict()
    if ll == None: return None
    else:
        node = ll
        index = 0
        while node:
            lldict[index] = node
            node = node.next
            index = index + 1

    size = index
    middle = int(size/2)

    return(lldict[middle])

class linkedlist():
    def __init__(self, data):
        self.data = data
        self.next = None

    def tolist(self):
        alist = []
        item = self
        while item:
            alist.append(item.data)
            item = item.next

        return alist

if __name__ == "__main__":
    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","d","s","g","g","d","f","g","d","f","f","g","h","j","f","g","h","j","g","h","j"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j","q"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist([])
    print("middle item in the list {} is {}".format(ml, find_middle(ml)))

    ml = create_linkedlist([1])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))
