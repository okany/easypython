# This script finds the size of the largest rectangle in a binary matrix in O(NxN) time complexity
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
        self.matrix = list()
        self.n = 0
        self.m = 0
        self.create_matrix()
        self.pairs = list()
        self.maxrect = 0
        self.intpairs = list()

    def create_matrix(self):
        self.n = len(self)
        if(self.n>0):
            self.m = len(self[0])

        # create a boundary lines around the input matrix
        for y in range(self.n+2):
            row = list()
            for x in range(self.m+2):
                if (y == 0 or x == 0 or y == self.n+1 or x == self.m+1):
                    row.append(0)
                else:
                    row.append(self[y-1][x-1])
            if len(row) != self.m+2:
                raise(ValueError)
            self.matrix.append(row)

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
    # reused during the largest rectangle calculation. This matrix reduces the complexity
    # of the algorithm to O(NxN)
    def create_int_pairs(self, debug = False):
        self.intpairs = list()
        for i in range(self.n):
            self.intpairs.append(self.pairs[i].copy())

        i = self.n - 1
        if debug:
            print("int pairs {} = {}".format(i, self.pairs[i]))
        while i > 0:
            self.pairs[i-1], maxint = self.find_intersects(self.pairs[i - 1], self.pairs[i])
            if debug:
                print("int pairs {} = {}".format(i, self.pairs[i]))
            i -= 1

    def largest_rect(self, debug = False):
        # iterate over each row to define the top edge of hte rectangle
        for y in range(1, self.n+2):
            startx = endx = -1
            self.pairs.append(list())
            for x in range(1, self.m+2):
                if startx < 0 and self.matrix[y][x] == 1:
                    startx = x - 1
                if startx >= 0 and endx < 0 and self.matrix[y][x] == 0:
                    endx = x - 2
                    self.pairs[-1].append([startx, endx])
                    self.maxrect = max(self.maxrect, endx-startx)
                    startx = endx = -1
        if debug:
            for y in range(self.n):
                print("row {} pairs = {}".format(y, self.pairs[y]))

        self.create_int_pairs(debug)

        maxrec = 0
        for i in range(self.n - 1):
            ints, maxint = self.find_intersects(self.pairs[i], self.intpairs[i+1])
            maxrec = max(maxint * (self.n - i), maxrec)
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
