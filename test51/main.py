# Find duplicate characters in a string
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

class stringdups(str):
    def __init__(self, astr):
        self.strdict = dict()
        self.strdups = []
        self = astr

    def finddups(self):
        for char in self:
            if self.strdict.get(char) == None:
                self.strdict[char] = 1
            else:
                self.strdict[char] = self.strdict[char] + 1
                if self.strdict[char] == 2:
                    self.strdups.append(char)

        return(self.strdups)


if __name__ == "__main__":
    str1 = "2293049o055776276122-059068607867874860-60940487827628a78478876969708t0-78-08-50498398201u9182a989o85095079089-"

    sd1 = stringdups(str1)
    print("DUPS1 = {}".format(sd1.finddups()))

    str2 = ""

    sd2 = stringdups(str2)
    print("DUPS2 = {}".format(sd2.finddups()))
