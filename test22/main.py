# This script implements a binary tree

def create_binary_tree(alist):
    try:
        if alist is None: return None
        else:
            bt = btree(alist[0])
            for item in alist[1:]:
                bt.insert(item)
    except:
        raise

    return bt

class btree():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def find(self, data):
        if self.data == data:
            return self
        elif self.data > data:
            if(self.left != None):
                return self.left.find(data)
            else:
                return None
        else:
            if(self.right != None):
                return self.right.find(data)
            else:
                return None

    def insert(self, num):
        if self.data == num:
            raise ValueError
        elif self.data > num:
            if self.left == None:
                self.left = btree(num)
            else:
                self.left.insert(num)
        else:
            if self.right == None:
                self.right = btree(num)
            else:
                self.right.insert(num)

    def to_list(self):
        alist = llist = rlist = []
        if(self.left != None):
            llist = self.left.to_list()
            alist.extend(llist)
        alist.append(self.data)
        if(self.right != None):
            rlist = self.right.to_list()
            alist.extend(rlist)

        return alist

if __name__ == "__main__":

    try:
        al = [1, 2, 30, 4, 60, 34, 12, -1 , 5, 23, 67, 35, 4, 99, -20, -45, 89, 78]
        bt = create_binary_tree(al)
        num = 55

        print("{} node in binary tree {} is {}".format(num, bt.to_list(), bt.find(num)))

    except:
        print ("list is not unique")

    try:
        al = [1, 2, 30, 4, 60, 34, 12, -1 , 5, 23, 67, 35, 99, -20, -45, 89, 78]
        bt = create_binary_tree(al)

        num = 55
        print("{} node in binary tree {} is {}".format(num, bt.to_list(), bt.find(num)))

        num = 99
        print("{} node in binary tree {} is {}".format(num, bt.to_list(), bt.find(num)))

    except:
        print ("list is not unique")
