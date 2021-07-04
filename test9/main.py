# this script determines if two strings are anagram or not
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

def isanogram(str1, str2):
    for char in str1:
        ind = str2.find(char)
        if ind >= 0:
            str2 = str2[0:ind] + str2[ind+1:]
        else:
            return (False)

    if str2 == "":
        return(True)

    return(False)

if __name__ == '__main__':
    str1 = "abcdefghau6uucdek"
    str2 = "abufdeccgha6dekuu"

    print("IS ANOGRAM=", isanogram(str1, str2))

