# This script finds Fibonacci numbers for a given positive integer
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

class fibo():
    def __init__(self):
        self.dict = dict()
        self.dict[0] = None
        self.dict[1] = 1
        self.dict[2] = 2

    def find_fibo(self, num):
        res = None
        if num in self.dict:
            res = self.dict[num]
        else:
            fn_1 = self.find_fibo(num - 1)
            fn_2 = self.find_fibo(num - 2)

            res = fn_1 + fn_2
            self.dict[num] = res
        return res


if __name__ == "__main__":

    fb = fibo()

    n = 0
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 1
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 2
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 15
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 16
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 17
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 1000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 1500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 2000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 2500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 3000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 3500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 4000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 4500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 5000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 5500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 6000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 6500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 7000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 7500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 8000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 8500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 9000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 9500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 10000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 10500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 11000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 11500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 12000
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))
    n = 12500
    print("Fibonacci number for {} is {}".format(n, fb.find_fibo(n)))

    x = n = 0
    for n in range(10000, 10**6+1, 500):
        x = fb.find_fibo(n)
        if(n % 100000 == 0):
            print("Found Fibonacci number for {}".format(n))

    print("Fibonacci number for {} is {} ".format(n, x))

