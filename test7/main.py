# This script finds the largest rectangle in a histogram
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
class histogram(list):
    def __init__(self, alist):
        # pad the list with 0s to set boundaries for the calculation
        # the 0s act like histogram data with 0 value on each side of the histogram
        # this simplifies the program while does not affect the result
        alist.insert(0,0)
        alist.append(0)
        super().__init__(alist)
        self.sorted = []
        self.used = []
        self.max_rect_area = 0
        print("alist= {}".format(alist))

    def insert_sorted(self, i):
        index = 0
        while index < len(self.sorted):
            # print("insert_sorted index={} self.sorted={} len(self.sorted)={} i={}".format(index, self.sorted,                                                                     len(self.sorted), i))
            if self[self.sorted[index]] > self[i]:
                break
            index += 1

        self.sorted.insert(index, i)

    def create_sorted(self):
        self.sorted.append(0)

        for i in range(1, len(self)):
            self.insert_sorted(i)
        print("self.sorted = {}".format(self.sorted))

    def insert_used(self, i):
        index = 0
        while index < len(self.used):
            if self.used[index] > i:
                break
            index += 1
        self.used.insert(index, i)

        return index

    def initialize_used(self):
        # initialize the used list with imaginary histogram blocks
        self.used = []

    def get_used_value(self, index):
        return(self[self.used[index]])

    def calculate_rectangle_area(self, used_index):
        print("self.used = {} used_index = {} self[used_index] = {}".format(self.used, used_index, self[used_index]))

        # return 0 for the boundary values
        if(used_index == 0 or used_index == len(self.used) -1 ): return 0

        prev = used_index - 1
        while prev > 0 and self.get_used_value(prev) == self.get_used_value(used_index):
            prev -= 1

        print("prev = {}".format(prev))

        next = used_index + 1
        while next < len(self.used)-1 and self.get_used_value(next) == self.get_used_value(used_index):
            next += 1

        print("next = {}".format(next))

        rect_area = self[self.used[used_index]] * (self.used[next] - self.used[prev] - 1 )

        return rect_area

    def largest_rect(self):
        # sort all histogram values in increasing order
        # first rectangle will be bounded by the shortest historam value
        self.create_sorted()
        # initialize used with two imaginary histogram values 0 and histogram+1 values
        self.initialize_used()

        while self.sorted != []:
            # calculate the area of the first rectangle
            hist_val = self.sorted.pop(0)
            # insert the popped histogram value into the used histogram list
            used_index = self.insert_used(hist_val)
            rect_area = self.calculate_rectangle_area(used_index)
            print("rect_area = {}".format(rect_area))

            if(rect_area > self.max_rect_area):
                # update the max rectangle area if the area is greater
                self.max_rect_area = rect_area

        return self.max_rect_area

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    alist = [12, 15, 17, 25, 40, 55, 30, 24, 60, 80, 90]

    hist = histogram(alist)

    print("LARGEST RECTANGLE FOR {} is {}".format(alist, hist.largest_rect()))

    alist = [12, 15, 17, 25, 25, 14, 12, 40, 55, 30, 24, 18, 18, 20, 60, 80, 90]

    hist = histogram(alist)

    print("LARGEST RECTANGLE FOR {} is {}".format(alist, hist.largest_rect()))