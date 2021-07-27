# This script finds sliding window maximums of an integer array
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
class sliding_window():
    def __init__(self, alist):
        self.alist = alist
        self.slide = list()
        self.slidelen = 0
        self.maxlist = list()

    def insert(self, index, num):
        sind = 0
        while sind < self.slidelen and sind < len(self.slide):
            # print("index={} num={} sind={} self.slide={} self.slidelen={} self.maxlist={}".
            #       format(index, num, sind, self.slide, self.slidelen, self.maxlist))
            if(self.slide[sind]<=index-num):
                # move up
                self.slide.pop(sind)
                self.slidelen -= 1
            elif(self.alist[self.slide[sind]]<=self.alist[index]):
                # replace with the current one
                self.slide[sind] = index
                self.slidelen = sind + 1
                break
            elif(self.alist[self.slide[sind]]>self.alist[index]):
                # entry at index is smaller than the current, so move to the next
                sind += 1

        if sind == len(self.slide):
            # finished the list, append this to the end
            self.slidelen += 1
            self.slide.append(index)
        elif self.slidelen == sind:
            self.slidelen += 1
            self.slide[sind] = index

    def get_max_list(self, num):
        self.slide = list()
        self.slidelen = 0
        self.maxlist = list()
        for aind in range(len(self.alist)):
            self.insert(aind, num)
            if(aind>=num-1):
                self.maxlist.append(self.alist[self.slide[0]])

        return self.maxlist

if __name__=="__main__":

    alist = [2, 3, 6, 1, 8, 4, 6, 10, 11, 2, 14, 15, 20, 1, 4, 5, 9]
    swsize = 4
    sw = sliding_window(alist)
    tno = 1

    print("TEST#{} for sliding window {} max list of {} is {}".format(tno, swsize, alist, sw.get_max_list(swsize)))

    alist = [1, 2, 3, 4, 5, 6, 20, 13, 14, 21, 15, 25, 26, 27, 30, 12, 15, 17, 26, 25, 2, 3, 4, 1, 1, 1, 1, 1]
    swsize = 5
    sw = sliding_window(alist)
    tno += 1

    print("TEST#{} for sliding window {} max list of {} is {}".format(tno, swsize, alist, sw.get_max_list(swsize)))

    alist = [5, 4, 3]
    swsize = 4
    sw = sliding_window(alist)
    tno += 1

    print("TEST#{} for sliding window {} max list of {} is {}".format(tno, swsize, alist, sw.get_max_list(swsize)))

    alist = [5, 4, 3, 6, 2, 1, 7]
    swsize = 1
    sw = sliding_window(alist)
    tno += 1

    print("TEST#{} for sliding window {} max list of {} is {}".format(tno, swsize, alist, sw.get_max_list(swsize)))

