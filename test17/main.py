# this script finds the nth node from the end in a singly linked list

class mylist():
    def __init__(self, alist):
        self.next = None
        self.data = None
        if (alist != None and alist != []):
            # create an object with no valid atrribute if the list is None or empty
            self.data = alist[0]
            self.next = None
            if(len(alist) > 1):
                self.next = mylist(alist[1:])

    def tolist(self):
        alist = []
        trv = self
        while trv != None:
            if(trv.data != None):
                alist.append(trv.data)
            trv = trv.next

        return alist

    def enditem(self, num):

        if(num <= 0): return None

        numlist = []
        trv  = self
        for i in range(num):
            if(trv is None):
                return(None)
            else:
                numlist.append(trv.data)
                trv = trv.next
        while trv != None:
            numlist.append(trv.data)
            numlist.pop(0)
            trv = trv.next

        return(numlist[0])

if __name__ == '__main__':
    ml = mylist(["a","s","d","a","s","d","a","s","f","d","s","g","g","d","f","g","d","f","f","g","h","j","f","g","h","j","g","h","j"])
    nth = 9
    print("{}th item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

    ml = mylist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    nth = 6
    print("{}th item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

    ml = mylist([])
    nth = 6
    print("{}th item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

    ml = mylist([1])
    nth = 1
    print("{}st item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

    ml = mylist(["a","s","d","a","s","d","a","s","f","g","h","j","g","h","j"])
    nth = 0
    print("{}th item from the end of list {} is {}".format(nth, ml.tolist(), ml.enditem(nth)))

