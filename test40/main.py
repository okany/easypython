# This script returns level order of a binary tree
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
def create_btree(alist):
    head = None
    if not alist or alist == []:
        pass
    else:
        tn = treenode(alist[0])
        head = tn
        for item in alist[1:]:
            tn.add_node(item)

    return head

def create_levelorder(tn):
    lvl = 0
    lolist = list()
    tn.levelorder(lolist, 0)

    return lolist

class treenode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if(data<self.data):
            if(self.left):
                self.left.add_node(data)
            else:
                self.left = treenode(data)
        elif(data>self.data):
            if(self.right):
                self.right.add_node(data)
            else:
                self.right = treenode(data)
        else:
            pass # duplicate node, just ignore

    def levelorder(self, lolist, lvl):
        if(len(lolist) <= lvl):
            lolist.append(list())

        lolist[lvl].append(self.data)
        if(self.left):
            self.left.levelorder(lolist, lvl+1)

        if(self.right):
            self.right.levelorder(lolist, lvl+1)

if __name__ == "__main__":

    tlist = [20, 34, 10, 11, 45, 42, 13, 17, 25, 28, 5, 7]

    tr = create_btree(tlist)

    lolist = create_levelorder(tr)

    print("test#1 - levelorder of {} is {}".format(tlist, lolist))

    tlist = [15, 2, 60, 72, 48, 12, 11, 20, 34, 10, 11, 45, 42, 13, 17, 25, 28, 5, 7]

    tr = create_btree(tlist)

    lolist = create_levelorder(tr)

    print("test#2 - levelorder of {} is {}".format(tlist, lolist))

    tlist = [1]

    tr = create_btree(tlist)

    lolist = create_levelorder(tr)

    print("test#3 - levelorder of {} is {}".format(tlist, lolist))

