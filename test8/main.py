# Find the kth minimum of a list
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

import sys
class datalist(list):

    def __init__(self, k, alist):
        self.fname = ""
        self.kvalue = k
        super().__init__(alist)
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
            self.append(num)

    def printdata(self):

        print("items in the list are ")
        for item in self:
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
        if (len(self) < self.kvalue):
            return None
        else:
            for item in self:
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


