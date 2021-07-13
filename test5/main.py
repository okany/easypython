# This script implements a search typehead
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
class search_typehead():
    def __init__(self, alist):
        self.adict = dict()
        thn = None
        for word in alist:
            print("word = {}".format(word))
            thn = self.adict.get(word[0])
            if not thn:
                thn = thnode(word[0])
                self.adict[word[0]] = thn

            thn.add_word(word, 1)

    def find_typehead(self, wpart):

        thn = self.adict.get(wpart[0])
        if not thn:
            return []
        else:
            return thn.find_typehead(wpart, 1)

    def print(self):
        for each in self.adict.values():
            print("search_typehead = {}".format(each))
            each.print()

class thnode():
    def __init__(self, achar):
        self.char = achar
        self.next = dict()
        self.word = None

    def add_word(self, word, index):
        if index == len(word) - 1:
            self.word = word
        else:
            thn = self.next.get(word[index])
            if not thn:
                thn = thnode(word[index])
                self.next[word[index]] = thn

            thn.add_word(word, index+1)

    def find_typehead(self, wpart, index):
        thlist = []

        if index == len(wpart):
            if(self.word):
                thlist.append(self.word)

            for item in self.next.values():
                alist = item.find_typehead(wpart, index)
                thlist.extend(alist)
        else:
            alist = []
            thn = self.next.get(wpart[index])
            if thn:
                alist = thn.find_typehead(wpart, index + 1)

            thlist.extend(alist)

        return thlist

    def print(self):
        print("char = {} word = {}".format(self.char, self.word))
        print("dictionary:")
        for each in self.next.values():
            each.print()

if __name__=="__main__":
    alist = ["michael", "michael phelp", "mich", "john", "john wayne",
             "johny", "mark", "markus", "michael phone", "mindy", "joan", "joan ark"]

    sth = search_typehead(alist)

    sth.print()

    wpart = "mic"
    print("typehead list for {} is {} ".format(wpart, sth.find_typehead(wpart)))

    wpart = "jo"
    print("typehead list for {} is {} ".format(wpart, sth.find_typehead(wpart)))

    wpart = "min"
    print("typehead list for {} is {} ".format(wpart, sth.find_typehead(wpart)))

    wpart = "po"
    print("typehead list for {} is {} ".format(wpart, sth.find_typehead(wpart)))
