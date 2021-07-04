# check if 2 strings are rotation of each other
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

class stringrot():
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def isrotate(self):
        retval = False
        if(len(self.str2) != len(self.str1)):
            pass
        elif(len(self.str1) == 1):
            retval = True
        else:
            tstr = self.str2
            for i in range(len(self.str2)):
                if(self.str1 == tstr):
                    retval = True
                    break
                else:
                    tstr = tstr[1:] + tstr[0]
        return retval

if __name__ == "__main__":
    str1="12312312434t5egfdfvdfopvkfsdocklkxcoksofpwkslck,elrrfgopepoefp;l;sc,lvl;s"
    str2="fpwkslck,elrrfgopepoefp;l;sc,lvl;s12312312434t5egfdfvdfopvkfsdocklkxcokso"

    sr = stringrot(str1,str2)

    print("Is rotate? = ",sr.isrotate())