# This finds the shortest sequence between two words start and end by changing
# single character each time and requiring all intermediary words in a word dictionary
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
class gNode():
    def __init__(self, value):
        self.value = value # value string
        self.nset = set() # neighbor list

    def print(self):
        print(" {} : {}".format(self.value, self.nset))

class clusters():
    def __init__(self, wdist, debug = False):
        self.wdist = wdist
        self.graph = dict()
        self.debug = debug
        self.sollist = list()
        self.sollen  = 0
        self.create_clusters()

    def isNeighbor(self, word1, word2):
        diff = 0
        retval = True
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
                if diff > 1:
                    retval = False
                    break
        return retval

    def create_gnode(self, word):
        if self.debug:
            print("adding new dictionary word {}".format(word))
        if not self.graph.get(word):
            gnode = gNode(word)
            for each in self.graph:
                if(self.isNeighbor(word, each)):
                    self.graph[each].nset.add(word)
                    gnode.nset.add(each)
            self.graph[word] = gnode

    def create_clusters(self):
        for word in self.wdist:
            if self.debug:
                print("processing word {}".format(word))
            if(self.graph.get(word) == None):
                self.create_gnode(word)

    def find_shortest(self, clist, cset, gword1, gword2):

        sollen = 0
        minsollist = list()
        # check the loops
        if gword1.value in cset:
            return None

        clist.append(gword1.value)
        cset.add(gword1.value)

        if gword2.value in gword1.nset:
            clist.append(gword2.value)
            cset.add(gword2.value)

            if self.minsollist == [] or self.sollen > len(clist):
                self.minsollist = [clist]
                self.sollen = len(clist)
            elif self.sollen == len(clist):
                self.minsollist.append(clist)

            if self.debug:
                print("possible solution {} - Minlength solution {}".format(clist, self.minsollist))

        else:
            for word in gword1.nset:
                if word != clist[-1]: # skip the previous word
                    newgword = self.graph.get(word)
                    self.find_shortest(clist.copy(), cset.copy(), newgword, gword2)

    def find_word_ladder(self, word1, word2):

        self.minsollist = list()
        self.sollen = 0

        # add word1 to the cluster
        if (self.graph.get(word1) == None):
            self.create_gnode(word1)

        # add word2 to the cluster
        if (self.graph.get(word2) == None):
            self.create_gnode(word2)

        gword1 = self.graph.get(word1)
        gword2 = self.graph.get(word2)

        currentlist = list()
        currentset = set()

        self.find_shortest(currentlist, currentset, gword1, gword2)
        return self.minsollist


    def print(self):
        print("Word : Neighbor List")
        print("---- : -------------")
        for word in self.graph:
            self.graph[word].print()

if __name__=="__main__":

    tno = 0

    tno += 1
    debug = False

    wdict = []
    start = 'dop'
    end = 'fas'

    cl = clusters(wdict, debug)
    if debug:
        cl.print()

    sol = cl.find_word_ladder(start, end)
    print("--------------------------------------------------------------------")
    print("TEST#{} Word Dictionary : {}".format(tno, wdict))
    print("TEST#{} Starting Word   : '{}' ".format(tno, start))
    print("TEST#{} Ending Word     : '{}' ".format(tno, end))
    print("TEST#{} Solution list   : {} ".format(tno, sol))
    print("--------------------------------------------------------------------")

    wdict = []
    start = 'dop'
    end = 'top'

    cl = clusters(wdict, debug)
    if debug:
        cl.print()

    sol = cl.find_word_ladder(start, end)
    print("TEST#{} Word Dictionary : {}".format(tno, wdict))
    print("TEST#{} Starting Word   : '{}' ".format(tno, start))
    print("TEST#{} Ending Word     : '{}' ".format(tno, end))
    print("TEST#{} Solution list   : {} ".format(tno, sol))
    print("--------------------------------------------------------------------")

    tno += 1
    debug = False

    wdict = ['top', 'pop', 'sop', 'tor', 'for', 'tip', 'rap', 'ras', 'das', 'wok', 'lor', 'are', 'ate', 'tap', 'far']
    start = 'dop'
    end = 'fas'

    cl = clusters(wdict, debug)
    if debug:
        cl.print()

    sol = cl.find_word_ladder(start, end)
    print("TEST#{} Word Dictionary : {}".format(tno, wdict))
    print("TEST#{} Starting Word   : '{}' ".format(tno, start))
    print("TEST#{} Ending Word     : '{}' ".format(tno, end))
    print("TEST#{} Solution list   : {} ".format(tno, sol))
    print("--------------------------------------------------------------------")


    tno += 1
    debug = False

    wdict = ['top', 'pop', 'sop', 'tor', 'for', 'tip', 'rap', 'ras', 'das', 'wok', 'lor', 'are', 'ate', 'tap', 'far']
    start = 'dop'
    end = 'pod'

    cl = clusters(wdict, debug)
    if debug:
        cl.print()

    sol = cl.find_word_ladder(start, end)
    print("TEST#{} Word Dictionary : {}".format(tno, wdict))
    print("TEST#{} Starting Word   : '{}' ".format(tno, start))
    print("TEST#{} Ending Word     : '{}' ".format(tno, end))
    print("TEST#{} Solution list   : {} ".format(tno, sol))
    print("--------------------------------------------------------------------")

    tno += 1
    debug = False

    wdict = ['top', 'pop', 'sop', 'tor', 'for', 'tip', 'rap', 'ras', 'das', 'wok', 'lor', 'are', 'ate', 'tap', 'far']
    start = 'dop'
    end = 'sar'

    cl = clusters(wdict, debug)
    if debug:
        cl.print()

    sol = cl.find_word_ladder(start, end)
    print("TEST#{} Word Dictionary : {}".format(tno, wdict))
    print("TEST#{} Starting Word   : '{}' ".format(tno, start))
    print("TEST#{} Ending Word     : '{}' ".format(tno, end))
    print("TEST#{} Solution list   : {} ".format(tno, sol))
    print("--------------------------------------------------------------------")

    tno += 1
    debug = False

    wdict = ['top', 'pop', 'sop', 'tor', 'for', 'tip', 'rap', 'ras', 'das', 'wok', 'lor', 'are', 'ate', 'tap', 'far']
    start = 'sas'
    end = 'ats'

    cl = clusters(wdict, debug)
    if debug:
        cl.print()

    sol = cl.find_word_ladder(start, end)
    print("TEST#{} Word Dictionary : {}".format(tno, wdict))
    print("TEST#{} Starting Word   : '{}' ".format(tno, start))
    print("TEST#{} Ending Word     : '{}' ".format(tno, end))
    print("TEST#{} Solution list   : {} ".format(tno, sol))
    print("--------------------------------------------------------------------")

