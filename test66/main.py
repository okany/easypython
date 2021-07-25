# This script calculates the nth integer in "count and say" list
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
class countandsay():
    def __init__(self):
        self.nlist = ["1"]

    def get_next(self):
        cur = self.nlist[-1]
        ind = 0
        next = ""
        while ind < len(cur):
            # read the current number
            cnum = cur[ind]
            # set the count to 1
            count = 0
            while ind < len(cur) and cur[ind] == cnum:
                # count the consecutive nums
                ind += 1
                count +=1
            next = next + str(count) + str(cnum)

        return next

    def find_nth(self, num):
        while len(self.nlist) < num:
            next = self.get_next()
            self.nlist.append(next)

        return (self.nlist[num-1])

if __name__=="__main__":

    num = 10
    cas = countandsay()
    print("TEST#1 - {}th number in the list {} is {}".format(num, cas.nlist, cas.find_nth(num)))
    num = 1
    print("TEST#2 - {}st number in the list {} is {}".format(num, cas.nlist, cas.find_nth(num)))
    num = 25
    print("TEST#3 - {}th number in the list {} is {}".format(num, cas.nlist, cas.find_nth(num)))

