# This script finds the minimum number of steps to convert string A into
# string B where character insertion, deletion, and modification are
# allowed as valid operations
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright [c] 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# [at your option] any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
class edit_distance():
    def __init__(self, stra, strb):
        self.stra = stra
        self.strb = strb
        self.soltbl = dict()

    def converta2b(self, stra, strb):
        ops = 0
        dicval = self.soltbl.get(stra + "-@-" + strb)
        if dicval != None:
            return dicval

        if stra == "":
            # append chars from strb
            ops = len(strb)
        elif strb == "":
            # delete chars from stra
            ops = len(stra)
        elif stra[0] == strb[0]:
            # have a match, so just skip this char
            ops = self.converta2b(stra[1:], strb[1:])
        else:
            # try removing a char
            remchar = self.converta2b(stra[1:], strb) + 1
            # try adding a char (strb[0])
            addchar = self.converta2b(stra, strb[1:]) + 1
            # try modifying a char (stra[0] -> strb[0])
            modchar = self.converta2b(stra[1:], strb[1:]) + 1

            # return the min of the ops
            ops = (min(min(remchar, addchar), modchar))

        # save this solution not to recalculate
        self.soltbl[stra + "-@-" + strb] = ops

        return ops

    def doconvert(self):
        self.soltbl = dict()
        return(self.converta2b(self.stra, self.strb))

if __name__=="__main__":

    tno = 0

    tno += 1
    strA = "spacex"
    strB = "escapelexx"

    ed = edit_distance(strA, strB)
    ops = ed.doconvert()
    print ("TEST#{} converting strA = {} into strB = {} requires {} number of ops".format(tno, strA, strB, ops))

    tno += 1
    strA = "see if you can match this string with the next"
    strB = "can you match next string with this"

    ed = edit_distance(strA, strB)
    ops = ed.doconvert()
    print("TEST#{} converting strA = {} into strB = {} requires {} number of ops".format(tno, strA, strB, ops))

