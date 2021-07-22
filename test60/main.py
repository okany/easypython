# This script finds if the list A with sorted integers have 2 indices such that
# A[i] - A[j] = k where k is a positive integer and i != j
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
class diffk(list):
    def __init__(self, alist):
        super().__init__(alist)

    def get_pos_diff(self, num):
        if len(self) < 2:
            return 0
        lower = 1
        for i in range(len(self)):
            j = lower
            while j < len(self):
                dif = abs(self[j] - self[i]) # can be sorted ascending or descending abs covers both
                # print ("i = {} j = {} lower = {} dif = {} num = {}".format(i, j, lower, dif, num))
                if dif == num:
                    # found indices which satisfy the rule
                    #  A[j] - A[i] = k
                    return 1
                elif dif < num:
                    # dif is short so increase the lower so don't try the same numbers again when i increases
                    j += 1
                    lower = j
                else: # dif > num - no need to continue or modify the lower, just break
                    break
        return 0

if __name__ == "__main__":

    arr = [4, 5, 6, 7, 9, 10, 11, 12]

    k = 9
    dk = diffk(arr)

    print("TEST#1 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
    k = 8
    print("TEST#2 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))

    arr = [4, 5, 7, 10, 14, 20, 30, 42]
    k = 7
    dk = diffk(arr)
    print("TEST#3 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
    k = 39
    print("TEST#4 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
    k = 38
    print("TEST#5 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
    k = 20
    print("TEST#6 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
    k = 12
    print("TEST#7 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
    k = 1
    print("TEST#8 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
    k = 8
    print("TEST#9 - arr = {} k = {} diffk = {} ".format(arr, k, dk.get_pos_diff(k)))
