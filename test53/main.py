# This script generates all combinations of n pairs of well-formed parentheses
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

class parens():
    def __init__(self, num):
        self.pairs = num
        self.soln = []
        self.open = "("
        self.close = ")"
        self.sset = set()

    def create_indlist(self, presoln):
        numlist = [0]
        pnum = 1
        for ind in range(1,len(presoln)):
            if(presoln[ind] == self.open):
                pnum += 1
            elif(presoln[ind] == self.close):
                pnum -= 1
            else:
                print("software error")

            if(pnum == 0):
                numlist.append(ind+1)
        # print ("numlist for {} is {}".format(presoln, numlist))
        return numlist

    def addparen(self, pstr):
        newsoln = []
        indlist = self.create_indlist(pstr)

        for ind in range(len(indlist)):
            for sind in range(ind+1):
                # print("pstr = {} sind = {} ind = {}".format(pstr, sind, ind))
                asol = pstr[0:indlist[sind]] + self.open + pstr[indlist[sind]:indlist[ind]] \
                       + self.close + pstr[indlist[ind]:len(pstr)+1]
                # print("asol = {}".format(asol))
                if(asol not in self.sset):
                    self.sset.add(asol)
                    newsoln.append(asol)

        return newsoln


    def generate_parens(self):
        soln = []
        if self.pairs == 0:
            return soln
        elif self.pairs == 1:
            return ["()"]
        else:
            prep = parens(self.pairs-1)
            presoln = prep.generate_parens()
            # print("presoln = {}".format(presoln))
            for each in presoln:
                asoln = self.addparen(each)
                soln.extend(asoln)

        return soln

if __name__=="__main__":

    for n in range(6):
        p = parens(n)
        soln = p.generate_parens()
        print("TEST#{} well-formed parentheses combination for n={} is {}".format(n+1, n, soln))
