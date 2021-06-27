# This script finds the middle node in a linked list in one pass

def create_linkedlist(alist):
    if (alist == None or alist == []):
        return None
    else:
        head = linkedlist(alist[0])
        head.next = create_linkedlist(alist[1:])

    return head

def find_middle(ll):
    lldict = dict()
    if ll == None: return None
    else:
        node = ll
        index = 0
        while node != None:
            lldict[index] = node
            node = node.next
            index = index + 1

    size = index
    middle = int(size/2)

    return(lldict[middle])

class linkedlist():
    def __init__(self, data):
        self.data = data
        self.next = None

    def tolist(self):
        alist = []
        item = self
        while item != None:
            alist.append(item.data)
            item = item.next

        return alist

if __name__ == "__main__":
    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","d","s","g","g","d","f","g","d","f","f","g","h","j","f","g","h","j","g","h","j"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j","q"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist([])
    print("middle item in the list {} is {}".format(ml, find_middle(ml)))

    ml = create_linkedlist([1])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))

    ml = create_linkedlist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    print("middle item in the list {} is {}".format(ml.tolist(), find_middle(ml).data))
