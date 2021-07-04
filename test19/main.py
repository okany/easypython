# This script finds all combinations of a string
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

class strcomb(str):
    def __init__(self, astr):
        self.comb = []
        self = astr

    def findallcombs(self):
        self.findcombs(self)
        return(self.comb)

    def findcombs(self, astr):
        if astr == "": pass
        elif len(astr) == 1:
            self.comb.append(astr)
        else:
            bstr = strcomb(astr[1:])
            alcomb = bstr.findallcombs()
            for item in alcomb:
                for i in range(len(item)+1):
                    self.comb.append(item[:i]+astr[0]+item[i:])

# using a class makes the code complicated
# this is a utility function which does not use a class
def findcombs2(astr):
    if astr == []: pass #return empty list if the string is empty
    elif len(astr) == 1: #return a list with a single char string
        return [astr]
    else:
        # save hte first char and look for string combinations in the rest of the string
        alcomb = findcombs2(astr[1:])
        newcomb = []
        for item in alcomb:
            # include item + astr[0] as well
            for i in range(len(item)+1):
                newcomb.append(item[:i]+astr[0]+item[i:])
        return newcomb

if __name__ == "__main__":
    str1 = "abcde"
    st1 = strcomb(str1)

    alcombs = st1.findallcombs()
    print("Class version:")
    print("There are {} combinations: {}".format(len(alcombs), alcombs))

    alcombs2 = findcombs2(str1)
    print("Utility function version:")
    print("There are {} combinations: {}".format(len(alcombs2), alcombs2))
