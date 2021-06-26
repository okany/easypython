# this script finds the nth node from the end in a singly linked list

class mylist(list):
    def __init__(self, alist):
        super().__init__(alist)

    def enditem(self, num):
        if(len(self)<num): None
        else:
            tmplist = []
            for item in self[:num]:
                tmplist.append(item)
            for item in self[num:]:
                tmplist.append(item)
                tmplist.pop(0)

        return(tmplist[0])

if __name__ == '__main__':
    tlist1 = ["a","s","d","a","s","d","a","s","f","d","s","g","g","d","f","g","d","f","f","g","h","j","f","g","h","j","g","h","j"]

    ml = mylist(tlist1)
    nth = 9
    print("{} item from the end of list {} is {}".format(nth, ml, ml.enditem(nth)))
