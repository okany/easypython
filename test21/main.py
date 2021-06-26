# This script reverses a singly linked list

def createlinkedlist(alist):
    if alist == None or alist == []:
        return None

    llist = linkedlist(alist[0])
    trv = llist
    for item in alist[1:]:
        trv.next = linkedlist(item)
        trv = trv.next
    return llist

class linkedlist():
    def __init__(self, data):
        self.data = data
        self.next = None

    def setnext(self, ll):
        self.next = ll

    def sefdata(self, data):
        self.data = data

    def reverse(self):
        if(self == None): re = None
        elif(self.next == None):
            rev = linkedlist(self.data)
        else:
            trv = self
            prev = linkedlist(self.data)
            while trv.next != None:
                next = linkedlist(trv.next.data)
                next.setnext(prev)
                rev = prev = next
                trv = trv.next

        return rev

    def tolist(self):
        alist = []
        trv = self

        while trv != None:
            alist.append(trv.data)
            trv = trv.next
        return(alist)

if __name__ == "__main__":

    ml = createlinkedlist(
        ["a", "s", "d", "a", "s", "d", "a", "s", "f", "d", "s", "g", "g", "d", "f", "g", "d", "f", "f", "g", "h", "j",
         "f", "g", "h", "j", "g", "h", "j"])
    print("reverse of list {} is {}".format(ml.tolist(), ml.reverse().tolist()))

    ml = createlinkedlist(["a", "s", "d", "a", "s", "d", "a", "s", "f", "g", "h", "j", "g", "h", "j"])
    print("reverse of list {} is {}".format(ml.tolist(), ml.reverse().tolist()))

    ml = createlinkedlist([])
    print("reverse of list {} is {}".format(ml, ml))

    ml = createlinkedlist([1])
    print("reverse of list {} is {}".format(ml.tolist(), ml.reverse().tolist()))

    ml = createlinkedlist(["a", "s", "d", "a", "s", "d", "a", "s", "f", "g", "h", "j", "g", "h", "j"])
    print("reverse of list {} is {}".format(ml.tolist(), ml.reverse().tolist()))
