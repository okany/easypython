# This script returns level order of a binary tree

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

