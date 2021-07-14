# This script implements power function with modulo operator
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

class power():
    def __init__(self, x, n, d):
        self.x = x
        self.n = n
        self.d = d
        self.pow_div = -1
        self.dict = dict()
        self.list = []
        result = None
        div = 1
        for num in range(1, self.n):
            div = (div * self.x) % self.d
            apow = self.dict.get(div)
            # print("get apow={} div={} to dict".format(apow, div))
            if(apow != None):
                # print("repeating num={} div={} to dict".format(num, div))
                # found a repeat - repeats after every dif powers
                dif = num - apow
                # power(x, n) % d = power(x, ind) % d
                ind = (self.n % dif) - 1
                if ind < 0: # the last value in the list is repeating
                    ind = dif - 1
                # print("ind = {}".format(ind))
                self.pow_div = self.list[ind]
                break
            else:
                # print("adding num={} div={} to dict".format(num, div))
                self.list.append(div)
                self.dict[div] = num

    def get_power_div(self):
        return self.pow_div

if __name__ == "__main__":

    x = 45
    n = 156
    d = 7
    pow = power(x, n, d)
    res = pow.get_power_div()
    print("TEST#1 - power({}, {}) % {} is {}".format(x, n, d, res))

    x = 10
    n = 200
    d = 10
    pow = power(x, n, d)
    res = pow.get_power_div()
    print("TEST#2 - power({}, {}) % {} is {}".format(x, n, d, res))

    x = 27
    n = 9
    d = 11
    pow = power(x, n, d)
    res = pow.get_power_div()
    print("TEST#3 - power({}, {}) % {} is {}".format(x, n, d, res))

