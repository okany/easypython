# check if a string has all digits
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

class digitstr(str):

    def __init__(self, astr):
        self = astr

    def alldigits(self):
        if self == "": return False
        else: return(self.checkdig(self))

    def checkdig(self, astr):
        if(astr == ""):
            return True
        elif(astr[0].isdigit()):
            return self.checkdig(astr[1:])
        else:
            return False

if __name__ == '__main__':

    astr = digitstr("23423423y5")
    print("alldigit? = ", astr.alldigits())
