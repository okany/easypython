# This script implements bubble sort, insertion sort, quick sort, merge sort, and bucket sort algorithms
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright (c) 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

class slist(list):

    def __init__(self, slist):
        super().__init__(slist)
        self.blist = slist
        self.ilist = slist
        self.bclist = []

    def bubblesort(self):
        last = len(self) - 1
        while last > 0:
            for i in range(last):
                if self.blist[i] > self.blist[i+1]:
                    temp = self.blist[i]
                    self.blist[i] = self.blist[i+1]
                    self.blist[i+1] = temp
            last = last - 1
        return self.blist

    def insertionsort(self):
        last = len(self)
        first = 0
        while first < last:
            min = self.ilist[first]
            mindex = first
            for i in range(first+1, last):
                if self.ilist[i] < min:
                    min = self.ilist[i]
                    mindex = i
            if(mindex != first):
                self.ilist.pop(mindex)
                self.ilist.insert(0,min)
            first = first + 1

        return self.ilist

    def findminmax(self):
        min = max = self[0]
        for each in self:
            if each < min:
                min = each
            elif each > max:
                max = each
        return min, max

    def bucketsort(self, k):
        if(len(self)<=1): return self
        min, max = self.findminmax()
        bucket = []
        bsize = int((max - min)/k)+1
        for i in range(k):
            bucket.append([])
        for each in self:
            bucket[int((each-min)/bsize)].append(each)

        for i in range(k):
            alist = slist(bucket[i])
            self.bclist.extend(alist.insertionsort())

        return self.bclist


def partition(list, pi):
    low = []
    high = []
    for i in range(len(list)):
        if i == pi: pass
        elif list[i] > list[pi]:
            high.append(list[i])
        else:
            low.append(list[i])
    return low, high

def quicksort(list):
    if(list == None): return None
    elif(len(list) <= 1):
        return list
    else:
        low, high = partition(list, 0)
        # print("low = {}, pivot = {}, high = {}".format(low, list[0], high))
        qlist = quicksort(low)
        qlist.append(list[0])
        qlist.extend(quicksort(high))

    return qlist

def mergesort(list):
    if list == None: return None
    elif(len(list) <=1): return list
    else:
        mid = int(len(list)/2)
        alist = list[:mid]
        blist = list[mid:]
        amlist = mergesort(alist)
        bmlist = mergesort(blist)
        i = j = 0
        mlist = []
        while(i<len(amlist) and j<len(bmlist)):
            if(amlist[i]<bmlist[j]):
                mlist.append(amlist[i])
                i = i + 1
            else:
                mlist.append(bmlist[j])
                j = j + 1
        mlist.extend(amlist[i:])
        mlist.extend(bmlist[j:])

    return mlist

if __name__ == '__main__':
    al = slist([1, 2, 30, 4, 60, 34, 12, -1, 5, 23, 67, 35, 4, 99, -20, -45, 89, 78])

    print("\nOriginal list         = ", al)
    print("Bubble sorted list    = ", al.bubblesort())
    print("Insertion sorted list = ", al.insertionsort())
    print("Quick sorted list     = ", quicksort(al))
    print("Merge sorted list     = ", mergesort(al))
    print("Bucket sorted list    = ", al.bucketsort(5))

    al2 = slist([])

    print("\nOriginal list         = ", al2)
    print("Bubble sorted list    = ", al2.bubblesort())
    print("Insertion sorted list = ", al2.insertionsort())
    print("Quick sorted list     = ", quicksort(al2))
    print("Merge sorted list     = ", mergesort(al2))
    print("Bucket sorted list    = ", al2.bucketsort(3))

    al3 = slist([1])

    print("\nOriginal list         = ", al3)
    print("Bubble sorted list    = ", al3.bubblesort())
    print("Insertion sorted list = ", al3.insertionsort())
    print("Quick sorted list     = ", quicksort(al3))
    print("Merge sorted list     = ", mergesort(al3))
    print("Bucket sorted list    = ", al3.bucketsort(7))

    al4 = slist([10, 1])

    print("\nOriginal list         = ", al4)
    print("Bubble sorted list    = ", al4.bubblesort())
    print("Insertion sorted list = ", al4.insertionsort())
    print("Quick sorted list     = ", quicksort(al4))
    print("Merge sorted list     = ", mergesort(al4))
    print("Bucket sorted list    = ", al4.bucketsort(2))

