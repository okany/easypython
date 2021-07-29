# This script finds the maximum length of list of disjoint intervals
# for a given list of intervals
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
class intervals():
    def __init__(self, intervals):
        self.ints = intervals
        self.intcnt = [[i,0, list()] for i in range(len(self.ints))]
        self.int_list = list()
        self.disints = list()

    def set_inter_count(self, i):
        for j in range(i+1, len(self.ints)):
            if self.ints[i][0] == self.ints[j][0] or self.ints[i][1] >= self.ints[j][0]:
                self.intcnt[i][1] += 1
                self.intcnt[i][2].append(j)
                self.intcnt[j][1] += 1
                self.intcnt[j][2].append(i)

    def find_max_inter(self):
        max = 0
        if self.int_list == []:
            return None
        for i in range(len(self.int_list)):
            if self.int_list[i][1] > self.int_list[max][1]:
                max = i
        return self.int_list[max]

    def insert_inter_list(self, item):
        i = 0
        while i < len(self.int_list):
            if self.int_list[i][1] < item[1]:
                break
            i += 1
        self.int_list.insert(i, item)

    def remove_inter_list(self, item):
        for other in item[2]:
            self.intcnt[other][1] -= 1
            self.intcnt[other][2].remove(item[0])
            if(self.intcnt[other][1] == 0):
                self.disints.append(self.ints[self.intcnt[other][0]])
                self.int_list.remove(self.intcnt[other])
        # print("item={}".format(item))
        self.int_list.remove(item)
        return

    def find_disjoint_intervals(self):
        self.disints = list()
        for i in range(len(self.ints)):
            # count the number of intersections
            self.set_inter_count(i)
            if self.intcnt[i][1] == 0:
                self.disints.append(self.ints[i])
            else:
                self.insert_inter_list(self.intcnt[i])

        # print("self.intcnt={}".format(self.intcnt))
        # print("self.inter_list={}".format(self.int_list))

        item = self.find_max_inter()
        while item != None:
            self.remove_inter_list(item)
            # print("self.inter_list={}".format(self.int_list))
            item = self.find_max_inter()

        return self.disints

if __name__=="__main__":

    tno = 0
    tno += 1
    alist = [[1,3],[2,5],[3,6],[5,9],[10,12],[12,15],[14,19],[20, 22]]
    aint = intervals(alist)
    print("TEST#{} - for alist={} disjoint intervals={}".format(tno, alist, aint.find_disjoint_intervals()))

    tno += 1
    alist = [[1, 3], [4, 5], [5, 8], [6, 8], [7, 8], [8, 9], [9, 12], [10, 14]]
    aint = intervals(alist)
    print("TEST#{} - for alist={} disjoint intervals={}".format(tno, alist, aint.find_disjoint_intervals()))

    tno += 1
    alist = [[1, 3], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 12], [10, 14], [15, 17], [18, 19]]
    aint = intervals(alist)
    print("TEST#{} - for alist={} disjoint intervals={}".format(tno, alist, aint.find_disjoint_intervals()))

