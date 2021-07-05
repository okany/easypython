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

import sys

class subsinstring():
    def __init__(self, astr, sublist):
        self.str = astr
        self.sublist = sublist
        self.subset = set()
        self.subdict = dict()

        if(len(sublist) == 0):
            raise ValueError
        self.sublen = len(sublist[0])
        for each in sublist:
            if(len(each) != self.sublen) or each in self.subset:
                raise ValueError
            else:
                self.subset.add(each)

            part = str(self.str)
            offset = ind = 0
            while ind >=0 and part and part != "":
                ind = part.find(each)
                if(ind >= 0):
                    offset = offset+ind
                    # print("found {} in {} at position {}".format(each, self.str, offset))
                    self.subdict[offset] = each
                    offset = offset+1
                    part = str(part[ind+1:])
        # print("subset = {}".format(self.subset))

    def find_subcombs(self):

        # keep the solutions in matchlist object in [stating index, substring order] format
        matchlist = []
        # check if you can find a substring of combination of all substrings in the string
        for index in range(len(self.str)):
            subindex = index
            used = set()
            while subindex < len(self.str):
                substr = self.subdict.get(subindex)
                if substr and substr not in used:
                    used.add(substr)
                    subindex += self.sublen
                else:
                    # no match, so try next index
                    break
            # length match indicates that all substrs are used
            if len(used) == len(self.sublist):
                #print ("found a string starting at {}".format(index))
                matchlist.append(index)

        return matchlist

if __name__ == "__main__":

    print("TEST #1")
    try:
        sublist = ["foo", "bar", "man"]
        sis = subsinstring("barfoothefoobarmanbarfoo", sublist)
        matchlist = sis.find_subcombs()
        print("searching substrings {} in {}".format(sublist, sis.str))
        print("sublist is {}".format(matchlist))
    except ValueError:
        print ("Value Error is received")
    except:
        print ("Unknown error is received {}".format(sys.exec_info()))

    print("\n\nTEST#2")

    try:
        sublist = ["foo", "bar", "man", "ball"]
        sis = subsinstring("barfoothefoobarmanbarfoo", sublist)
        matchlist = sis.find_subcombs()
        print("searching substrings {} in {}".format(sublist, sis.str))
        print("sublist is {}".format(matchlist))
    except ValueError:
        print("Value Error is received")
    except:
        print ("Unknown error is received {}".format(sys.exec_info()))

    print("\n\nTEST#3")

    try:
        sublist = ["foo", "bar", "man", "bal"]
        sis = subsinstring("barfoothefoobarmanbarfoo", sublist)
        matchlist = sis.find_subcombs()
        print("searching substrings {} in {}".format(sublist, sis.str))
        print("sublist is {}".format(matchlist))
    except ValueError:
        print("Value Error is received")
    except:
        print ("Unknown error is received {}".format(sys.exec_info()))

    print("\n\nTEST#4")

    try:
        sublist = ["foo", "bar", "man", "bal", "tal", "sol"]
        sis = subsinstring("barfoothefoobarmanbarfoobaltalbarsolman", sublist)
        matchlist = sis.find_subcombs()
        print("searching substrings {} in {}".format(sublist, sis.str))
        print("sublist is {}".format(matchlist))
    except ValueError:
        print("Value Error is received")
    except:
        print ("Unknown error is received {}".format(sys.exec_info()))

    print("\n\nTEST#5")

    try:
        sublist = ["foo", "bar", "man", "bal", "tal", "sol", "bar"]
        sis = subsinstring("barfoothefoobarmanbarfoobaltalbarsolman", sublist)
        matchlist = sis.find_subcombs()
        print("searching substrings {} in {}".format(sublist, sis.str))
        print("sublist is {}".format(matchlist))
    except ValueError:
        print("Value Error is received")
    except:
        print ("Unknown error is received {}".format(sys.exec_info()))




