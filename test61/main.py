# This script finds 3 numbers with a sum closest to a given integer T
# in a list of integers S
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
class threesum():
    def __init__(self, alist):
        self.slist = alist
        self.dict = dict()
        self.slist.sort()

    def find3sum(self, num):
        solist = list()
        if len(self.slist) < 3:
            return None, solist
        sol = abs(self.slist[0] + self.slist[1] + self.slist[2] - num)
        solist = [self.slist[0], self.slist[1], self.slist[2]]
        for anum in range(len(self.slist)):
            bnum = anum+1
            lowc = bnum+1
            while bnum < len(self.slist):
                cnum = lowc = max(lowc, bnum+1)
                while cnum < len(self.slist):
                    # print("anum={}, bnum={}, cnum={}, lowc={}, sol={}".format(anum, bnum, cnum, lowc, sol))
                    tot = self.slist[anum] + self.slist[bnum] + self.slist[cnum] - num
                    if abs(tot) < abs(sol):
                        sol = tot
                        solist = [self.slist[anum], self.slist[bnum], self.slist[cnum]]
                        cnum += 1
                        if sol == 0:
                            return sol, solist
                    elif tot > abs(sol):
                        # there is no way to improve the solution by increasing cnum
                        break
                    elif tot < abs(sol):
                        cnum += 1
                        lowc = cnum
                    else:
                        cnum += 1
                bnum += 1
        return sol, solist

if __name__=="__main__":

    arr = [1, 5, -2, 3, -1, 16, 7, 9, 10, -5, -4, 12, 14]
    num = 16
    ts = threesum(arr)
    sol, solist = ts.find3sum(num)
    print("TEST#1 - arr = {}, num = {}, best sum = {} best sum list = {}".format(arr, num, sol, solist))
    num = 11
    sol, solist = ts.find3sum(num)
    print("TEST#2 - arr = {}, num = {}, best sum = {} best sum list = {}".format(arr, num, sol, solist))
    num = 32
    sol, solist = ts.find3sum(num)
    print("TEST#3 - arr = {}, num = {}, best sum = {} best sum list = {}".format(arr, num, sol, solist))
    num = 44
    sol, solist = ts.find3sum(num)
    print("TEST#4 - arr = {}, num = {}, best sum = {} best sum list = {}".format(arr, num, sol, solist))
    num = -15
    sol, solist = ts.find3sum(num)
    print("TEST#5 - arr = {}, num = {}, best sum = {} best sum list = {}".format(arr, num, sol, solist))
    num = -10
    sol, solist = ts.find3sum(num)
    print("TEST#6 - arr = {}, num = {}, best sum = {} best sum list = {}".format(arr, num, sol, solist))
    arr = [1, 5]
    num = 10
    ts = threesum(arr)
    sol, solist = ts.find3sum(num)
    print("TEST#7 - arr = {}, num = {}, best sum = {} best sum list = {}".format(arr, num, sol, solist))
