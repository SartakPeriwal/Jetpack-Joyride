from bullet import Bullet
from person import Person
class Dragon(Person):
    def __init__(self,row,column):
        super().__init__(row, column)
        self._shape=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\033[90m\033[m,', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '\033[90m.\033[m', '\033[90m.\033[m', '\033[90mf\033[m', ' ', ' ', ' '], [' ', '\033[90m.\033[m', '\033[90m.\033[m', '\033[90m,\033[m', '\033[90m6\033[m', '\033[90m)\033[m', ' ', ' ', '\033[90m"\033[m', '\033[90m_\033[m', ' '], ['\033[90m(\033[m', '\033[90mo\033[m', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\033[90m"\033[m'], [' ', ' ', ' ', ' ', '\033[90m"\033[m', '\033[90m"\033[m', '', '', '\033[90m~\033[m', '\033[90m"\033[m', '\033[90m.\033[m'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\033[90m"\033[m', '\033[90m.\033[m']]
        self._size=[6,11]
        self._bulllist=[]
        self._drag_lives=120
    def place(self,fr):
        for i in range(6):
            for j in range(11):
                fr.set_cell(i+self._row,j+self._column,self._shape[i][j])
    def remove(self,fr):
        for i in range(6):
            for j in range(11):
                fr.set_cell(i+self._row,j+self._column,' ')
    def follow(self,man,fr):
        coods=man.getcood()
        if self._row < coods[0]:
            self.move('s',fr)
        if self._row >= coods[0]:
            self.move('w',fr)
    def collision_check(self,row,column,fr):
        return False    
    def move_bullet(self,fr,drag,mando):
        for i in self._bulllist:
            i.move_dragon(fr,drag,mando)
    def getdraglives(self):
        return self._drag_lives
    def setdraglives(self,en):
        self._drag_lives=en
    def getcood(self):
        return [self._row,self._column]