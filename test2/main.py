# Find the kth minimum number in a list
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

class datalist(list):
    def __init__(self, list):
        self.k = 0
        self.klist = []
        super().__init__(list)

    def printlist(self):
        print("DATALIST =", self)

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
        if(len(self) < self.k):
            return None
        else:
            for item in self:
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

