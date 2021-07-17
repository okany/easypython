# This script evaluates an expression in reverse polish notation
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

def evaluate(alist):
    exp = expression(alist)
    return(exp.eval())

class expression(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.orig = self
        self.opers = ["+", "-", "/", "*"]

    def operate(self, oper, num1, num2):
        if oper == "+":
            return num1 + num2
        elif oper == "-":
            return num1 - num2
        elif oper == "*":
            return num1 * num2
        elif oper == "/":
            return num1 / num2
        else:
            print("parse error")
            return None

    def eval(self):
        if self == "":
            return self.result
        elif self[-1] in self.opers:
            oper = self[-1]
            self.pop(-1)
            num1 = self.eval()
            num2 = self.eval()
            return self.operate(oper, num1, num2)
        else:
            num = int(self[-1])
            self.pop(-1)
            return num

if __name__ == "__main__":

    alist = ["2", "3", "*", "10", "+"]
    res = evaluate(alist)

    print("TEST#1 - evaluation result of list of {} is {}".format(alist, res))

    alist = ["1", "5", "15", "/", "-"]
    res = evaluate(alist)

    print("TEST#2 - evaluation result of list of {} is {}".format(alist, res))

    alist = ["1", "5", "15", "/", "-", "6", "4", "2", "+", "*", "+"]
    res = evaluate(alist)

    print("TEST#3 - evaluation result of list of {} is {}".format(alist, res))
