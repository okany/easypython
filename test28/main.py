# This script finds the least common ancestor of two elements in a binary seach tree
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

def create_btree(list):
    bt = None
    if(list == None or list == []):
        return None
    else:
        for each in list:
            bt = addbtree(bt, each)
    return bt


def addbtree(tree, data):
    bt = btree(data)
    if tree == None:
        return bt
    elif (tree.data > data):
        if(tree.left == None):
            tree.left = bt
        else:
            addbtree(tree.left, data)
    elif (tree.data < data):
        if(tree.right == None):
            tree.right = bt
        else:
            addbtree(tree.right, data)

    return tree

class btree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def to_list(self):
        list = []
        if self.left:
            list.extend(self.left.to_list())
        list.append(self.data)
        if self.right:
            list.extend(self.right.to_list())

        return list

    def find(self, a):
        dlist = []
        if self.data == a:
            dlist.append(a)
        elif self.data < a:
            if(self.right):
                dlist = self.right.find(a)
                if dlist != []:
                    dlist.append(self.data)
        else:
            if(self.left):
                dlist = self.left.find(a)
                if dlist != []:
                    dlist.append(self.data)

        return dlist

    def common_ancestor(self, a, b):
        hash = dict()
        alist = self.find(a)
        blist = self.find(b)

        if(alist == [] or blist == []): return None, None

        mindist = len(alist) + len(blist)
        common = alist[-1]

        # store the parent nodes in the dict
        for i in range(len(alist)):
            if(hash.get(alist[i]) == None):
                hash[alist[i]] = i

        for i in range(len(blist)):
            if(hash.get(blist[i]) != None):
                dist = i + hash[blist[i]]
                if mindist > dist:
                    mindist = dist;
                    common = blist[i]

        print("ALIST = {} BLIST = {}, common = {}, distance = {}".format(alist, blist, common, mindist))

        return common, mindist

if __name__=="__main__":

    bt = create_btree([1, 2, 30, 4, 60, 34, 12, -1, 5, 23, 67, 35, 4, 99, -20, -45, 89, 78])
    print("AL = ", bt.to_list())

    bt.common_ancestor(4, 35)
    bt.common_ancestor(5, 12)
    bt.common_ancestor(12, 35)
