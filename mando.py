from person import Person
from bullet import Bullet
import os
class Mando(Person):
    def __init__(self,row,column):
        super().__init__(row, column)
        self._shape=[['[', ' ',']'],[' ','{',' '],[' ','}',' ']]
        self._shieldshape=[['\033[30m]',' ','['],[' ','}',' '],['}',' ','{\033[m']]
        self._speed=1
        self._size=[3,3]
        self._shield=0
        self._bulllist=[]
        self._score=0
        self._lives=3
    def place(self,fr):
        if self._shield==0:
            for i in range(3):
                for j in range(3):
                    fr.set_cell(i+self._row,j+self._column,self._shape[i][j])
        if self._shield==1:
            for i in range(3):
                for j in range(3):
                    fr.set_cell(i+self._row,j+self._column,self._shieldshape[i][j])
    
    def gravity(self,fr):
        coo_col = 0 
        coo_row = 0
        if self._row==35:
            ground=1
        if self._row < 35:
            for i in range(3):
                for j in range(3):
                    fr.set_cell(i+self._row,j+self._column,' ')
            coo_col=self._column
            coo_row=self._row + self._speed
            if coo_row > 35 :
                coo_row=35
            if(self.collision_check(coo_row,coo_col,fr)==False):
                self._row=coo_row
                self._col=coo_col
        
        self.place(fr)
        if self._row==coo_row:
            self._speed+=1
        else:
            self._speed=1 
    
    def move_bullet(self,fr,drag,mando):
        for i in self._bulllist:
            i.move_man(fr,drag,mando)
            
    def getcood(self):
        return [self._row,self._column]
    def getshield(self):
        return self._shield
    def setshield(self,en):
        self._shield=en
    def setcood(self,row,column):
        self._row=row
        self._column=column

    def coingetter(self):
        return self._score
    def coinsetter(self,score):
        self._score=score

    def lifegetter(self):
        return self._lives
    def lifesetter(self,lif):
        self._lives=lif


    def collision_check(self,row,column,fr):
        flag=0
        drag_symbols=['\033[90m.\033[m','\033[90m,\033[m','\033[90mf\033[m','\033[90m6\033[m','\033[90m)\033[m','\033[90m(\033[m','\033[90m"\033[m','\033[90m_\033[m','\033[90mo\033[m','\033[90m~\033[m','\033[30m*\033[m']
        for i in range(3):
            for j in range(3):
                ch=fr.get_cell(i+row,j+column)    
                if ch=='\033[93m$\033[m':
                    self._score+=10
                    #return False
                if ch=='\033[91m-\033[m':
                    if self._shield==0:
                        flag=1
                        self._lives-=1
                        if self._lives==0:
                            os.system('clear')
                            print("YOU LOST")
                            exit()
                        self._row=35
                        self.place(fr)
                    if self._shield==1:
                        flag=1
                if ch=='\033[91m/\033[m':
                    if self._shield==0:
                        flag=1
                        self._lives-=1
                        if self._lives==0:
                            os.system('clear')
                            print("YOU LOST")
                            exit()
                        self._row=35
                        self.place(fr)
                    if self._shield==1:
                        flag=1
                if ch=='\033[91m|\033[m':
                    if self._shield==0:
                        flag=1
                        self._lives-=1
                        if self._lives==0:
                            os.system('clear')
                            print("YOU LOST")
                            exit()
                        self._row=35
                        self.place(fr)
                    if self._shield==1:
                        flag=1
                if ch=='\033[45mm\033[m':
                    flag=1
                if ch in drag_symbols:
                    if self._shield==0:
                        flag=1
                        self._lives-=1
                        if self._lives==0:
                            os.system('clear')
                            print("YOU LOST")
                            exit()
                        self._row=35
                        self.place(fr)
                    if self._shield==1:
                        flag=1
        if flag==0:
            return False
        if flag==1:
            return True

                        

        #return False    
