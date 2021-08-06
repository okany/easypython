# This script inserts a new interval into a list of intervals which are
# non-overlapping and sorted based on start times
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright [c] 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# [at your option] any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
def insert_interval(intlist, interval, debug = False):
    
    if intlist == []:
        intlist.append[interval]
        return
    
    minint = 0
    maxint = len(intlist) - 1
    curint = ((maxint - minint) >> 1) + minint
    start = end = -1
    # first search for the start of the new interval
    target = interval[0]
    state = "start"
    while state != "found" and state != "nointer":
        if debug:
            print("minint={} maxint={} curint={} state={}".format(minint, maxint, curint, state))
        if intlist[curint][1] < target:
            # search the right side
            minint = curint + 1
        elif intlist[curint][0] > target:
            # search the left side
            maxint = curint - 1

        elif intlist[curint][0] <= target:
            # found the target intersection
            if state == "start":
                target = interval[1]
                if intlist[curint][1] >= target:
                    # we found the solution
                    state = "found"
                    start = end = curint
                else:
                    start = curint
                    minint = curint + 1
                    state = "end"
                    maxint = len(intlist) - 1
            elif state == "end":
                # we found the solution
                state = "found"
                end = curint
        
        if minint > maxint:
            if state == "start":
                target = interval[1]
                start = minint
                if start >= len(intlist) or intlist[start][0] > target:
                    state = "nointer"
                else:
                    intlist[start][0] = interval[0]
                    state = "end"
                    maxint = len(intlist) - 1
            else:
                # we found the solution
                state = "found"
                end = curint

        if(state in ["start", "end"]):
            curint = ((maxint - minint) >> 1) + minint

    if debug:
        print("minint={} maxint={} curint={} state={} start={}".format(minint, maxint, curint, state, start))
    if state == "nointer":
        if start > 0 and (interval[0] <= (intlist[start-1][1]+1)):
            if start < len(intlist) and interval[1] >= (intlist[start][0] - 1):
                intlist[start-1][1] = intlist[start][1]
                intlist.pop(start)
            else:
                intlist[start-1][1] = interval[1]
        elif start < len(intlist) and interval[1] >= (intlist[start][0]-1):
            intlist[start][0] = interval[0]
        else:
            intlist.insert(start, interval)
    else:
        intlist[start][1] = intlist[end][1]
        for i in range(end-start):
            intlist.pop(start+1)
            
if __name__=="__main__":

    tn = 0

    tn += 1
    debug = False
    intlist = [[1,2], [4, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [20, 87]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[1, 2], [4, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [66, 69]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[1, 2], [4, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [52, 55]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[3, 4], [5, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [1, 2]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[3, 4], [5, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [1, 4]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[3, 4], [5, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94],
               [96, 99]]
    interval = [1, 18]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[4, 5], [6, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [1, 2]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[3, 4], [5, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [100, 105]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))

    tn += 1
    debug = False
    intlist = [[3, 4], [5, 7], [10, 15], [19, 26], [30, 40], [45, 50], [57, 65], [70, 77], [80, 82], [85, 90], [92, 94], [96, 99]]
    interval = [101, 105]

    print("TEST#{} Original list = {} \n       Interval      = {}".format(tn, intlist, interval))
    insert_interval(intlist, interval, debug)
    print("       Merged list   = {}".format(intlist))
