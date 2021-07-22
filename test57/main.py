# This script finds a substring in a string
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
class strstr(str):
    def __init__(self, astr):
        super().__init__()
        self = astr

    def compare(self, ind, substr):
        retval = True
        for sind in range(len(substr)):
            if self[ind+sind] != substr[sind]:
                retval = False

        return retval

    def findstr(self, substr):
        index = -1
        if self == "" or substr == "":
            pass
        else:
            for ind in range(len(self)-len(substr)+1):
                if self.compare(ind, substr):
                    index = ind
                    break

        return index

if __name__=="__main__":

    astr = "asbnbenraaaaaalkqweqe"
    substr = "aaalkq"

    st = strstr(astr)
    ind = st.findstr(substr)
    if(ind <0):
        print("TEST#1 - substr {} does not exist in {} ".format(substr, astr))
    else:
        print("TEST#1 - substr {} exists in {} at starting index {}".format(substr, astr, ind))

    astr = ""
    substr = "aaalkq"

    st = strstr(astr)
    ind = st.findstr(substr)
    if(ind <0):
        print("TEST#2 - substr {} does not exist in {} ".format(substr, astr))
    else:
        print("TEST#2 - substr {} exists in {} at starting index {}".format(substr, astr, ind))

    astr = "asbnbenraaaaaalkqweqe"
    substr = ""

    st = strstr(astr)
    ind = st.findstr(substr)
    if(ind <0):
        print("TEST#3 - substr {} does not exist in {} ".format(substr, astr))
    else:
        print("TEST#3 - substr {} exists in {} at starting index {}".format(substr, astr, ind))

    astr = "abcdefghijk"
    substr = "abcdefghijkl"

    st = strstr(astr)
    ind = st.findstr(substr)
    if(ind <0):
        print("TEST#4 - substr {} does not exist in {} ".format(substr, astr))
    else:
        print("TEST#4 - substr {} exists in {} at starting index {}".format(substr, astr, ind))

    astr = "abcdefghijk"
    substr = "abcdefghijk"

    st = strstr(astr)
    ind = st.findstr(substr)
    if(ind <0):
        print("TEST#5 - substr {} does not exist in {} ".format(substr, astr))
    else:
        print("TEST#5 - substr {} exists in {} at starting index {}".format(substr, astr, ind))
