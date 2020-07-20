import random
from objects import Object
class Firebeam(Object):
    def __init__(self,row,column):
        super().__init__(row,column)
        self._shape1=[['\033[91m|\033[m'],['\033[91m|\033[m'],['\033[91m|\033[m'],['\033[91m|\033[m']]
        self._size1=[4,1]
        self._shape2=[['\033[91m-\033[m','\033[91m-\033[m','\033[91m-\033[m','\033[91m-\033[m']]
        self._size2=[1,4]
        self._shape3=[[' ',' ',' ','\033[91m/\033[m'],[' ',' ','\033[91m/\033[m',' '],[' ','\033[91m/\033[m',' ',' '],['\033[91m/\033[m',' ',' ',' ']]
        self._size3=[4,4]
        self._type=random.randint(1,3)

    def place(self,fr):
        v=self._type
        if v==1:
            for i in range(4):
                for j in range(1):
                    fr.set_cell(i+self._row,j+self._column,self._shape1[i][j])
        if v==2:
            for i in range(1):
                for j in range(4):
                    fr.set_cell(i+self._row,j+self._column,self._shape2[i][j])
        if v==3:
            for i in range(4):
                for j in range(4):
                    fr.set_cell(i+self._row,j+self._column,self._shape3[i][j])
    def remove(self,fr):
        v=self._type
        if v==1:
            for i in range(4):
                for j in range(1):
                    fr.set_cell(i+self._row,j+self._column,' ')
        if v==2:
            for i in range(1):
                for j in range(4):
                    fr.set_cell(i+self._row,j+self._column,' ')
        if v==3:
            for i in range(4):
                for j in range(4):
                    fr.set_cell(i+self._row,j+self._column,' ')
        
        
        
        