# This script finds if the list A with sorted integers have 2 indices such that
# A[i] - A[j] = k where k is a positive integer and i != j (time optimized)
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
class Solution(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.aset = set()
        for each in self:
            if each not in self.aset:
                self.aset.add(each)

    def diffPossible(self, k):
        for each in self:
            if (each + k) in self.aset:
                return True
        return False

if __name__ == '__main__':

    alist = [1, 4, 7, 9, 10, 12, 15]

    sol = Solution(alist)
    tnum = 0

    k = 5
    tnum += 1
    print("TEST#{}: diffk is {} for list = {} and k = {}".format(tnum, sol.diffPossible(k), alist, k))

    k = 7
    tnum += 1
    print("TEST#{}: diffk is {} for list = {} and k = {}".format(tnum, sol.diffPossible(k), alist, k))

    k = 9
    tnum += 1
    print("TEST#{}: diffk is {} for list = {} and k = {}".format(tnum, sol.diffPossible(k), alist, k))

    k = 11
    tnum += 1
    print("TEST#{}: diffk is {} for list = {} and k = {}".format(tnum, sol.diffPossible(k), alist, k))

    k = 12
    tnum += 1
    print("TEST#{}: diffk is {} for list = {} and k = {}".format(tnum, sol.diffPossible(k), alist, k))
