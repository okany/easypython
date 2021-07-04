# How can a given string be reversed using recursion?
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

class rstr(str):
    def __init__(self, astr):
        self = astr

    def reverse(self):
        return(self.reversestr(self))

    def reversestr(self, astr):
        if(astr == "" or len(astr) == 1):
            return astr
        else:
            return(self.reversestr(astr[1:]) +  astr[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    astr = rstr("jwekjrkwjekrbmsndmfnsmdf")
    print("TEST#1 - reverse of string {} is {} ".format(astr, astr.reverse()))

    bstr = rstr("")
    print("TEST#2 - reverse of string {} is {} ".format(bstr, bstr.reverse()))

    cstr = rstr("2")
    print("TEST#3 - reverse of string {} is {} ".format(cstr, cstr.reverse()))

