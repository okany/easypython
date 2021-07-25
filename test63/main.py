# This script finds all unique paths in a grid of MxN size between points (1,1) and (M,N)
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
#
class grid():
    def __init__(self, grid, m, n):
        self.grid = grid
        self.m = m
        self.n = n
        if(self.verify_grid() == False):
            raise ValueError
        self.paths = list()

    def verify_grid(self):
        valid = False
        if self.grid[0][0] == 1:
            return valid
        if(len(self.grid) == self.n):
            for row in self.grid:
                if len(row) != self.m:
                    return valid
            valid = True
        return valid

    def set_paths(self, grid, x, y, path):
        # don't modify the original grid
        mygrid = self.clone_grid(grid)
        mygrid[x][y] = 1
        path.append([x,y])
        # print("x = {} y = {} path = {}".format(x, y, path))
        if(x == self.n-1 and y == self.m-1):
            self.paths.append(list(path))
        else:
            if (x+1 < self.n and mygrid[x+1][y] == 0):
                # move right
                self.set_paths(mygrid, x+1, y, path.copy())

            if (y+1 < self.m and mygrid[x][y+1] == 0):
                # move down
                self.set_paths(mygrid, x, y+1, path.copy())

    def clone_grid(self, orig):
        grid = list()
        for row in orig:
            crow = row.copy()
            grid.append(crow)
        return grid

    def find_paths(self):
        path = list()
        if (self.grid[0][0] == 0):
            self.set_paths(self.grid, 0, 0, path)
        return self.paths

if __name__=="__main__":

    try:
        agrid = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        m = 4
        n = 6
        grd = grid(agrid, m, n)
        paths = grd.find_paths()
        print("TEST #1 - paths between (0,0) and ({},{}) in grid = {} are:".format(m, n, agrid))

        for path in paths:
            print("   {}".format(path))
    except ValueError:
        print("TEST #1 ValueError received")

    try:
        agrid = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        m = 4
        n = 6
        grd = grid(agrid, m, n)
        paths = grd.find_paths()
        print("TEST #2 paths between (0,0) and ({},{}) in grid = {} are:".format(m, n, agrid))

        for path in paths:
            print("   {}".format(path))
    except ValueError:
        print("TEST #2 ValueError received")

    try:
        agrid = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]
        m = 4
        n = 6
        grd = grid(agrid, m, n)
        paths = grd.find_paths()
        print("TEST #3 paths between (0,0) and ({},{}) in grid = {} are:".format(m, n, agrid))

        for path in paths:
            print("   {}".format(path))
    except ValueError:
        print("TEST #3 ValueError received")

    try:
        agrid = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 0]]
        m = 4
        n = 6
        grd = grid(agrid, m, n)
        paths = grd.find_paths()
        print("TEST #4 paths between (0,0) and ({},{}) in grid = {} are:".format(m, n, agrid))

        for path in paths:
            print("   {}".format(path))
    except ValueError:
        print("TEST #4 ValueError received")

    try:
        agrid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        m = 4
        n = 6
        grd = grid(agrid, m, n)
        paths = grd.find_paths()
        print("TEST #5 paths between (0,0) and ({},{}) in grid = {} are:".format(m, n, agrid))

        for path in paths:
            print("   {}".format(path))
    except ValueError:
        print("TEST #5 ValueError received")

    try:
        agrid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        m = 4
        n = 6
        grd = grid(agrid, m, n)
        paths = grd.find_paths()
        print("TEST #6 paths between (0,0) and ({},{}) in grid = {} are:".format(m, n, agrid))

        for path in paths:
            print("   {}".format(path))
    except ValueError:
        print("TEST #6 ValueError received")
