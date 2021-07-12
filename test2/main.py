# This script implements preorder, inorder, and postorder traversal of a binary tree with and without using recursion
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

def create_tree(alist):
    if alist == None: return None
    else:
        bt = btree(alist[0])
        for item in alist[1:]:
            bt.insert(item)
    return bt

class btree():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            pass # duplicate - don't insert
        elif self.data > data:
            if(self.left == None):
                # create a new node as a left child
                self.left = btree(data)
            else:
                # insert to left branch
                self.left.insert(data)
        else:
            if(self.right == None):
                # create a new node as a right child
                self.right = btree(data)
            else:
                # insert to right branch
                self.right.insert(data)

    def find(self, data):
        if self.data == data:
            return data # we found it
        elif self.data > data:
            if(self.left == None):
                return None # does not exists
            else:
                # search in the left branch
                return self.left.find(data)
        else:
            if(self.right == None):
                return None # does not exists
            else:
                # search in the right branch
                return self.right.find(data)

    def inorder_list(self):
        ilist = []
        if(self.left != None):
            ilist.extend(self.left.inorder_list())
        ilist.append(self.data)
        if(self.right != None):
            ilist.extend(self.right.inorder_list())

        return(ilist)


    def nr_inorder_list(self):
        ilist = [self]
        item = self
        i = 0
        leftdone = False
        while True:
            if(leftdone == False and item.left != None):
                ilist.insert(i, item.left)
                item = item.left
            elif (item.right != None):
                i = i + 1
                ilist.insert(i, item.right)
                # evaluate the right branch
                item = item.right
                leftdone = False
            else:
                i = i + 1
                if(i<len(ilist)):
                    # move to the parent node to look for right branch
                    item = ilist[i]
                    # don't search the left branch on the parent node
                    leftdone = True
                else:
                    #this is the rightmost item so stop the search
                    break
        dlist = []
        for item in ilist:
            # create the data list from list of linked list items
            dlist.append(item.data)

        return dlist

    def nr_preorder_list(self):
        ilist = [self]
        item = self
        i = 0
        while True:
            if(item.right != None):
                # insert the right node
                ilist.insert(i+1, item.right)
            if (item.left != None):
                # insert the left node before the right node
                ilist.insert(i+1, item.left)
            i = i + 1 # move pointer to the next node
            if(i<len(ilist)):
                # move to the next node in the list
                item = ilist[i]
            else:
                # this is the rightmost item so stop the search
                break

        dlist = []
        for item in ilist:
            # create the data list from list of linked list items
            dlist.append(item.data)

        return dlist

    def nr_postorder_list(self):
        ilist = [self]
        item = self
        i = 0
        while True:
            if (item.left != None):
                # insert the left
                ilist.insert(i, item.left)
                i = i + 1 # move the pointer back to the parent node
            if(item.right != None):
                # insert the right node
                ilist.insert(i, item.right)
                i = i + 1 # move the pointer back to the parent node

            i = i - 1 # move pointer to the previous node
            if(i>=0):
                # move to the previous node in the list
                item = ilist[i]
            else:
                # this is the leftmost item so stop the search
                break

        dlist = []
        for item in ilist:
            # create the data list from list of linked list items
            dlist.append(item.data)

        return dlist

    def preorder_list(self):
        plist = [self.data]
        if(self.left != None):
            plist.extend(self.left.preorder_list())
        if(self.right != None):
            plist.extend(self.right.preorder_list())

        return(plist)

    def postorder_list(self):
        plist = []
        if (self.left != None):
            plist.extend(self.left.postorder_list())
        if (self.right != None):
            plist.extend(self.right.postorder_list())
        plist.append(self.data)

        return (plist)

if __name__ == "__main__":

    al = [1, 2, 30, 4, 60, 34, 12, -1, 5, 23, 67, 35, 4, 99, -20, -45, 89, 78]
    bt = create_tree(al)

    print("     list is                        : {}".format(al))
    print("     inorder list is                : {}".format(bt.inorder_list()))
    print("     nonrecursive inorder list is   : {}".format(bt.nr_inorder_list()))
    print("     preorder list is               : {}".format(bt.preorder_list()))
    print("     nonrecursive preeorder list is : {}".format(bt.nr_preorder_list()))
    print("     postorder list is              : {}".format(bt.postorder_list()))
    print("     nonrecursive postorder list is : {}".format(bt.nr_postorder_list()))




