from objects import Object
class Coin(Object):
    def __init__(self,row,column):
        super().__init__(row, column)
        self._shape=[['\033[93m$\033[m']]
        self._size1=[1,1]
    def place(self,fr):
        for i in range(1):
            for j in range(1):
                fr.set_cell(i+self._row,j+self._column,self._shape[i][j])
    def remove(self,fr):
        for i in range(1):
            for j in range(1):
                fr.set_cell(i+self._row,j+self._column,' ')
    