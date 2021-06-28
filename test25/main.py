# This script prints all leaves of a binary tree

def create_btree(alist):
    bt = None
    if((alist == None) or (alist == [])):
        pass
    else:
        bt = btree(alist[0])
        for each in alist[1:]:
            bt.insert(each)

    return bt

class btree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setleft(self, lt):
        self.left = lt

    def setright(self, rt):
        self.right = rt

    def insert(self, data):
        if(self.data > data):
            if self.left:
                self.left.insert(data)
            else:
                self.left = btree(data)
        elif(self.data < data):
            if self.right:
                self.right.insert(data)
            else:
                self.right = btree(data)
        else:
            pass
            # duplicate - just skip (or raise an exception)

    def print_leaves(self):
        leaves = []
        if self.left == None and self.right == None :
            #print ("leaf = {}".format(self.data))
            leaves.append(self.data)
        else:
            if self.left:
                leaves.extend(self.left.print_leaves())
            if self.right:
                leaves.extend(self.right.print_leaves())
        return leaves

    def to_list(self):
        alist = []
        if self.left:
            alist.extend(self.left.to_list())
        alist.append(self.data)
        if self.right:
            alist.extend(self.right.to_list())

        return alist

if __name__ == "__main__":
    al = [1, 2, 30, 4, 60, 34, 12, -1, 5, 23, 67, 35, 4, 99, -20, -45, 89, 78]
    bt = create_btree(al)

    print("list  = ", bt.to_list())
    print("LEAVES...:", bt.print_leaves())
