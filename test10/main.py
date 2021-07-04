# How do you print the first non-repeated character from a string?
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

class firstnrep(str):
    def __init__(self, astr):
        self.set = set()
        self.first = ""
        self = astr

    def firstnon(self):
        self.first = ""
        for char in self[::-1]:
            if char not in self.set:
                self.set.add(char)
                self.first = char

        return self.first

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    astr = "sdklklrtiojkeksrdll"

    fnrs = firstnrep(astr)
    print("First Non-repeated char= {}".format(fnrs.firstnon()))