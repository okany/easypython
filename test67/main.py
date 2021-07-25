# This script adds two binary strings
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
def add_bin_strs(str1, str2):
    result = ""
    str1ind = len(str1) - 1
    str2ind = len(str2) - 1
    overflow = 0
    while str1ind >= 0 or str2ind >= 0:
        str1num = 0
        str2num = 0
        if(str1ind >= 0 and str1[str1ind] == "1"):
            str1num = 1
        if(str2ind >= 0 and str2[str2ind] == "1"):
            str2num = 1
        sum = str1num + str2num + overflow

        if sum == 0 or sum == 1:
            result = str(sum) + result
            overflow = 0
        else:
            overflow = 1
            if sum == 2:
                # sum is 2
                result = "0" + result
            else:
                # sum is 3
                result = "1" + result
        str1ind -= 1
        str2ind -= 1

    if(overflow == 1):
        # insert another "1" for the remainder
        result = "1" + result

    return result

def get_decimal(numstr):
    num = 0
    power = 1
    for digit in numstr[::-1]:
        num = num + int(digit) * power
        power *= 2
        # print("digit={} and num={}".format(digit, num))

    return num

if __name__=="__main__":

    num1 = "10010101010111011"
    num2 = "111111000111010001111101111"
    sum = add_bin_strs(num1, num2)

    print ("TEST#1 - sum of {} ({}) and {} ({}) is {} ({})".
           format(num1, get_decimal(num1), num2, get_decimal(num2), sum, get_decimal(sum)))

    num1 = "111111111111111111111111111"
    num2 = "111111111111111111111111111"
    sum = add_bin_strs(num1, num2)

    print ("TEST#2 - sum of {} ({}) and {} ({}) is {} ({})".
           format(num1, get_decimal(num1), num2, get_decimal(num2), sum, get_decimal(sum)))

    num1 = "0"
    num2 = "0"
    sum = add_bin_strs(num1, num2)

    print ("TEST#3 - sum of {} ({}) and {} ({}) is {} ({})".
           format(num1, get_decimal(num1), num2, get_decimal(num2), sum, get_decimal(sum)))

    num1 = "1"
    num2 = "0"
    sum = add_bin_strs(num1, num2)

    print ("TEST#4 - sum of {} ({}) and {} ({}) is {} ({})".
           format(num1, get_decimal(num1), num2, get_decimal(num2), sum, get_decimal(sum)))

