# This script finds starting position of substrings in a string S where
# each substring is a combination of all substrings provided in a list L
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

class subsinstring():
    def __init__(self, astr, sublist):
        self.str = astr
        self.sublist = sublist
        self.slist = []

        if(len(sublist) == 0):
            raise ValueError
        self.sublen = len(sublist[0])
        for each in sublist:
            if(len(each) != self.sublen):
                raise ValueError
            aset = set()
            # create a dictionary for each substring
            self.slist.append(aset)
            part = str(self.str)
            offset = 0
            ind = 0
            while ind >=0 and part and part != "":
                ind = part.find(each)
                if(ind >= 0):
                    offset = offset+ind
                    # print("found {} in {} at position {}".format(each, self.str, offset))
                    aset.add(offset)
                    offset = offset+1
                    part = str(part[ind+1:])

    def check_subs(self, used, index):
        if(len(used) == len(self.slist)):
            return True, used
        for i in range(len(self.slist)):
            if i not in used and index in self.slist[i]:
                # this is a possible solution so append i to used list and check the next index
                used.append(i)
                found, sol = self.check_subs(used, index+self.sublen)
                if(found):
                    return True, sol
        return False, []

    def find_subcombs(self):
        #make sure that all substrings are found in the string
        for i in range(len(self.slist)):
            if len(self.slist[i]) == 0:
                print("substring {} does not exist in {}".format(self.sublist[i], self.str))
                return False

        # keep the solutions in matchlist object in [stating index, substring order] format
        matchlist = []
        # check if you can find a substring of combination of all substrings in the string
        for i in range(len(self.slist)):
            for index in self.slist[i]:

                # starting from match index of sublist i
                used = [i]
                found, sol = self.check_subs(used, index+self.sublen)
                if found:
                    print ("found a string starting at {}".format(index))
                    matchlist.append(index)
        return matchlist

if __name__ == "__main__":

    print("TEST #1")
    try:
        sublist = ["foo", "bar", "man"]
        sis = subsinstring("barfoothefoobarmanbarfoo", sublist)
        matchlist = sis.find_subcombs()
        print("sublist is {}".format(matchlist))
    except ValueError:
        print ("Value Error is received")
    except:
        print ("Unknown error is received")

    print("\n\nTEST#2")

    try:
        sublist = ["foo", "bar", "man", "ball"]
        sis = subsinstring("barfoothefoobarmanbarfoo", sublist)
        matchlist = sis.find_subcombs()
        print("sublist is {}".format(matchlist))
    except ValueError:
        print("Value Error is received")
    except:
        print("Unknown error is received")

    print("\n\nTEST#3")

    try:
        sublist = ["foo", "bar", "man", "bal"]
        sis = subsinstring("barfoothefoobarmanbarfoo", sublist)
        matchlist = sis.find_subcombs()
        print("sublist is {}".format(matchlist))
    except ValueError:
        print("Value Error is received")
    except:
        print("Unknown error is received")

    print("\n\nTEST#4")

    try:
        sublist = ["foo", "bar", "man", "bal", "tal", "sol"]
        sis = subsinstring("barfoothefoobarmanbarfoobaltalbarsolman", sublist)
        matchlist = sis.find_subcombs()
        print("sublist is {}".format(matchlist))
    except ValueError:
        print("Value Error is received")
    except:
        print("Unknown error is received")



