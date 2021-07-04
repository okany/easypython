# This script finds the max depth of a binary tree
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
    if alist != None and alist != []:
        head = btree(alist[0])
        for each in alist[1:]:
            head.add(each)

    return head

class btree():
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def add(self, data):
        rslt = False
        if self.data < data:
            if self.right == None:
                dt = btree(data)
                self.right = dt
                rslt = True
            else:
                return self.right.add(data)
        elif self.data > data:
            if self.left == None:
                dt = btree(data)
                self.left = dt
                rslt = True
            else:
                return self.left.add(data)

        return rslt

    def to_tree_list(self, depth=1):
        alist = []
        if(self.left):
            alist.append(self.left.to_tree_list(depth=depth+1))
        alist.append(self.data)
        if(self.right):
            alist.append(self.right.to_tree_list(depth=depth+1))

        print("depth= {}", depth)
        return alist

    def to_list(self):
        alist = []
        if(self.left):
            alist.extend(self.left.to_list())
        alist.append(self.data)
        if(self.right):
            alist.extend(self.right.to_list())
        return alist

    def maxdepth(self):
        ld = rd = 1
        if self.left:
            ld = 1 + self.left.maxdepth()
        if self.right:
            rd = 1 + self.right.maxdepth()

        md = max(ld, rd)

        return(md)

if __name__ == "__main__":

    alist = [25, 24, 1, 2 ,6 ,7, -15, -10, -5, -4, 50, 66, 73, 89, 100, 45, 23, 8, 45, 9, 10]

    bt = create_btree(alist)

    print("Max depth of btree {} is {}".format(bt.to_list(), bt.maxdepth()))
    print("nested tree like list is {}".format(bt.to_tree_list()))
