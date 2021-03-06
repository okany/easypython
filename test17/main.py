# this script finds the nth node from the end in a singly linked list
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
    if(alist == None or alist == []):
        return None
    else:
        llist = linkedlist(alist[0])
        llist.setnext(createlinkedlist(alist[1:]))
        return llist

class linkedlist():
    def __init__(self, data):
        self.next = None
        self.data = data

    def setnext(self, next):
        self.next = next

    def setdata(self, data):
        self.data = data
        
    def tolist(self):
        alist = []
        trv = self
        while trv != None:
            alist.append(trv.data)
            trv = trv.next

        return alist

    def enditem(self, num):

        if(num <= 0): return None

        numlist = []
        trv  = self
        for i in range(num):
            if(trv is None):
                return(None)
            else:
                numlist.append(trv.data)
                trv = trv.next
        while trv != None:
            numlist.append(trv.data)
            numlist.pop(0)
            trv = trv.next

        return(numlist[0])

if __name__ == '__main__':
    ml = createlinkedlist(["a","s","d","a","s","d","a","s","f","d","s","g","g","d","f","g","d","f","f","g","h","j","f","g","h","j","g","h","j"])
    nth = 9
    print("{}th item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

    ml = createlinkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    nth = 6
    print("{}th item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

    ml = createlinkedlist([])
    nth = 6
    print("{}th item from the end of list {} is {}".format(nth, ml, ml))

    ml = createlinkedlist([1])
    nth = 1
    print("{}st item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

    ml = createlinkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    nth = 0
    print("{}th item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

