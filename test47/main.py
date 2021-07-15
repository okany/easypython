# This script calculates combination sum of a set of numbers (C) such that sum equals to target number (T)
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
def find_combination_sums(cnums, t):
    cnums.set_t(t)
    sollist = cnums.find_com_sums(0, 0, [])
    return sollist

class comb_nums(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.t = None

    def set_t(self, t):
        self.t = t

    def find_com_sums(self, tot, start, alist):
        sollist = []
        for i in range(start, len(self)):
            # print("tot is {} i is {} alist is {}".format(tot, self[i], alist))
            if self[i]+tot > self.t:
                break
            elif self[i]+tot == self.t:
                blist = alist.copy()
                blist.append(self[i])
                sollist.append(blist)
                # print ("alist = {}".format(blist))
                break
            else:
                blist = alist.copy()
                blist.append(self[i])
                soln = self.find_com_sums(tot+self[i], i, blist)
                sollist.extend(soln)

        return sollist

if __name__ == "__main__":

    alist = [1 ,2 ,3, 5, 7, 9, 12, 15]
    cn = comb_nums(alist)
    num = 9
    sl = find_combination_sums(cn, num)

    print("TEST#1 solution list for list {} and number {} is {}".format(alist, num, sl))

    alist = [1 ,2 ,3, 5, 7, 9, 12, 15, 30, 50, 70]
    cn = comb_nums(alist)
    num = 1
    sl = find_combination_sums(cn, num)

    print("TEST#2 solution list for list {} and number {} is {}".format(alist, num, sl))

    alist = [1 ,2 ,3, 5, 7, 9, 12, 15, 30, 50, 70]
    cn = comb_nums(alist)
    num = 16
    sl = find_combination_sums(cn, num)

    print("TEST#3 solution list for list {} and number {} is {}".format(alist, num, sl))

    alist = [1 ,2 ,3, 5, 7, 9, 12, 15, 30, 50, 70]
    cn = comb_nums(alist)
    num = 14
    sl = find_combination_sums(cn, num)

    print("TEST#3 solution list for list {} and number {} is {}".format(alist, num, sl))
