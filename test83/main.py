# This script distributes minimum number of candies to N children each
# with a priority such that every child gets at least one candy and each
# kid gets more candies than a kid with a lower priority
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright [c] 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# [at your option] any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
class distribute_candy():
    def __init__(self, priorities):
        self.plist = priorities
        self.pdict = dict()
        self.min_candies = 0
        self.slist = list()

    def get_min_candies(self):
        self.slist = [each for each in self.plist if each not in self.pdict]

        for each in self.plist:
            self.pdict[each] = self.pdict[each] + 1 if each in self.pdict else 1

        # sort unique priority list
        self.slist.sort()
        self.min_candies = 0

        for index, item in enumerate(self.slist):
            # give one more cnady to the next group
            self.min_candies += (index+1) * self.pdict[item]

        # return the minimum number of candies
        return(self.min_candies)

if __name__ == "__main__":

    tno = 0

    tno += 1
    priorities = [1, 1, 5, 2, 3, 4, 4]

    dc = distribute_candy(priorities)

    print("TEST#{} minimum number of candies needed for priority list {} is {}".format(tno, priorities, dc.get_min_candies()))

    tno += 1
    priorities = [1, 1, 5, 2, 3, 4, 4, 2, 2, 3, 7, 10, 15, 17, 15, 17]

    dc = distribute_candy(priorities)

    print("TEST#{} minimum number of candies needed for priority list {} is {}".format(tno, priorities, dc.get_min_candies()))




