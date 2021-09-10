# This script approximates the Pi value by accumulating the distance among
# point increments on the upper right quartile of the circle
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
import math

class pi():
    def __init__(self, decrement):
        self.inc = decrement
        self.incsqr = self.inc * self.inc
        self.pi = 0

    def calculate_pi(self):

        prev_y = 0.0
        arc = 0.0
        x = 1.0
        while x >= 0.0:
            x -= decrement
            y = math.sqrt(1-x*x)
            ydif = y - prev_y
            dist = math.sqrt(ydif*ydif + self.incsqr)
            prev_y = y
            arc += dist

        # add the last arc as x == 0.0 case may not be satisfied
        ydif = 1 - prev_y
        dist = math.sqrt(ydif*ydif + self.incsqr)
        arc += dist

        self.pi = 2 * arc

        return self.pi

if __name__=="__main__":

    tno = 0

    tno += 1
    decrement = 10**-3

    pival = pi(decrement)
    print("TEST#{} Pi approximation for {} decrement value is {}".format(tno, decrement, pival.calculate_pi()))

    tno+= 1
    decrement = 10**-5

    pival = pi(decrement)
    print("TEST#{} Pi approximation for {} decrement value is {}".format(tno, decrement, pival.calculate_pi()))

    tno+= 1
    decrement = 10**-7

    pival = pi(decrement)
    print("TEST#{} Pi approximation for {} decrement value is {}".format(tno, decrement, pival.calculate_pi()))

    tno+= 1
    decrement = 10**-8

    pival = pi(decrement)
    print("TEST#{} Pi approximation for {} decrement value is {}".format(tno, decrement, pival.calculate_pi()))



