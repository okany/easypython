# This script finds the minimum number of cuts to create palindromes from a string
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
class palindromes():
    def __init__(self, astr):
        self.pstr = astr
        self.pal_list = list()
        self.cur_pals = list()
        self.cut_list = list()
        self.debug = False

    def insert_pal_list(self, rng):
        i = 0
        while i < len(self.pal_list):
            if self.pal_list[i][1]-self.pal_list[i][0] > rng[1] - rng[0]:
                i += 1
            else:
                break
        self.pal_list.insert(i, rng)

    def extend_pal_list(self, rnglist):
        for rng in rnglist:
            self.insert_pal_list(rng)

    def find_palindromes(self):
        for i in range(len(self.pstr)):
            cur_pals = list()
            if self.debug:
                print("self.cur_pals = {}".format(self.cur_pals))
            for palind in range(len(self.cur_pals)):
                if ((self.cur_pals[palind][0]>0 and self.cur_pals[palind][1]+1<len(self.pstr)) and
                    (self.pstr[self.cur_pals[palind][0]-1] == self.pstr[self.cur_pals[palind][1]+1])):
                    cur_pals.append([self.cur_pals[palind][0]-1, self.cur_pals[palind][1]+1])
            self.cur_pals = cur_pals
            if i > 0 and self.pstr[i] == self.pstr[i-1]:
                self.cur_pals.append([i-1, i])
            if i > 1 and self.pstr[i] == self.pstr[i-2]:
                self.cur_pals.append([i-2, i])
            if (self.cur_pals != []):
                self.extend_pal_list(self.cur_pals)
        if self.debug:
            print("self.cur_pals={} self.pal_list={}".format(self.cur_pals, self.pal_list))

        return self.pal_list

    def find_min_cuts(self, debug = False):
        self.debug = debug
        self.find_palindromes()
        palind = 0
        min_cuts = len(self.pstr) - 1
        while palind < len(self.pal_list):
            pal = self.pal_list[palind]
            min_cuts -= (pal[1] - pal[0])
            nextind = palind + 1
            while nextind < len(self.pal_list):
                # check if they intersects
                if ((self.pal_list[nextind][0] >= pal[0] and self.pal_list[nextind][0] <= pal[1]) or
                    (self.pal_list[nextind][1] >= pal[0] and self.pal_list[nextind][1] <= pal[1])):
                    # remove this palindrome from the list
                    self.pal_list.pop(nextind)
                else:
                    nextind += 1
            palind += 1
        if (self.debug):
            print("Unique pal list is {}".format(self.pal_list))
        return min_cuts

if __name__=="__main__":

    tno = 0
    tno += 1
    debug = False
    astr = "ababbacbabcbbababccbabababc"
    # 0 1 2345 67890 1 234567890123 4 5 6
    # a b abba cbabc b bababccbabab a b c
    pal = palindromes(astr)

    print("TEST#{} - minimim number of cuts for {} is {}".format(tno, astr, pal.find_min_cuts(debug)))

    tno += 1
    debug = False
    astr = "aaaabbbaaaaa"
    pal = palindromes(astr)

    print("TEST#{} - minimim number of cuts for {} is {}".format(tno, astr, pal.find_min_cuts(debug)))

    tno += 1
    debug = False
    astr = "acabacabababacabaca"
    pal = palindromes(astr)

    print("TEST#{} - minimim number of cuts for {} is {}".format(tno, astr, pal.find_min_cuts(debug)))
