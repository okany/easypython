# This script finds if parentheses are balanced in a string
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

class parentheses(str):
    def __init__(self, astr):
        super().__init__()
        self.open = "("
        self.close = ")"
        self.numofparan = 0
        self = astr

    def isBalanced(self):
        self.numofparan = 0
        retval = False
        for char in self:
            if char == self.open:
                self.numofparan += 1
            elif char == self.close:
                self.numofparan -= 1
            else:
                pass # skip if not a paran

            if self.numofparan < 0:
                break # return False

        if self.numofparan == 0:
            retval = True

        return retval

if __name__=="__main__":

    astr = "(()()((()))()(()))"
    ph = parentheses(astr)
    print("TEST#1 - str {} has its parentheses isBalanced = {}".format(astr, ph.isBalanced()))

    astr = "(()()((())))()(()))"
    ph = parentheses(astr)
    print("TEST#2 - str {} has its parentheses isBalanced = {}".format(astr, ph.isBalanced()))

    astr = "())(()()((()))()(()))"
    ph = parentheses(astr)
    print("TEST#3 - str {} has its parentheses isBalanced = {}".format(astr, ph.isBalanced()))

    astr = "()(()()((()))()(()))"
    ph = parentheses(astr)
    print("TEST#4 - str {} has its parentheses isBalanced = {}".format(astr, ph.isBalanced()))

    astr = "()(()()((()))()(()))("
    ph = parentheses(astr)
    print("TEST#5 - str {} has its parentheses isBalanced = {}".format(astr, ph.isBalanced()))

