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
class matrix():
    def __init__(self, amatrix, debug = False):
        self.amatrix = amatrix
        self.debug = debug
        # accumulate the cells above each line to turn this into the
        # maximum rectangle in a histogram problem
        self.hmatrix = list()
        # create a sort matrix to keep the sorted hight matrix indices
        self.smatrix = list()
        # set self.hmatrix and self.smatrix attributes
        self.create_hight_matrix()
        self.maxrect = 0
        if debug == True:
            print("Hight Matrix:")
            self.dump(self.hmatrix)
            print("Sorted Matrix:")
            self.dump(self.smatrix)

    def create_hight_matrix(self):

        for i in range(len(self.amatrix)):
            self.hmatrix.append(list())
            self.smatrix.append(list())
            for j in range(len(self.amatrix[i])):
                if i == 0:
                    # set the hight matrix value
                    self.hmatrix[i].append(self.amatrix[i][j])
                    if self.amatrix[i][j] > 0:
                        self.smatrix[i].insert(0,j)
                else:
                    # set the hight matrix value
                    if(self.amatrix[i][j] == 0):
                        self.hmatrix[i].append(self.amatrix[i][j]) # reset the hight
                    else:
                        # add the cell value (1) to the high of the previous row
                        self.hmatrix[i].append(self.amatrix[i][j] + self.hmatrix[i-1][j])

                    if self.hmatrix[i][-1] > 0:
                        k = 0
                        # find the location of the new cell in the sorted list
                        while k < len(self.smatrix[i]) and self.hmatrix[i][self.smatrix[i][k]] > self.hmatrix[i][-1]:
                            k += 1
                        # insert the index of the new element in the sorted index list
                        self.smatrix[i].insert(k, j)

    def largest_rectangle(self):
        self.maxrect = 0

        for i in range(len(self.smatrix)):
            # create an empty row to store used
            # for j in range(self.smatrix[i]):
            #    used.append(0)
            used = list()

            for j in range(len(self.smatrix[i])):
                k = 0
                inserted = False
                while k < len(used) and inserted == False:

                    if (used[k][1] == self.smatrix[i][j] - 1):
                        used[k][1] = self.smatrix[i][j]
                        inserted = True
                        if (k + 1 < len(used)) and (used[k + 1][0] == self.smatrix[i][j] + 1):
                            used[k][1] = used[k + 1][1]
                            used.pop(k + 1)
                    elif (used[k][0] == self.smatrix[i][j] + 1):
                        used[k][0] = self.smatrix[i][j]
                        inserted = True
                    elif (used[k][0] > self.smatrix[i][j]):
                        used.insert(k, [self.smatrix[i][j], self.smatrix[i][j]])
                        inserted = True
                    else:
                        k += 1

                if inserted == False:
                    used.append([self.smatrix[i][j], self.smatrix[i][j]])

                thisrect = (used[k][1] - used[k][0] + 1) * self.hmatrix[i][self.smatrix[i][j]]

                if thisrect > self.maxrect:
                    self.maxrect = thisrect
            if debug == True:
                print("row {} used list is {}".format(i, used))
        return self.maxrect

    def dump(self, matrix):
        print("[")
        for each in matrix:
            print("  {}".format(each))

        print("]")

if __name__ == "__main__":

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

    mtx = matrix(mat1, debug)
    print("TEST#{} Matrix:".format(tno))
    mtx.dump(mat1)
    print("TEST#{} largest rectangle has {} cells".format(tno, mtx.largest_rectangle()))

    tno += 1
    debug = False
    mat1 = [[0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat1, debug)
    print("TEST#{} Matrix:".format(tno))
    mtx.dump(mat1)
    print("TEST#{} largest rectangle has {} cells".format(tno, mtx.largest_rectangle()))

    tno += 1
    debug = False
    mat1 = [[0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat1, debug)
    print("TEST#{} Matrix:".format(tno))
    mtx.dump(mat1)
    print("TEST#{} largest rectangle has {} cells".format(tno, mtx.largest_rectangle()))

    tno += 1
    debug = False
    mat1 = [[0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat1, debug)
    print("TEST#{} Matrix:".format(tno))
    mtx.dump(mat1)
    print("TEST#{} largest rectangle has {} cells".format(tno, mtx.largest_rectangle()))

    tno += 1
    debug = False
    mat1 = [[0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 1, 0, 1, 1],
           [1, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0]]

    mtx = matrix(mat1, debug)
    print("TEST#{} Matrix:".format(tno))
    mtx.dump(mat1)
    print("TEST#{} largest rectangle has {} cells".format(tno, mtx.largest_rectangle()))

