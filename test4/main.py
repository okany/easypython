# This script recovers a binary search tree with 2 replaced nodes
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
    bt = None
    if alist != None and alist != []:
        bt = btree(alist[0])
        for each in alist[1:]:
            add_btree(bt, each)
    return bt

def add_btree(bt, data):
    if data == None:
        pass
    elif bt == None:
        bt = btree(data)
    else:
        if data == bt.data:
            pass #duplicate, do don't do anything (or raise an except
        elif data < bt.data:
            if bt.left:
                add_btree(bt.left, data)
            else:
                bt.left = btree(data)
        else:
            if bt.right:
                add_btree(bt.right, data)
            else:
                bt.right = btree(data)

def recover_btree(bt):
    reclist = bt.recover()
    print("MIN misplaced {} and MAX misplaced {}".format(bt.recmin.data, bt.recmax.data))
    swap_data(bt.recmin, bt.recmax)
    return reclist

def swap_data(a, b):
    temp = a.data
    a.data = b.data
    b.data = temp

class btree():
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.resetrecovery()

    def resetrecovery(self):
        self.recmin = self.recmax = None

    # set minimum misplaced node
    def setrecmin(self, node):
        if(node):
            if(self.recmin == None or self.recmin.data > node.data):
                self.recmin = node

    # set maximum misplaced node
    def setrecmax(self, node):
        if(node):
            if(self.recmax == None or self.recmax.data < node.data):
                self.recmax = node

    def to_list(self):
        alist = []

        if self.left:
            alist.extend(self.left.to_list())
        alist.append(self)
        if self.right:
            alist.extend(self.right.to_list())

        return alist

    def to_data_list(self):
        alist = []

        if self.left:
            alist.extend(self.left.to_data_list())

        alist.append(self.data)

        if self.right:
            alist.extend(self.right.to_data_list())

        return alist

    def to_data_tlist(self):
        alist = []

        if self.left:
            alist.append(self.left.to_data_tlist())

        alist.append(self.data)

        if self.right:
            alist.append(self.right.to_data_tlist())

        return alist

    def recover(self):
        ll = []
        rl = []
        self.resetrecovery()

        if self.left:
            ll = self.left.recover()
            self.setrecmin(self.left.recmin)
            self.setrecmax(self.left.recmax)
            if ll[-1] and (ll[-1].data > self.data):
                self.setrecmin(self)
                self.setrecmax(ll[-1])

        if self.right:
            rl = self.right.recover()
            self.setrecmin(self.right.recmin)
            self.setrecmax(self.right.recmax)
            if rl[0] and (rl[0].data < self.data):
                self.setrecmin(rl[0])
                self.setrecmax(self)

        ll.append(self)
        ll.extend(rl)
        dl = []
        #for each in ll:
        #    dl.append(each.data)
        #print ("recover = {}".format(dl))
        return ll

if __name__=="__main__":

    bt = create_btree([1, 2, 30, 4, 60, 34, 12, -1, 5, 23, 67, 35, 4, 99, -20, -45, 89, 78])
    tlist = bt.to_list()
    print("Original tlist  = ", bt.to_data_tlist())

    #test 6th and 11th replacement
    swap_data(tlist[5], tlist[10])
    print("broken list     = ", bt.to_data_tlist())
    reclist = recover_btree(bt)
    print("recovered list  = ", bt.to_data_list())

    tlist = bt.to_list()
    print("\n\nOriginal tlist  = ", bt.to_data_tlist())
    # test min and max replacement
    swap_data(tlist[0], tlist[16])
    print("broken list     = ", bt.to_data_tlist())
    reclist = recover_btree(bt)
    print("recovered list  = ", bt.to_data_list())

    tlist = bt.to_list()
    print("\n\nOriginal tlist  = ", bt.to_data_tlist())
    # test 7th and 15th replacement
    swap_data(tlist[6], tlist[14])
    print("broken list     = ", bt.to_data_tlist())
    reclist = recover_btree(bt)
    print("recovered list  = ", bt.to_data_list())
