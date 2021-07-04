# This script demonstrates trying and catching exceptions while getting an a positive integer as an input
# and printing its square
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

class square(int):
    def __init__(self, num):
        self = num

    def getnum(self):
        return self

    def getsqr(self):
        return (self * self)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:
        numstr = input("Enter a number: ")
        num = int(numstr)
        if num < 0: raise ValueError
    except NameError:
        print("Name Error")
    except ValueError:
        print("Value Error")
    except IOError:
        print("I/O Error")
    except:
        print("not a valid entry")
    else:
        numobj = square(num)
        print("Square of {0} is {1}".format(numobj.getnum(), numobj.getsqr()))
