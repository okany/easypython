# This script rearranges a list such that A[i] becomes A[A[i]] where A[i] has
# N elements such that 0<=A[i]<=N-1
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

class rlist(list):
    def __init__(self, alist):
        super().__init__(alist)
    def rearrange(self):
        num = 0
        while num < len(self):
            if self[num] != num:
                # swap num and self[num]
                tmp = self[num]
                self[num] = self[tmp]
                self[tmp] = tmp
            else:
                num += 1

if __name__=="__main__":

    alist = [ 3, 5, 6, 2, 1, 0, 7, 9, 10, 15, 12, 14, 11, 4, 8, 13]

    rl = rlist(alist)
    rl.rearrange()

    print("rearranged {} is {}".format(alist, rl))