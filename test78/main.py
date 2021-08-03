# This script solves the word break problem which determines if a string
# consists of substrings all found in a dictionary
#
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
class word_break():
    def __init__(self, astr, alist, debug = False):
        self.astr = astr
        self.alist = alist
        self.debug = debug
        self.wset = set()
        self.load_dict()

    def load_dict(self):
        for word in self.alist:
            self.wset.add(word)
        if(self.debug):
            print("word dictionary = {}".format(self.wset))

    def segment_word(self):
        return self.segment_str(self.astr)

    def segment_str(self, substr):
        if substr == "":
            return ""
        for index in range(1, len(self.astr)):
            teststr = substr[0:index]
            if(teststr in self.wset):
                if debug: print("found dictionary word ({})".format(teststr))
                next = self.segment_str(substr[index:])
                if next != None:
                    if next == "":
                        return(teststr)
                    else:
                        return (teststr + " " + next)

        # we evaluated all possibilities but could not find a position
        return None

if __name__ == "__main__":

    tno = 0

    tno +=1
    test1 = "conflationalgorithmsareusedininformationretrievalsystemsformatchingthemorphologicalvariantsoftermsforefficientindexingandfasterretrievaloperationstheconflationprocesscanbedoneeithermanuallyorautomaticallytheautomaticconflationoperationisalsocalledstemmingfrakescategorizesstemmingmethodsintofourgroups"
    dict1 = ["conflation" ,"algorithms", "are", "used", "in", "information", "retrieval", "systems", "for", "matching", "the", "morphological", "variants", "of", "terms", "efficient",
             "indexing", "and", "faster", "operations", "process", "can", "be", "done", "either", "manually", "or", "automatically", "automatic", "conflation", "operation", "is", "also",
             "called", "stemming", "frakes", "categorizes", "methods", "into", "four", "groups", "index", "integer", "info", "stem", "fast", "manual"]
    debug = True
    wb = word_break(test1, dict1, debug)

    sw = wb.segment_word()

    print("\nTEST#{} segmented words of the test string #1 is: \n{}".format(tno, sw))

    tno +=1
    test1 = "conflationalgorithmsareusedininformationretrievalsystemsformatchingthemorphologicalvariantsoftermsforefficientindexingandfasterretrievaloperationstheconflationprocesscanbedoneeithermanuallyorautomaticallytheautomaticconflationoperationisalsocalledstemmingfrakescategorizesstemmingmethodsintofourgroups"
    # we use the same dictionary except for "groups" is replaced with "group" - partitioning should fail. Using a stemmer
    # would eliminate this problem. See my application generator for stemming algorithms at https://github.com/okany/stemgen to solve this issue :-)
    dict1 = ["conflation" ,"algorithms", "are", "used", "in", "information", "retrieval", "systems", "for", "matching", "the", "morphological", "variants", "of", "terms", "efficient",
             "indexing", "and", "faster", "operations", "process", "can", "be", "done", "either", "manually", "or", "automatically", "automatic", "conflation", "operation", "is", "also",
             "called", "stemming", "frakes", "categorizes", "methods", "into", "four", "group", "index", "integer", "info", "stem", "fast", "manual"]
    debug = True
    wb = word_break(test1, dict1, debug)

    sw = wb.segment_word()

    print("\nTEST#{} segmented words of the test string #1 is: \n{}".format(tno, sw))
