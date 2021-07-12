# This script finds stepping numbers between two integers e.g. A=10, B=40 output = [10, 12, 21, 23, 32, 34]
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
class stepping_numbers():
    def __init__(self):
        # use ascending and descending stepping numbers to generate the candidate
        self.ascending = "123456789"
        self.descending = "9876543210"
        # keep results in stplist
        self.stplist = list()

    def genlist(self, nlen):
        numlist = list() # create numbers in length nlen
        for i in range(len(self.ascending)-nlen+1):
            astr = self.ascending[i:i+nlen]
            anum = int(astr)

            # exclude numbers not in aint<N<bint range
            if(self.aint<=anum and self.bint>=bnum):
                numlist.append(anum)

        for i in range(len(self.descending)-nlen+1):
            astr = self.descending[i:i+nlen]
            anum = int(astr)

            # exclude numbers not in aint<N<bint range
            if(self.aint<=anum and self.bint>=anum):
                numlist.append(anum)

        return numlist

    def find_nos(self, aint, bint):
        self.aint = aint
        self.bint = bint

        astr = str(aint)
        bstr = str(bint)
        self.stplist = []

        for nlen in range(len(astr), len(bstr)+1):

            alist = self.genlist(nlen)
            self.stplist.extend(alist)

        return self.stplist


if __name__ == "__main__":

    anum = 54
    bnum = 3596478

    sn = stepping_numbers()

    print("stepping numbers list {}".format(sn.find_nos(anum, bnum)))