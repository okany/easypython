# This script checks if a string is palindrome or not
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

class pstr(str):
    def __init__(self, astr):
        self = astr

    def ispalindrome(self):
        for i in range(int(len(self)/2)):
            if(self[i] != self[len(self)-i-1]):
                return False
        return True

if __name__ == "__main__":

    pstr1 = pstr("123454321")
    print("String {} is Palindrome = {}".format(pstr1, pstr1.ispalindrome()))

    pstr2 = pstr("123456654321")
    print("String {} is Palindrome = {}".format(pstr2, pstr2.ispalindrome()))

    pstr3 = pstr("123454354321")
    print("String {} is Palindrome = {}".format(pstr3, pstr3.ispalindrome()))
