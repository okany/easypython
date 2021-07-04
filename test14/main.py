# This script removes duplicate entries in a list
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

class uniquelist(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.set = set()
        self.rlist = []

    def dedup(self):
        self.rlist = []
        for i in range(len(self)):
            item = self[i]
            if item not in self.set:
                self.set.add(item)
                self.rlist.append(item)
        return (self.rlist)

    def dedup2(self):
        self.rlist = self
        i = len(self.rlist) - 1
        while i > 0:
            item = self.rlist[i]
            if(item not in self.set):
                self.set.add(item)
            else:
                self.rlist.pop(i)
            i = i - 1
        return(self.rlist)

if __name__ == "__main__":
    str1 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."
    alist1 = str1.split()

    ul1 = uniquelist(alist1)
    print(ul1.dedup())

    str2 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."
    alist2 = str2.split()

    ul2 = uniquelist(alist2)
    print(ul2.dedup2())

