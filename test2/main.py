# This script solves NQueens puzzle which is the problem of placing n
# queens on an n×n chessboard such that no two queens attack each other
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
class nqueens():
    def __init__(self, num):
        self.num = num
        self.solset_start = 0
        self.reset()
        self.allsols = list()
        self.debug = False

    def reset(self):
        self.board = self.create_board()
        self.removed = [list() for _ in range(self.num)]
        self.sol = list()

    def create_board(self):
        board = list()
        for i in range(self.num):
            row = list()
            for j in range (self.num):
                if i > 0 or j >= self.solset_start:
                    row.append([i, j])
            board.append(row)
        return board

    def full_board(self):
        return True

    def find_solutions(self, debug = False):
        self.debug = debug
        for self.solset_start in range(self.num):
            self.reset()
            i = 0
            j = 0
            while i >= 0 and i < num:
                # selected a raw
                while j < len(self.board[i]):
                    # selected an available point in the board
                    if self.place_queen(self.board[i][j]):
                        self.print_board()
                        break
                    else:
                        self.print_board()
                        self.remove_sol()
                        self.print_board()
                        j = 0

                if i+1 == len(self.sol):
                    i += 1
                elif self.board[i] == []:
                    self.remove_sol()
                    self.print_board()
                    i -= 1
            if len(self.sol) == self.num:
                self.allsols.append(self.sol)
                if debug:
                    print("All solutions = {} i={} j={}".format(self.allsols, i, j))
            self.print_board()

    def print_all_solutions(self):
        print("All solutions for {0}x{0} board are:".format(self.num))

        if(self.allsols == []):
            print("None")
        else:
            for i, sol in enumerate(self.allsols):
                print("Solution #{} :".format(i+1))
                print(sol)
                self.print_solution(sol)

    def print_solution(self, sol):
        for _ in range((self.num*3)+4):
            print(end='-')
        print ("")
        for i, asol in enumerate(sol):
            print("{:2}".format("|"), end=' ')
            for j in range(asol[1]):
                print("{:2}".format("."), end=' ')
            print("{:2}".format("X"), end=' ')
            for j in range(asol[1]+1, self.num):
                print("{:2}".format("."), end=' ')
            print("{:2}".format("|"), end=' ')
            print("")
        for _ in range((self.num*3)+4):
            print(end='-')
        print ("")

    def print_board(self):
        if self.debug:
            print("-----------------------")
            for i, board in enumerate(self.board):
                print(" row {}     = {}".format(i, board))
            for i, removed in enumerate(self.removed):
                print(" removed {} = {}".format(i, removed))
            print(" solution is {}".format(self.sol))
            print("-----------------------")

    def clone_board(self, board):
        clone  = list()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                clone.append(cell.copy())

        return clone

    def add_sol(self, pos):
        if self.debug:
            print("adding solution {}".format(pos))
        for each in self.board[pos[0]]:
            if each != pos:
                self.removed[pos[0]].append(each)
        # remove the row as queen is placed to this raw
        self.board[pos[0]] = list()
        self.sol.append(pos)

    def remove_sol(self):
        if self.sol == []:
            return None
        pos = self.sol.pop()
        if self.debug:
            print("removing solution {}".format(pos))
        if(pos[0]>0):
            self.removed[pos[0]-1].append(pos)
        for each in self.removed[pos[0]]:
            self.board[each[0]].append(each)
        self.removed[pos[0]] = list()
        return pos[0]

    def place_queen(self, pos):
        self.add_sol(pos)
        for raw in self.board[pos[0]+1:]:
            i = 0
            while i < len(raw):
                if(raw[i][1] == pos[1] or abs(raw[i][0]-pos[0])==abs(raw[i][1]-pos[1])):
                    self.removed[pos[0]].append(raw[i])
                    raw.pop(i)
                else:
                    i += 1
            if raw == []:
                return False
        return True

if __name__=="__main__":

    tno = 0

    debug = False
    tno += 1
    num = 2
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 3
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 4
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 5
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 6
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 7
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 8
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 16
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

    debug = False
    tno += 1
    num = 24
    print("TEST#{}".format(tno))
    nq = nqueens(num)
    nq.find_solutions(debug)
    nq.print_all_solutions()

