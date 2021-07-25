# This script computes and returns the square root of integer A as
# floor(sqrt(A)) where 1<=A<=10^9
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
def sqrt(num):
    # shift num + 1 to cover num = 1 case as well
    start = (num+1) >> 1
    # find the number to start the search
    while start * start > num:
        # print("start = {}".format(start))
        start = start >> 1

    # start is our default solution
    test = start
    end = (start << 1) - 1
    # print ("start = {} end = {}".format(start, end))

    while end > start:
        # print ("start = {} end = {}".format(start, end))
        # now do binary search between start and end
        test = ((end - start) >> 1) + start + 1
        sqr = test * test
        if sqr > num:
            # set end and test to test -1 as test cannot be a solution
            test = end = test-1
        elif sqr < num:
            # set start to test as test can be a solution
            start = test
        else:
            # bingo - we found the number
            break
    return test

if __name__=="__main__":

    num = 12340050
    print("TEST#1 - square root of {} is {}".format(num, sqrt(num)))

    num = 10 ** 9 # this is the max in the problem definition
    print("TEST#2 - square root of {} is {}".format(num, sqrt(num)))

    # test 3 consecutive numbers to verify the sensitivity of the sort function
    num = 999950884
    print("TEST#3 - square root of {} is {}".format(num, sqrt(num)))

    num = 999950883
    print("TEST#4 - square root of {} is {}".format(num, sqrt(num)))

    num = 999950885
    print("TEST#5 - square root of {} is {}".format(num, sqrt(num)))

    num = 1 # this is an important corner case to cover
    print("TEST#6 - square root of {} is {}".format(num, sqrt(num)))

    num = 2
    print("TEST#7 - square root of {} is {}".format(num, sqrt(num)))
