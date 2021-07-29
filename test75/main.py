# This script finds the majority element in a list
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
def majority_element(alist):
    majdict = dict()
    majno = int(len(alist) >> 1)
    # print(majno, len(alist))
    for item in alist:
        if item in majdict:
            # print("count for item {} is {} and mojority threshold is {}".format(item, majdict[item], majno))
            majdict[item] += 1
            if majdict[item] > majno:
                return item
        else:
            # print(item)
            # add the item to our counter dictionary
            majdict[item] = 1

    # if we reach here then there must be no majority element e.g. we have only N/2 or less # of items
    return None

if __name__=="__main__":

    tno = 0

    tno += 1
    alist = [1, 2, 1, 1, 1, 2, 2, 3, 2, 1, 1, 1, 2, 2, 2, 1, 1]

    print("TEST#{} majority element in list={} is {}".format(tno, alist, majority_element(alist)))

    tno += 1
    alist = [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1]

    print("TEST#{} majority element in list={} is {}".format(tno, alist, majority_element(alist)))

    tno += 1
    alist = [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2]

    print("TEST#{} majority element in list={} is {}".format(tno, alist, majority_element(alist)))
