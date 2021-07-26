# This script finds the length of the shortest string to be appended to turn
# a string into a palindrome
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
class create_palindrome():
    def __init__(self, astr):
        self.astr = astr

    def ispalindrome(self, checkstr):
        # print(checkstr)
        for i in range(len(checkstr) >> 1):
            if checkstr[i] != checkstr[len(checkstr)-i-1]:
                return False
        return True

    def find_min_append(self):
        for i in range(len(self.astr)):
            if(self.ispalindrome(self.astr[i:])):
                return i
        return 0

if __name__=="__main__":

    astr = "abcdefghijklkjihg"
    cp = create_palindrome(astr)
    print("TEST #1 - To convert {} into a palindrome at least {} characters need to be appended".
          format(astr, cp.find_min_append()))

    astr = "abcdefghijkllllllkjihg"
    cp = create_palindrome(astr)
    print("TEST #2 - To convert {} into a palindrome at least {} characters need to be appended".
          format(astr, cp.find_min_append()))

    astr = "a"
    cp = create_palindrome(astr)
    print("TEST #3 - To convert {} into a palindrome at least {} characters need to be appended".
          format(astr, cp.find_min_append()))

    astr = ""
    cp = create_palindrome(astr)
    print("TEST #4 - To convert {} into a palindrome at least {} characters need to be appended".
          format(astr, cp.find_min_append()))

    astr = "11111122222"
    cp = create_palindrome(astr)
    print("TEST #5 - To convert {} into a palindrome at least {} characters need to be appended".
          format(astr, cp.find_min_append()))

    astr = "111111111111111111"
    cp = create_palindrome(astr)
    print("TEST #6 - To convert {} into a palindrome at least {} characters need to be appended".
          format(astr, cp.find_min_append()))

    astr = "1111111111111111112"
    cp = create_palindrome(astr)
    print("TEST #7 - To convert {} into a palindrome at least {} characters need to be appended".
          format(astr, cp.find_min_append()))
