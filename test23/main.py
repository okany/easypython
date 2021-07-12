# This script searches an integer in a presorted integer array which was
# rotated from an unknown pivot point (array has no duplicates)
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

class rotated_array(list):
    def __init__(self, alist):
        super().__init__(alist)

    def isrotated(self):
        if len(self) < 2:
            return False
        else:
            if self[0] < self[len(self)-1]:
                return False
            else:
                return True

    def find(self, anint):

        # print("self = {}".format(self))

        if self == []:
            return -1
        elif len(self) == 1:
            if self[0] == anint:
                return 0
            else:
                return -1
        elif not self.isrotated():
            if self[0] > anint or self[-1] < anint:
                return -1

        middle = len(self) >> 1

        ra1 = rotated_array(self[:middle])
        ra2 = rotated_array(self[middle:])

        # print("middle = {} ra1={} ra2={}".format(middle, ra1, ra2))

        ind = ra1.find(anint)
        if ind > -1:
            return ind
        else:
            ind = ra2.find(anint)
            if(ind > -1):
                return ind + middle

        return -1

if __name__ == "__main__":

    array = [93, 95, 97, 111, 123, 145, 2, 4, 5, 7, 10, 12, 25, 45, 53, 70, 89]

    ra = rotated_array(array)
    anum = 45
    index = ra.find(anum)
    print("TEST#1 - found {} in {} at index {}".format(anum, array, index))

    array = [15, 27, 42, 45, 93, 95, 97, 111, 123, 145, 2, 4, 5, 7, 10, 12]

    ra = rotated_array(array)
    anum = 45
    index = ra.find(anum)
    print("TEST#2 - found {} in {} at index {}".format(anum, array, index))

    array = [15, 27, 42, 45, 93, 95, 97, 111, 123, 145, 2, 4, 5, 7, 10, 12]

    ra = rotated_array(array)
    anum = 49
    index = ra.find(anum)
    print("TEST#3 - found {} in {} at index {}".format(anum, array, index))

    array = [15, 27, 42, 45, 93, 95, 97, 111, 123, 1, 2, 4]

    ra = rotated_array(array)
    anum = 123
    index = ra.find(anum)
    print("TEST#4 - found {} in {} at index {}".format(anum, array, index))

    array = []

    ra = rotated_array(array)
    anum = 5
    index = ra.find(anum)
    print("TEST#5 - found {} in {} at index {}".format(anum, array, index))

    array = [30, 10, 17, 25, 29]

    ra = rotated_array(array)
    anum = 29
    index = ra.find(anum)
    print("TEST#6 - found {} in {} at index {}".format(anum, array, index))

