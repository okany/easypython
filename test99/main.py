# This reverses a linked list partially between two values
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
'''
    creates a linked list from a list
    @type alist: list
    @param alist: the list to be converted into a linked list
    @returns head: the head of the new linked list
'''
def create_linked_list(alist):

    head = None # start with an empty list

    if alist == None or alist == []:
        pass # list is empty so return an empty linked list
    else:
        head = node(alist[0]) # create a node with the first element in the list
        for each in alist[1:]:
            head.add_node(each) # add the node to the linked list

    return head

'''
    creates a linked list in reverse order with data of a linked list
    @type node: node
    @param node: head of the linked list to be reversed
    @returns head: head of the reversed linked list
'''
def reverse_linked_list(node):

    head = None
    if node == None:
        pass
    else:
        head = node.reverse(None)

    return (head)

'''
    creates a list from a linked list
    @type node :node
    @param node : head of the linked list
'''
def create_list(node):
    alist = list()
    while node != None:
        alist.append(node.data)
        node = node.next
    return alist

'''
    a node of a linked list
'''
class node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_node(self, data):
        if data == None:
            pass
        elif self.next == None:
            self.next = node(data) # append a new node with the data
        else:
            self.next.add_node(data) # append node to linked list of the next node

    def reverse(self, prev):
        head = None
        if (self == None):
            # print("PASS")
            pass
        elif (self.next == None):
            # print("Next is none")
            head = self
            self.next = prev
        else:
            # print("Reverse next")
            head = self.next.reverse(self)
            self.next = prev

        return(head)


if __name__ == "__main__":

# TEST 1
    alist = [14,12,3,25,7,5,10,27,65,32,41,54,0,8]
    head = create_linked_list(alist)

    reversed = reverse_linked_list(head)
    reversed_list = create_list(reversed)

    print("TEST 1 - LIST = ", alist)
    print("REVERSED LIST = ", reversed_list)
    print()

# TEST 2
    alist = []
    head = create_linked_list(alist)

    reversed = reverse_linked_list(head)
    reversed_list = create_list(reversed)

    print("TEST 2 - LIST = ", alist)
    print("REVERSED LIST = ", reversed_list)
    print()

# TEST 3
    head = None

    reversed = reverse_linked_list(head)
    reversed_list = create_list(reversed)

    print("TEST 3   LIST = ", None)
    print("REVERSED LIST = ", reversed_list)
    print()

# TEST 4
    alist = [100]
    head = create_linked_list(alist)

    reversed = reverse_linked_list(head)
    reversed_list = create_list(reversed)

    print("TEST 5   LIST = ", alist)
    print("REVERSED LIST = ", reversed_list)
    print()

# TEST 6
    alist = [50, 75]
    head = create_linked_list(alist)

    reversed = reverse_linked_list(head)
    reversed_list = create_list(reversed)

    print("TEST 6   LIST = ", alist)
    print("REVERSED LIST = ", reversed_list)
    print()
