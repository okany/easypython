# This script finds the size of the largest rectangle in a binary matrix
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
class matrix(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.n = len(self)
        self.m = len(self[0])
        self.pairs = list()
        self.maxrect = 0
        self.intpairs = list()

    def find_intersects(self, list1, list2):
        i = j = 0
        intlist = list()
        maxrec = 0
        while i < len(list1) and j < len(list2):
            if list1[i][1] < list2[j][0]:
                # no intersection
                i += 1
            elif list1[i][0] > list2[j][1]:
                # no intersection
                j += 1
            else:
                inter = [max(list1[i][0], list2[j][0]), min(list1[i][1], list2[j][1])]
                maxrec = max(inter[1] + 1 - inter[0], maxrec)
                if list1[i][1] > list2[j][1]:
                    j += 1
                elif list1[i][1] < list2[j][1]:
                    i += 1
                else:
                    i += 1
                    j += 1
                intlist.append(inter)

        return intlist, maxrec

    # this function preclaculates the intersections of partial matrices which will be
    # reused during the largest rectangle calculation.
    def create_int_pairs(self, debug = False):
        self.intpairs = list()
        for i in range(self.n):
            plist = list()
            for j in range(self.n):
                plist.append(self.pairs[i].copy())
            self.intpairs.append(plist)

        for j in range(self.n - 1, -1, -1):
            i = j
            while i > 0:
                self.intpairs[j][i-1], maxint = self.find_intersects(self.pairs[i - 1], self.intpairs[j][i])
                if debug:
                    print("int pairs (i,j)=({},{}) is {}".format(i, j, self.intpairs[j][i]))
                i -= 1

    def largest_rect(self, debug = False):
        # iterate over each row to define the top edge of the rectangle
        for y in range(self.n):
            startx = endx = -1
            self.pairs.append(list())
            for x in range(self.m):
                if startx < 0 and self[y][x] == 1:
                    startx = x
                if startx >= 0 and endx < 0 and (self[y][x] == 0 or x == self.m - 1):
                    if self[y][x] == 0:
                        endx = x - 1
                    else:
                        endx = x
                    self.pairs[-1].append([startx, endx])
                    self.maxrect = max(self.maxrect, endx-startx)
                    startx = endx = -1

        if debug:
            for y in range(self.n):
                print("row {} pairs = {}".format(y, self.pairs[y]))

        self.create_int_pairs(debug)

        maxrec = 0
        j = self.n - 1
        for i in range(self.n - 1):
            for j in range(self.n - 1, -1, -1):
                ints, maxint = self.find_intersects(self.pairs[i], self.intpairs[j][i+1])
                maxrec = max(maxint * (j - i + 1), maxrec)
                if debug:
                    print("ints = {}, max rectangle = {}".format(ints, maxrec))

        return maxrec

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    mat1 = [[0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0]]

    mtx = matrix(mat1)
    maxrec = mtx.largest_rect(debug)
    print("TEST#{} largest rectangle has {} cells".format(tno, maxrec))

    tno += 1
    debug = False
    mat2 = [[0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat2)
    maxrec = mtx.largest_rect(debug)
    print("TEST#{} largest rectangle has {} cells".format(tno, maxrec))

    tno += 1
    debug = False
    mat2 = [[0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat2)
    maxrec = mtx.largest_rect(debug)
    print("TEST#{} largest rectangle has {} cells".format(tno, maxrec))

    tno += 1
    debug = False
    mat = [[0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat)
    maxrec = mtx.largest_rect(debug)
    print("TEST#{} largest rectangle has {} cells".format(tno, maxrec))

    tno += 1
    debug = False
    mat = [[0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 1, 0, 1, 1],
           [1, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat)
    maxrec = mtx.largest_rect(debug)
    print("TEST#{} largest rectangle has {} cells".format(tno, maxrec))
