from bullet import Bullet
from board import Board

class Person:
    def __init__(self,row,column):
        self._row=row
        self._column=column
        self._shape=[[]]

    def move(self,ch,fr):
        coo_col = 0
        coo_row = 0
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                fr.set_cell(i+self._row,j+self._column,' ')
        if ch=='d':
            coo_col=self._column + 2
            coo_row=self._row
        elif ch=='a':
            coo_col=self._column - 2
            coo_row=self._row
        elif ch=='w':
            coo_col=self._column
            coo_row=self._row -2
        elif ch=='s':
            coo_col=self._column
            coo_row=self._row + 1

        if coo_row > 37 - self._size[0] + 1:
            coo_row = 37 - self._size[0] + 1
        if coo_row < 3:
            coo_row = 3
        if (self.collision_check(coo_row,coo_col,fr)==False):
            self._row=coo_row
            self._column=coo_col
        self.place(fr)

    def shoot(self,fr):
        coods=[self._row,self._column]
        bull=Bullet(coods[0],coods[1])
        bull.place(fr)
        self._bulllist.append(bull)
    def move_bullet(self,fr):
        pass