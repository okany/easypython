# This script sorts a list of colors 0, 1, and 2 in minimum number of
# swaps (O(N) complexity)
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
#
class colorsort():
    def __init__(self, clist):
        self.clist = clist.copy()
        self.inds = [-1, -1, -1]
    def sort(self):
        self.inds = [-1, -1, -1]
        for ind in range(len(self.clist)):
            if self.clist[ind] == 2:
                # increase the end index of color 2 - no need to do anything else
                self.inds[2] += 1
            elif self.clist[ind] == 1:
                # increase the end index of color 1
                self.inds[1] += 1
                # swap the current with first element with color 2
                tmp = self.clist[self.inds[1]]
                self.clist[self.inds[1]] = self.clist[ind]
                self.clist[ind] = tmp
                # increase the end index of color 2
                self.inds[2] += 1
            elif self.clist[ind] == 0:
                # increase the end index of color 0
                self.inds[0] += 1
                tmp = self.clist[self.inds[0]]
                # insert the current toe end of color 0
                self.clist[self.inds[0]] = self.clist[ind]
                # increase the end index of color 1
                self.inds[1] += 1
                # move the first color 1 to the position o
                self.clist[ind] = self.clist[self.inds[1]]
                self.clist[self.inds[1]] = tmp
                self.inds[2] += 1

if __name__ == "__main__":

    colors = [1, 2, 2, 0, 1, 2, 0, 0, 0, 2, 1, 1, 0, 2]
    cs = colorsort(colors)
    cs.sort()
    print("TEST #1 - sorted list of colors in list {} is {}".format(colors, cs.clist))

    colors = [2,2,2,1,1,2,2,2,2,2,1,1,1,2,1]
    cs = colorsort(colors)
    cs.sort()
    print("TEST #2 - sorted list of colors in list {} is {}".format(colors, cs.clist))

    colors = [0,0,0,0,0,0,0,0,0,0]
    cs = colorsort(colors)
    cs.sort()
    print("TEST #3 - sorted list of colors in list {} is {}".format(colors, cs.clist))

    colors = [2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
    cs = colorsort(colors)
    cs.sort()
    print("TEST #4 - sorted list of colors in list {} is {}".format(colors, cs.clist))



