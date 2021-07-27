# This script finds all permutations of items in a list
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
def find_all_permutations(alist):
    # print("fiding perms of {}".format(alist))
    myperms = list()
    if(alist == None):
        return None
    elif alist == []:
        return myperms
    elif(len(alist)==1):
        myperms.append(alist)
        return myperms
    for i in range(len(alist)):
        blist = alist.copy()
        blist.pop(i)
        perms = find_all_permutations(blist)
        for perm in perms:
            ilist = [alist[i]]
            ilist.extend(perm)
            myperms.append(ilist)

    return myperms

if __name__=="__main__":

    tno = 0
    tno += 1
    alist = [1, 2, 3, 4, 5, 6]
    print("\nTEST#1 All permutations of list {} are:".format(alist))
    perms = find_all_permutations(alist)
    for each in perms:
        print("  {}".format(each))

    tno += 1
    alist = ['o', 'k', 'a', 'n']
    print("\nTEST#1 All permutations of list {} are:".format(alist))
    perms = find_all_permutations(alist)
    for each in perms:
        print("  {}".format(each))

    tno += 1
    alist = []
    print("\nTEST#1 All permutations of list {} are:".format(alist))
    perms = find_all_permutations(alist)
    for each in perms:
        print("  {}".format(each))

    tno += 1
    alist = None
    print("\nTEST#1 All permutations of list {} are:".format(alist))
    perms = find_all_permutations(alist)
    if alist == None:
        print("  {}".format(alist))
    else:
        for each in perms:
            print("  {}".format(each))
