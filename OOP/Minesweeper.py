from __future__ import print_function
from Queue import Queue
from random import randint
import os

class MineSweeper(object):

    def __init__(self, row=10, col=10, mineCount=15):
        self.row = row
        self.col = col
        self.board = [[0] * col for _ in range(row)]
        self.accessable = set()
        self.mines = self.mineGenerator(mineCount)
        self.win = False
        self.lose = False

    def mineGenerator(self, num):
        mines = set()
        while num:
            x, y = randint(0, self.row - 1), randint(0, self.col - 1)
            if self.board[x][y] != -1:
                mines.add((x, y))
                self.board[x][y] = -1
                num -= 1
                for _x, _y in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                    if 0 <= x + _x < self.row and 0 <= y + _y < self.col and self.board[x + _x][y + _y] != -1:
                        self.board[x + _x][y + _y] += 1
        return mines

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.row):
            for j in range(self.col):
                if (i, j) not in self.accessable and not self.win and not self.lose:
                    print('X', end=" ")
                else:
                    if self.board[i][j] == -1:
                        print("*", end=" ")
                    else:
                        print(self.board[i][j], end=" ")
            print(' ')

    def click(self,i, j):
        if (i, j) in self.accessable:
            print("This area has already been explored, try again")
            return False
        try:
            if self.board[i][j] == -1:
                self.lose = True
                self.accessable.add((i,j))
            else:
                self.bfs(i,j)
            if not self.lose and len(self.accessable) + len(self.mines) == self.row*self.col:
                self.win = True
            return True
        except IndexError as e:
            print("area out of board, try again")
            return False

    def bfs(self,i,j):
        Q = Queue()
        Q.put((i,j))
        while not Q.empty():
            i,j = Q.get()
            self.accessable.add((i,j))
            if self.board[i][j] == 0:
                for _i, _j in [[1,0],[-1,0],[0,1],[0,-1]]:
                    if 0<=i+_i<self.row and 0<=j+_j<self.col and (i+_i,j+_j) not in self.accessable:
                        Q.put((i+_i,j+_j))

if __name__ == '__main__':
    arglist = raw_input("Set row,col,mine nums\n").split(',')
    if arglist[0]:
        args = [int(arg) for arg in arglist]
    else:
        args = []
    ms = MineSweeper(*args)
    ms.display()
    while not ms.win and not ms.lose:
        i,j = raw_input("Please make your next move\n").split(',')
        if ms.click(int(i),int(j)):
            ms.display()
    if ms.win:
        print("congratulations, you have win this game")
    else:
        print("sorry, you reach a mine")
