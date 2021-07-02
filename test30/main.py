# This script creates a binary tree iterator

def create_btree(alist):
    bt = None
    if (alist != None and alist != []):
        bt = btree(alist[0])
        for each in alist [1:]:
            bt.add(each)
    return bt

class btree():
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.parent = None

    def add(self, data):
        ret = False
        if data == self.data:
            # error - skip it
            pass
        else:
            next = None
            if(self.data > data):
                next = self.left
            else:
                next = self.right

            if(next == None):
                node = btree(data)
                node.parent = self
                if(self.data > data):
                    self.left = node
                else:
                    self.right = node
                ret = True
            else:
                ret = next.add(data)
        return ret

    def to_list(self):
        alist = []

        if(self.left):
            alist.append(self.left.to_list())
        alist.append(self.data)
        if(self.right):
            alist.append(self.right.to_list())

        return alist

class iter():
    def __init__(self, bt):
        self.bt = bt
        self.cur = None

    def begin(self):
        if(self.bt.left):
            it = iter(self.bt.left)
            return(it.begin())
        else:
            return self.bt

    def end(self):
        if(self.bt.right):
            it = iter(self.bt.right)
            return(it.end())
        else:
            return self.bt

    def next(self):
        bt = self.cur
        self.cur = None
        if(bt.right):
            it = iter(bt.right)
            self.cur = it.begin()
        else:
            while (bt.parent and self.cur == None):
                if(bt.parent.right != bt):
                    self.cur = bt.parent
                else:
                    bt = bt.parent

        return self.cur

    def setcurrent(self, node):
        self.cur = node

    def current(self):
        return self.cur

if __name__=="__main__":

    alist = [1, 2, 30, 4, 60, 34, 12, -1, 5, 23, 67, 35, 4, 99, -20, -45, 89, 78]
    bt = create_btree(alist)
    print("list is {}".format(alist))
    print("btree is {}".format(bt.to_list()))

    it = iter(bt)
    it.setcurrent(it.begin())
    print ("it begin = {} and it end {}".format(it.current().data, it.end().data))

    while(it.current() != it.end()):
        print ("in next= {}".format(it.next().data))
