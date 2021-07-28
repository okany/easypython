# This script finds the starting gas station of a list of gas stations
# to be able to travel all gas stations in listA
# where listA holds the available gas amounts and listB holds the gas
# cost of traveling from a gas station to the next one.
#
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
def circular_trip(listA, listB):
    cost = minc = maxc = 0
    firstmin = firstmax = 0
    start = -1
    # determine the final cost of each trip (A[i]-B[i+1]
    for station in range(len(listA)):

        # calculate the gas obtained from this station - trip to next
        thiscost = listA[station] - listB[station]
        # check if this is a local minima or local maxima
        if (cost * thiscost < 0):
            # reset the cost counter
            cost = thiscost
        else:
            cost += thiscost

        if thiscost < 0:
            # set the starting station to be used later
            start = station
        # sort the negative costs in a list
        if cost > maxc:
            maxstart = start + 1
            maxc = cost
        minc = min(minc, cost)

        # save the min as the first minimum to add it to last min for circular operation
        if maxc == 0:
            firstmin = minc
        # save the last min as the first maximum to add it the last max for circular operation
        elif minc == 0:
            firstmax = maxc
        # print("station={} minc{} maxc{}".format(station, minc, maxc))

    if cost > 0:
        cost += firstmax
        if cost > maxc:
            maxstart = start + 1
            maxc = cost
    elif cost < 0:
        cost += firstmin
        minc = min(cost, minc)

    if minc + maxc >= 0:
        return (maxstart % len(listA))
    else:
        return -1

if __name__=="__main__":

    tno = 0
    tno +=1
    alist = [1, 2, 1, 3, 2, 1, 2, 0]
    blist = [1, 1, 1, 2, 1, 2, 2, 3]

    print("TEST#{} - Gas amounts A={} and trip costs B={} circular trip starting from station {}".
          format(tno, alist, blist, circular_trip(alist, blist)))
    tno +=1
    alist = [1, 2, 1, 3, 2, 1, 2, 2]
    blist = [1, 1, 1, 2, 1, 2, 4, 1]
    print("TEST#{} - Gas amounts A={} and trip costs B={} circular trip starting from station {}".
          format(tno, alist, blist, circular_trip(alist, blist)))

    tno +=1
    alist = [1, 2, 1, 3, 2, 1, 2, 2]
    blist = [1, 1, 1, 2, 1, 4, 2, 1]
    print("TEST#{} - Gas amounts A={} and trip costs B={} circular trip starting from station {}".
          format(tno, alist, blist, circular_trip(alist, blist)))

    tno +=1
    alist = [0, 2, 1, 3, 2, 1, 2, 2]
    blist = [1, 1, 1, 2, 1, 4, 2, 1]
    print("TEST#{} - Gas amounts A={} and trip costs B={} circular trip starting from station {}".
          format(tno, alist, blist, circular_trip(alist, blist)))
