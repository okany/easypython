# This script converts an integer N into a roman numeral where 1 < N < 4000
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
class roman():
    def __init__(self, num):
        self.rnum = ""
        self.num = num
        self.rmax = 4000
        self.r1000 = "M"
        self.d1000 = 1000

        self.d900 = 900
        self.r500 = "D"
        self.d500 = 500
        self.d400 = 400
        self.r100 = "C"
        self.d100 = 100

        self.d90 = 90
        self.r50 = "L"
        self.d50 = 50
        self.d40 = 40
        self.r10 = "X"
        self.d10 = 10

        self.d9 = 9
        self.r5 = "V"
        self.d5 = 5
        self.d4 = 4
        self.r1 = "I"
        self.d1 = 1


        if num < self.rmax:

            # process thousands
            if(self.num >= self.d1000):
                times = int(self.num / self.d1000)
                for i in range(times):
                    self.rnum = self.rnum + self.r1000
                self.num -= self.d1000 * times
            # process hundreds
            self.roman_helper(self.r1000, self.d900, self.r500, self.d500, self.d400, self.r100, self.d100)
            # process tens
            self.roman_helper(self.r100, self.d90, self.r50, self.d50, self.d40, self.r10, self.d10)
            # process ones
            self.roman_helper(self.r10, self.d9, self.r5, self.d5, self.d4, self.r1, self.d1)

    def roman_helper(self, r10x, d9x, r5x, d5x, d4x, r1x, d1x):
        if self.num >= d9x:
            self.rnum = self.rnum + r1x
            self.rnum = self.rnum + r10x
            self.num -= d9x
        elif self.num >= d5x:
            self.rnum = self.rnum + r5x
            self.num -= d5x
            times = int(self.num / d1x)
            for i in range(times):
                self.rnum = self.rnum + r1x
            self.num -= d1x * times
        elif self.num >= d4x:
            self.rnum = self.rnum + r1x
            self.rnum = self.rnum + r5x
            self.num -= d4x
        elif self.num >= d1x:
            times = int(self.num / d1x)
            for i in range(times):
                self.rnum = self.rnum + r1x
            self.num -= d1x * times

    # returns empty string if the numner is not in range (0, 4000)
    def get_rnum(self):
        return self.rnum

if __name__=="__main__":

    num = 945
    rm = roman(num)
    print("TEST#1 - decimal {} in roman numeral is {}".format(num, rm.get_rnum()))

    num = 834
    rm = roman(num)
    print("TEST#2 - decimal {} in roman numeral is {}".format(num, rm.get_rnum()))

    num = 421
    rm = roman(num)
    print("TEST#3 - decimal {} in roman numeral is {}".format(num, rm.get_rnum()))

    num = 3333
    rm = roman(num)
    print("TEST#4 - decimal {} in roman numeral is {}".format(num, rm.get_rnum()))

    num = 0
    rm = roman(num)
    print("TEST#5 - decimal {} in roman numeral is {}".format(num, rm.get_rnum()))

    num = 9500
    rm = roman(num)
    print("TEST#6 - decimal {} in roman numeral is {}".format(num, rm.get_rnum()))
