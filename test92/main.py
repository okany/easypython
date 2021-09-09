# This finds subsets of a list of distinct integers and returns them
# in the non-descending order
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
class subsets(list):
    def __init__(self, alist, debug = False):
        if alist == None:
            raise ValueError
        super().__init__(alist)
        self.debug = debug
        self.subsets = list()
        self.sort()

    def find_subsets(self, alist):
        if self.debug:
            print("finding subsets {}".format(alist))
        # include empty list as the first solution
        rlist = [[]]
        for i in range(len(alist)):
            # find subsets of the list with integers greater than alist[i]
            subset_list = self.find_subsets(alist[i+1:])
            if self.debug:
                print("i = {} alist = {} ss = {}".format(i, alist, subset_list))
            for each in subset_list:
                rlist.append([alist[i]]+each)
            if self.debug:
                print("i = {} rlist = {}".format(i, rlist))
        return rlist

    def create_subset_list(self):
        self.subsets = self.find_subsets(self)

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False
    alist = None

    try:
        ss = subsets(alist, debug)
        ss.create_subset_list()

        print("TEST#{} subsets of {} are : {}".format(tno, ss, ss.subsets))
    except:
        print("TEST#{} received exception for list {}".format(tno, alist))

    tno += 1
    debug = False
    alist = []

    ss = subsets(alist, debug)
    ss.create_subset_list()

    print("TEST#{} subsets of {} are : {}".format(tno, ss, ss.subsets))

    tno += 1
    debug = False
    alist = [4, 3, 1, 2]

    ss = subsets(alist, debug)
    ss.create_subset_list()

    print("TEST#{} subsets of {} are : {}".format(tno, ss, ss.subsets))

    tno += 1
    debug = False
    alist = [45, 47, 33, 15, 20, 12, 13, 70, 56, 54]

    ss = subsets(alist, debug)
    ss.create_subset_list()

    print("TEST#{} subsets of {} are : {}".format(tno, ss, ss.subsets))


