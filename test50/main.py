# This finds contiguous subarray within an array, A of length N which has the largest sum
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
class largest_sum(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.sublist = list()
        self.max = 0
        self.sum = 0

    def find_largest(self):
        for i in range(len(self)):
            self.sum += self[i]
            if self.sum < 0:
                self.sum = 0
            elif self.sum > self.max:
                self.max = self.sum
        return self.max

if __name__=="__main__":

    alist = [-5, -1, 7, -3, -2, -1, 6, 5, -7, -2, -1, 1, 8, 2]
    ls = largest_sum(alist)

    lsum = ls.find_largest()

    print("TEST#1 - sublist in the largest sum of list {} is {}".format(ls, lsum))

    alist = [-5, -1, 7, -3, -2, -1, 6, 5, -7, -2, -1, 1, 8, 2, -4, -5, 6, 5, -3, 4, 6, -1, 7]
    ls = largest_sum(alist)

    lsum = ls.find_largest()

    print("TEST#2 - sublist in the largest sum of list {} is {}".format(ls, lsum))

    alist = [-5, -1, 7, -3, -2, -1, 6, 5, -7, -2, -1, 1, 8, 2, -4, -5, 6, 5,
             -3, 4, 6, -1, 7, -10, -8, -12, 5, 6, 7, -1, 5, 7, -5, -3]
    ls = largest_sum(alist)

    lsum = ls.find_largest()

    print("TEST#3 - sublist in the largest sum of list {} is {}".format(ls, lsum))