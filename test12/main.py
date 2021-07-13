# This script finds the median of an array which is created by merging two sorted arrays
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
class median_array():
    def __init__(self, l1, l2):
        if(len(l1)>=len(l2)):
            self.l1 = l1
            self.l2 = l2
        else:
            self.l1 = l2
            self.l2 = l1

        self.median = None

    def iseven(self, anum):
        if anum == (anum >> 1) * 2:
            # totlen is even
            return True
        else:
            return False

    def find_median(self):

        med2 = len(self.l2) >> 1
        totlen = len(self.l1)+len(self.l2)
        even = self.iseven(totlen)
        med = ((totlen+1) >> 1) - 1
        med1 = med - med2 - 1
        soln = sol1 = sol2 = None

        # handle special cases that l1 and l2 has no intersections
        if (self.l2[0] >= self.l1[-1]):
            soln = sol1 = self.l1[med]
            if even:
                if med+1 == len(self.l1):
                    sol2 = self.l2[0]
                else:
                    sol2 = self.l1[med + 1]
                soln = (sol1 + sol2) / 2

            return soln
        elif (self.l2[-1]<=self.l1[0]):
            if(med < len(self.l2)):
                soln = sol1 = self.l2[med]
                if even:
                    sol2 = self.l1[0]
                    soln = (sol1 + sol2) / 2
            else:
                soln = sol1 = self.l1[med - len(self.l2)]
                if even:
                    sol2 = self.l1[med - len(self.l2) + 1]
                    soln = (sol1 + sol2) / 2

            return soln

        # print("med1={} med2={} total length={} median={}".format(med1, med2, totlen, med))

        # set the search area in the shorter array
        if self.l1[med1] > self.l2[med2]:
            min2 = med2
            max2 = len(self.l2) - 1
        else:
            min2 = 0
            max2 = med2

        while True:
            if self.l1[med1] > self.l2[med2]:
                # print("med1={} at {} med2={} at {} min2 {} max2 {}".
                #      format(self.l1[med1], med1, self.l2[med2], med2, min2, max2))
                if(self.l1[med1] < self.l2[med2+1]):
                    # we found the median or exhausted one of the arrays
                    break
                min2 = med2+1
                if (min2 > max2):
                    # we hit the max or min of l2
                    break
                move = (max2 - min2) + 1 >> 1
                # print("move={}".format(move))
                med1 -= move
                med2 += move
            elif self.l1[med1] < self.l2[med2]:
                # print("med1={} at {} med2={} at {} min2 {} max2 {}".
                #      format(self.l1[med1], med1, self.l2[med2], med2, min2, max2))
                if(self.l1[med1+1] > self.l2[med2]):
                    # we found the median or exhausted one of the arrays
                    break
                max2 = med2-1
                if (min2 > max2):
                    # we hit the max or min of l2
                    break
                move = (max2 - min2) + 1 >> 1
                # print("move={}".format(move))
                med1 += move
                med2 -= move
            else:
                # we found the median
                break

        # we exhausted all items in array 2
        # search for solution in array 1
        if self.l2[med2] >= self.l1[med1]:
            sol1 = self.l2[med2]
        else:
            sol1 = self.l1[med1]
        soln  = sol1
        # print ("solution1 is {} ".format(sol1))

        if even:
            if med2+1 < len(self.l2) and self.l2[med2 + 1] < self.l1[med1 + 1]:
                sol2 = self.l2[med2 + 1]
            else:
                sol2 = self.l1[med1 + 1]
            soln = (sol1+sol2)/2

        # print ("solution2 is {} ".format(sol2))
        # print ("final solution is {} ".format(soln))

        return soln

if __name__ == '__main__':
    l1 = [2, 5, 25, 37, 50, 66, 71, 72, 80, 91, 92, 100]
    l2 = [75, 77, 79, 84, 86, 105, 107, 110]

    ma = median_array(l1, l2)

    med = ma.find_median()

    print("TEST#1 - median of A1 {} and A2 {} is {}".format(l1, l2, med))

    l1 = [2, 5, 25, 37, 50, 66, 71, 72, 80, 91, 92, 100]
    l2 = [75, 77, 79, 84, 86, 105, 107, 110, 120]

    ma = median_array(l1, l2)

    med = ma.find_median()

    print("TEST#2 - median of A1 {} and A2 {} is {}".format(l1, l2, med))
    l1 = [2]
    l2 = [75]

    ma = median_array(l1, l2)

    med = ma.find_median()

    print("TEST#3 - median of A1 {} and A2 {} is {}".format(l1, l2, med))
    l1 = [20]
    l2 = [20]

    ma = median_array(l1, l2)

    med = ma.find_median()

    print("TEST#4 - median of A1 {} and A2 {} is {}".format(l1, l2, med))

    l1 = [20]
    l2 = [20, 21]

    ma = median_array(l1, l2)

    med = ma.find_median()

    print("TEST#5 - median of A1 {} and A2 {} is {}".format(l1, l2, med))

    l1 = [10, 18]
    l2 = [20, 30, 40, 45]

    ma = median_array(l1, l2)

    med = ma.find_median()

    print("TEST#6 - median of A1 {} and A2 {} is {}".format(l1, l2, med))
