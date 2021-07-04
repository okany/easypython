# How do you reverse words in a given sentence without using any library method
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

class reverser():
    def __init__(self, str1):
        self.str1 = str1
        self.revstr1 = ""

    def reverse(self):

        rvstr1 = ""
        list1 = self.str1.split()

        for item in list1[::-1]:
            rvstr1 = rvstr1 + item.strip() + " "

        return rvstr1


if __name__=="__main__":
    str1 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."

    rv = reverser(str1)
    print("STRING =", str1)
    print("REVERSE=", rv.reverse())