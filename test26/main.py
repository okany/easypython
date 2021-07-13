# count the occurrence of each word in a list
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

class listcount(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.adict = dict()
        self.createdict()

    def createdict(self):
        for item in self:
            if (self.adict.get(item) == None):
                self.adict[item] = 1
            else:
                self.adict[item] = self.adict[item]+1

    def printcounts(self):
        print("WORD COUNT = {}".format(self.adict))

if __name__ == '__main__':
    test1 = "Conflation algorithms areused in Information Retrieval (IR) systems for matching the morphological variants of terms for efficient indexing and faster retrieval operations. The conflation process can be done either manually or automatically. The automatic conflation operation is also called stemming. Frakes [1] categorizes stemming methods into four groups: Manuscript received July 9, 2007. Okan Yilmaz, Student Member, IEEE, William Frakes, Member, IEEE A Case Study of Using Domain Analysis for the Conflation Algorithms Domain IN the early 1980s software companies started the systematic reuse process through domain engineering to improve software productivity and quality. There has been insufficient empirical study of the domain engineering process and domain products such as reusable components and generators. This paper addresses this problem by documenting and empirically evaluating a domain engineering project for the conflation algorithms domain. This domain is important for many types of systems such as information retrieval systems, search engines, and word processors. The application generator developed for this study extends the domain scope compared to previous ones. affix removal, successor variety, n-gram and table lookup. Affix removal is the most intuitive and commonly used of these algorithm types. In order to determine the stem, affix removal algorithms remove suffixes and sometimes also prefixes of terms. Successor variety and n-gram methods analyze a word corpus to determine the stems of terms. Successor variety bases its analysis on the frequency of letter sequences in terms, while n-gram conflates terms into groups based on the ratio of common letter sequences, called n-grams. Table lookup based methods use tables which map terms to their stems."
    test2 = "We did a domain analysis for the semantic automatic conflation algorithms domain. We analyzed 3 affix removal stemmers, a successor variety stemmer, an n-gram stemmer, and a table lookup stemmer. Based on this analysis, we created a generic architecture, determined reusable components, and designed and developed a little language and an application generator for this domain. We compared the performance of the automatically generated algorithms with their original versions and found that automatically generated versions of the algorithms are nearly as precise as the original versions."

    list1 = list(test1.split())
    list2 = list(test2.split())

    wc1 = listcount(list1)
    wc1.printcounts()

    wc2 = listcount(list2)
    wc2.printcounts()
