# This script matches two regular expression strings
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
def isMatch(strA, strB):
    indA = indB = 0

    # print("checking if {} and {}".format(strA, strB))
    while indA < len(strA) and indB < len(strB):
        if (strA[indA] == "*") or (strB[indB] == "*"):
            return(evaluate_star(strA[indA:], strB[indB:]))
        elif(strA[indA] == strB[indB] or strA[indA] == "?" or strB[indB] == "?"):
            indA += 1
            indB += 1
        else:
            return False

    if indA != len(strA):
        # strA has extra characters
        while indA < len(strA):
            if strA[indA] != "*":
                return False
            else:
                indA += 1
    else:
        # strB has extra characters
        while indB < len(strB):
            if strB[indB] != "*":
                return False
            else:
                indB += 1

    if indA == len(strA) and indB == len(strB):
        return True
    else:
        return False

def evaluate_star(strA, strB):
    if(strA[0] == "*"):
        # test all strB substrings including empty string
        for i in range(len(strB)+1):
            if(isMatch(strA[1:], strB[i:])):
                return True
    if(strB[0] == "*"):
        # test all strA substrings including empty string
        for i in range(len(strA)+1):
            if(isMatch(strA[i:], strB[1:])):
                return True
    return False

if __name__=="__main__":

    strA = "abcdef"
    strB = "abcdef"

    print("TEST#1 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "abcdef"
    strB = "abdcef"

    print("TEST#2 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "abcdef"
    strB = "ab??ef"

    print("TEST#3 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "abcdef?"
    strB = "abcdef"

    print("TEST#4 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "abcdef*"
    strB = "abcdef"

    print("TEST#5 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "abcdef****"
    strB = "abcdef**"

    print("TEST#6 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "*"
    strB = "abcdef"

    print("TEST#7 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "**abcdef"
    strB = "abcdef**"

    print("TEST#8 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "*f"
    strB = "a*"

    print("TEST#9 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "?f"
    strB = "a?"

    print("TEST#10 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "*f"
    strB = "*a"

    print("TEST#11 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = "?"
    strB = "a*"

    print("TEST#12 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))

    strA = ""
    strB = "*"

    print("TEST#12 - does strA {} and strB {} match? - {} ".format(strA, strB, isMatch(strA, strB)))
