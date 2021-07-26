# This script finds all possible letter combinations of for digits
# dialed on a letter phone
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
class letter_phone():
    def __init__(self,digits):
        self.digits = digits
        self.letters = [["0"],["1"],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],
                        ["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

    def get_combs(self):
        if self.digits == "":
            return []
        index = 1
        mycombs = self.letters[int(self.digits[0])].copy()
        while index < len(self.digits):
            # print("digits={} mycombs={}".format(self.digits, mycombs))
            newcombs = list()
            for comb in mycombs:
                for letter in self.letters[int(self.digits[index])]:
                    newcombs.append(comb+letter)
            mycombs = newcombs
            index += 1

        return mycombs

if __name__=="__main__":

    testind = 1
    digits = "24"
    lp = letter_phone(digits)

    print("TEST#{} - letter combinations for doaled digits {} is {}".format(testind, digits, lp.get_combs()))

    testind += 1
    digits = "124553532"
    lp = letter_phone(digits)

    print("TEST#{} - letter combinations for doaled digits {} is {}".format(testind, digits, lp.get_combs()))

    testind += 1
    digits = ""
    lp = letter_phone(digits)

    print("TEST#{} - letter combinations for doaled digits {} is {}".format(testind, digits, lp.get_combs()))

    testind += 1
    digits = "0"
    lp = letter_phone(digits)

    print("TEST#{} - letter combinations for doaled digits {} is {}".format(testind, digits, lp.get_combs()))

    testind += 1
    digits = "01100011"
    lp = letter_phone(digits)

    print("TEST#{} - letter combinations for doaled digits {} is {}".format(testind, digits, lp.get_combs()))

    testind += 1
    digits = "6526"
    lp = letter_phone(digits)

    print("TEST#{} - letter combinations for doaled digits {} is {}".format(testind, digits, lp.get_combs()))
