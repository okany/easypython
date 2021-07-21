# This script rotates a matrix 90 degrees clockwise without using another matrix
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

class matrix():
    def __init__(self, alist):
        self.alist = alist
        self.n = len(self.alist)
        self.clist = None

        if self.verify() == False:
            raise ValueError

    def verify(self):
        ret = False
        if(self.n > 0 and len(self.alist) == self.n):
            ret = True
            for i in range(self.n):
                if(len(self.alist[i]) != self.n):
                    ret = False
                    break
        return ret

    def rotate(self):
        # rotate only one forth of the array
        for x in range(self.n >> 1):
            # if n is odd include an extra column
            for y in range((self.n + 1) >> 1):
                tmp = self.alist[x][y]
                self.alist[x][y] = self.alist[self.n-y-1][x]
                self.alist[self.n - y - 1][x] = self.alist[self.n-x-1][self.n-y-1]
                self.alist[self.n - x - 1][self.n-y-1] = self.alist[y][self.n-x-1]
                self.alist[y][self.n-x-1] = tmp

    def print(self):
        print("[")
        for y in range(self.n-1):
            print("  {},".format(self.alist[y]))
        if self.n > 0:
            print("  {}".format(self.alist[self.n-1]))
        print("]")

if __name__=="__main__":


    try:
        alist = [[1, 2, 5, 12, 15], [6, 7, 9, 3, 4], [10, 11, 0, 14, 16], [1, 13, 17, 18, 19], [20, 24, 23, 22, 21]]
        mat = matrix(alist)
        print("TEST#1 - Original Matrix:")
        mat.print()

        mat.rotate()
        print("TEST#1 - Rotated Matrix:")
        mat.print()

        alist = [[1]]
        mat = matrix(alist)
        print("TEST#2 - Original Matrix:")
        mat.print()

        mat.rotate()
        print("TEST#2 - Rotated Matrix:")
        mat.print()

        alist = [[1, 2, 5, 12, 15, 25], [6, 7, 9, 3, 4, 26], [10, 11, 0, 14, 16, 27],
                 [36, 13, 17, 18, 19, 28], [20, 24, 23, 22, 21, 29], [30, 31, 32, 33, 34, 35]]
        mat = matrix(alist)
        print("TEST#3 - Original Matrix:")
        mat.print()

        mat.rotate()
        print("TEST#3 - Rotated Matrix:")
        mat.print()


    except ValueError:
        print("ValueError")

