# This script cuts a rod from the weak points of the rod in an order to minimize the rod cutting cost where
# cutting each rod costs the length of the rod
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright [c] 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# [at your option] any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

class rod(list):
    def __init__(self, rod, length, debug = False):
        self.debug = debug
        self.sol = dict()
        myrod = rod.copy()
        myrod.insert(0, 0)
        myrod.append(length)
        super().__init__(myrod)

    def cut(self, lpoint, rpoint):
        dictkey = str(lpoint) + "-" + str(rpoint)

        if self.sol.get(dictkey) != None:
            return self.sol[dictkey][0],self.sol[dictkey][1]

        thiscost = self[rpoint] - self[lpoint]
        cost = (rpoint-lpoint) * thiscost
        if self.debug:
            print("calculating cutting the rod between {} and {} points. Thiscost = {} and cost = {}".
                  format(lpoint, rpoint, thiscost, cost))

        order = list()
        if lpoint == rpoint - 1:
            cost = 0
        elif lpoint == rpoint - 2:
            cost = thiscost
            order.append(rpoint-1)
        else:
            for cp in range(lpoint+1, rpoint):
                lcost, lorder = self.cut(lpoint, cp)
                rcost, rorder = self.cut(cp, rpoint)
                cpcost = lcost + rcost + thiscost

                if cpcost < cost:
                    order = list()
                    order.append(cp)
                    order.extend(lorder)
                    order.extend(rorder)
                    cost = cpcost

        if self.debug:
            print("thiscost={} cost={}".format(thiscost, cost))

        self.sol[dictkey] = [cost, order]

        return cost, order

    def cut_rod(self):
        cost = 0
        order = list()
        cost, order = self.cut(0, len(self) - 1)
        if self.debug:
            print("cost={} order={}".format(cost, order))
            print("solution table = {}".format(self.sol))
        return(cost, order)

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    rodpts = [7]
    rodlen = 13

    rodobj = rod(rodpts, rodlen, debug)

    cost, order = rodobj.cut_rod()

    print("TEST#{} - Cutting the rod {} in the order {} results the min cost of {}".format(tno, rodpts, order, cost))

    tno += 1
    debug = False
    rodpts = [2, 12]
    rodlen = 15

    rodobj = rod(rodpts, rodlen, debug)

    cost, order = rodobj.cut_rod()

    print("TEST#{} - Cutting the rod {} in the order {} results the min cost of {}".format(tno, rodpts, order, cost))

    tno += 1
    debug = False
    rodpts = [2, 4, 5, 7, 10, 12]
    rodlen = 15

    rodobj = rod(rodpts, rodlen, debug)

    cost, order = rodobj.cut_rod()

    print("TEST#{} - Cutting the rod {} in the order {} results the min cost of {}".format(tno, rodpts, order, cost))

    tno += 1
    debug = False
    rodpts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    rodlen = 15

    rodobj = rod(rodpts, rodlen, debug)

    cost, order = rodobj.cut_rod()

    print("TEST#{} - Cutting the rod {} in the order {} results the min cost of {}".format(tno, rodpts, order, cost))

    rodpts = [1, 2, 3, 4, 5, 6, 9, 10, 11, 13, 14, 21, 23, 25, 26, 30, 31, 34, 41, 42, 45, 46, 49, 60, 61, 63, 64, 71, 73, 75, 76, 80, 81, 84, 91, 92, 93, 94, 95, 96, 99]
    rodlen = 100

    rodobj = rod(rodpts, rodlen, debug)

    cost, order = rodobj.cut_rod()

    print("TEST#{} - Cutting the rod {} in the order {} results the min cost of {}".format(tno, rodpts, order, cost))

