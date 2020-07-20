from objects import Object
class Magnet(Object):
    def __init__(self,row,column):
        super().__init__(row, column)
        self._shape=[['\033[45mm\033[m',' ','\033[45mm\033[m'],['\033[45mm\033[m','\033[45mm\033[m','\033[45mm\033[m'],['\033[45mm\033[m',' ','\033[45mm\033[m']]
        self._size1=[3,3]
    def place(self,fr):
        for i in range(3):
            for j in range(3):
                fr.set_cell(i+self._row,j+self._column,self._shape[i][j])
    def remove(self,fr):
        for i in range(1):
            for j in range(1):
                fr.set_cell(i+self._row,j+self._column,' ')
    def attraction(self,man,fr):
        coods=man.getcood()
        
        if coods[1]>self._column-6 and coods[1]<=self._column+2:
            man.move('d',fr)
        if coods[1]>self._column+3 and coods[1] <self._column+9:
            man.move('a',fr)
        if coods[0] > self._row+4:
            if coods[1] >self._column -6 and coods[1]< self._column+9:
                man.move('w',fr)
    