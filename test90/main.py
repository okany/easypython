# This script returns elements of an NxM matrix in spiral order
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
    def __init__(self, amat, debug = False):
        self.amat = amat
        self.debug = debug
        # set N X M values
        self.N = len(amat)
        self.M = len(amat[0])
        # use the delta matrix below to calculate the next cell to add to spiral list
        self.delta = [[0, 1],
                      [1, 0],
                      [0,-1],
                      [-1,0]]
        # Xrange and Yrange delta values are coded in the matrix below
        # might be confusing but this is an alternative to have 4 if/elif
        # statements that are commented out below
        self.range_delta = [[0,0,1,0],[1,0,0,0],[0,0,0,-1],[0,-1,0,0]]
        self.Xrange = [0, self.N - 1]
        self.Yrange = [0, self.M - 1]
        self.spiral = list()

    def print(self):
        print("[")
        for each in self.amat:
            print(" {},".format(each))
        print("]")

    def spiral_form(self):
        current = [0,0]
        dindex = 0
        append = True

        while self.Xrange[0] <= self.Xrange[1] and self.Yrange[0] <= self.Yrange[1]:
            if append:
                self.spiral.append(self.amat[current[0]][current[1]])
            increment = self.delta[dindex % 4]
            next = [current[0]+increment[0], current[1]+increment[1]]
            if self.debug:
                print("next element = {}".format(next))
            if next[0] >= self.Xrange[0] and next[0] <= self.Xrange[1] and next[1] >= self.Yrange[0] and next[1] <= self.Yrange[1]:
                current = next
                append = True
            else:
                dindex += 1
                '''
                if(self.delta[dindex % 4][0]) > 0:
                    self.Xrange[0] += 1
                elif (self.delta[dindex % 4][0]) < 0:
                    self.Xrange[1] -= 1
                elif (self.delta[dindex % 4][1]) > 0:
                    self.Yrange[0] += 1
                elif (self.delta[dindex % 4][1]) < 0:
                    self.Yrange[1] -= 1
                
                use the delta values stored in the range_delta matrix below instead of the if/elif statments above
                '''
                self.Xrange[0] += self.range_delta[dindex % 4][0]
                self.Xrange[1] += self.range_delta[dindex % 4][1]
                self.Yrange[0] += self.range_delta[dindex % 4][2]
                self.Yrange[1] += self.range_delta[dindex % 4][3]
                append = False

        return self.spiral

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    amatrix = [[1]]

    mat = matrix(amatrix, debug)
    print("TEST#{} Original Matrix:")
    mat.print()
    sp = mat.spiral_form()
    print("TEST#{} Spiral List : {}".format(tno, sp))

    tno += 1
    debug = False
    amatrix = [[1,2,3,4],
               [10,11,12,5],
               [9,8,7,6]]

    mat = matrix(amatrix, debug)
    print("TEST#{} Original Matrix:")
    mat.print()
    sp = mat.spiral_form()
    print("TEST#{} Spiral List : {}".format(tno, sp))

    tno += 1
    debug = False
    amatrix = [[1,2,3,4,5],
               [14,15,16,17,6],
               [13,20,19,18,7],
               [12,11,10,9,8]]

    mat = matrix(amatrix, debug)
    print("TEST#{} Original Matrix:")
    mat.print()
    sp = mat.spiral_form()
    print("TEST#{} Spiral List : {}".format(tno, sp))

    tno += 1
    debug = False
    amatrix = [[1,2,3],
               [10,11,4],
               [9,12,5],
               [8,7,6]]

    mat = matrix(amatrix, debug)
    print("TEST#{} Original Matrix:")
    mat.print()
    sp = mat.spiral_form()
    print("TEST#{} Spiral List : {}".format(tno, sp))

    tno += 1
    debug = False
    amatrix = [[1,2,3,4,5],
               [16,17,18,19,6],
               [15,24,25,20,7],
               [14,23,22,21,8],
               [13,12,11,10,9]]

    mat = matrix(amatrix, debug)
    print("TEST#{} Original Matrix:")
    mat.print()
    sp = mat.spiral_form()
    print("TEST#{} Spiral List : {}".format(tno, sp))

