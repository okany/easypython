# This script manipulates a number string by adding a "*" between two
# consecutive even numbers and "-" between two consecutive odd numbers
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

class strmanup(str):
    def __init__(self, astr):
        super().__init__()
        self.offset = 0
        self = astr

    def isEven(self, i):
        return((int(self[i]) % 2) == 0)

    def isOdd(self, i):
        return((int(self[i]) % 2) != 0)

    def manupstr(self, offset):
        newstr = ""
        if(len(self)<offset):
            return self

        for i in range(len(self)-offset+1):
            newstr = newstr + self[i]
            if (self.isEven(i) and self.isEven(i+1)):
                newstr = newstr + "*"
            elif (self.isOdd(i) and self.isOdd(i+1)):
                newstr = newstr + "-"
        return newstr

if __name__ == '__main__':
    astr = "1235353565675675567889098"
    offset = 2

    strobj = strmanup(astr)

    print("NEWSTR=", strobj.manupstr(2))

