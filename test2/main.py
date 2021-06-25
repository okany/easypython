# Find the kth minimum number in a list
import sys

class datalist:
    def __init__(self, list):
        self.mylist = list
        self.k = 0
        self.klist = []

    def printlist(self):
        print("DATALIST =", self.mylist)

    def insertklist(self, newitem):
        if(len(self.klist) == self.k and self.klist[self.k-1]<newitem):
            return
        else:
            index = 0
            for item in self.klist:
                if item > newitem:
                    break
                else:
                    index = index+1

            self.klist.insert(index, newitem)
            if len(self.klist) > self.k: self.klist.pop(self.k)

    def printkmin(self, k):
        self.k = k
        if len(self.klist)>0: self.klist.clear()
        if(len(self.mylist) < self.k):
            return None
        else:
            for item in self.mylist:
                self.insertklist(item)
            return self.klist[self.k-1]

if __name__ == '__main__':

    dl1 = datalist([2,3,1,4,5,6,7,6,8,78,23,34,2,4,5,7,8,0,122])

    dl1.printlist()
    min = dl1.printkmin(5)
    print ("kmin=", min)

    dl2 = datalist([2,3,1,4,5,6,7,6,8,78,23,34,2,4,5,7,8,0,122])
    dl1.printlist()
    min = dl1.printkmin(25)
    print ("kmin=", min)

