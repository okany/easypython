# Find the kth minimum of a list

import sys

class datalist:

    def __init__(self, k, alist):
        self.fname = ""
        self.kvalue = k
        self.list = alist
        self.klist = []

    def readdata(self):
        print("Please enter the data file name:")
        for self.fname in sys.stdin:
            break

        try:
            # open file
            f = open(self.fname.rstrip())
        except:
            print("file open failed")
            exit(1)

        # read words
        for num in f:
            self.list.append(num)

    def printdata(self):

        print("items in the list are ")
        for item in self.list:
            print(item)

        print("items in the klist are")
        for item in self.klist:
            print(item)

    def insertklist(self, newitem):
        # list is full?
        if (len(self.klist) == self.kvalue and self.klist[self.kvalue-1] < newitem):
            return
        else:
            index = 0
            for item in self.klist :
                if item > newitem:
                    break
                else:
                    index = index+1
            self.klist.insert(index, newitem)

        if(len(self.klist) > self.kvalue):
            self.klist.pop(self.kvalue)

    def findkmin(self):
        if (len(self.list) < self.kvalue):
            return None
        else:
            for item in self.list:
                self.insertklist(item)
            return self.klist[self.kvalue-1]


def readk():
    line = input("Please enter K value:")
    try:
        k = int(line)
    except:
        print("invalid K value entered")
        exit(1)
    else:
        return k


if __name__ == '__main__':

    #kvalue = readk()
    #print('k value is', kvalue)

    #dl = datalist()
    #dl.readdata()
    #dl.printdata()

    dl1 = datalist(100, (1,9,7,8,2,3,5,5,3,3,2,1,43,35,5,45,0,213,12))
    print("TEST#1 - kmin=", dl1.findkmin())

    dl2 = datalist(5, (10,100,78,9,7,8,2,3,5,5,3,3,2,1,43,35,5,45,0,213,12))
    print("TEST#2 - kmin=", dl2.findkmin())
    dl2.printdata()

    #kval = readk()

    #print("K is =", kval)


