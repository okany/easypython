# This script implements eval function for arithmetic operands *,/,+,-
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
class expression():
    def __init__(self, astr):
        self.astr = astr
        self.left = None
        self.opr = None
        self.right = None
        self.ind = 0
        self.add = "+"
        self.sub = "-"
        self.mul = "*"
        self.div = "/"
        self.oprs = [self.add, self.sub, self.mul, self.div]
        self.digits = "0123456789"

    def get_num(self):
        num = 0
        while self.ind < len(self.astr) and self.astr[self.ind] in self.digits:
            num = 10 * num + int(self.astr[self.ind])
            self.ind += 1
        return num

    def get_opr(self):
        opr = None
        if self.ind < len(self.astr):
            if self.astr[self.ind] not in self.oprs:
                raise ValueError
            opr = self.astr[self.ind]
            self.ind += 1
        return opr

    def calc(self, left, opr, right):
        if opr == self.add:
            return left + right
        elif opr == self.sub:
            return left - right
        elif opr == self.mul:
            return left * right
        else:
            return left / right

    def eval(self):
        while self.ind < len(self.astr):
            if self.left == None:
                self.left = self.get_num()
                # print("left num = {}".format(self.left))
                continue
            elif self.opr == None:
                self.opr = self.get_opr()
                # print("operand = {}".format(self.opr))
                continue
            else:
                # just set the right num
                self.right = self.get_num()
                if self.opr == self.add or self.opr == self.sub:
                    nextopr = self.get_opr()
                    while nextopr == self.mul or nextopr == self.div:
                        nextval = self.get_num()
                        self.right = self.calc(self.right, nextopr, nextval)
                        nextopr = self.get_opr()
                    if nextopr != None:
                        self.ind -= 1
                # print("right num = {}".format(self.right))

            # evaluate the expression to set the left string and continue with the remaining string
            self.left = self.calc(self.left, self.opr, self.right)

            # reset right value and operand to parse the remaining string as the right string
            self.right = None
            self.opr = None
            # print("remaining string = {}, index = {}, left = {}".format(
            #    self.astr[self.ind:], self.ind, self.left))

        return self.left

if __name__=="__main__":

    try:
        astr = "10+27*188-35/7+125"
        ex = expression(astr)
        print("TEST#1 - evaluation result of the expression {} is {}".format(astr, ex.eval()))
    except ValueError:
        print("ValueError received!")

    try:
        astr = "100*20/5+70+30*10-25*4-200*2"
        ex = expression(astr)
        print("TEST#2 - evaluation result of the expression {} is {}".format(astr, ex.eval()))
    except ValueError:
        print("ValueError received!")

    try:
        astr = "10+20/5+70+30*10/2/5*4*20*6"
        ex = expression(astr)
        print("TEST#3 - evaluation result of the expression {} is {}".format(astr, ex.eval()))
    except ValueError:
        print("ValueError received!")
