from objects import Object
import os
class Bullet(Object):
    def __init__(self,row,column):
        super().__init__(row, column+5)
        self._shape=[['\033[30m*\033[m']]
        self._size1=[1,1]
    def place(self,fr):
         for i in range(1):
            for j in range(1):
                fr.set_cell(i+self._row,j+self._column,self._shape[i][j])
    def move_man(self,fr,drag,mando):
        for i in range(1):
            for j in range(1):
                fr.set_cell(i+self._row,j+self._column,' ')
        coo_col=self._column+1
        coo_row=self._row

        if (self.collision_check(coo_row,coo_col,fr,drag,mando)==False):
            self._column=coo_col
            for i in range(1):
                for j in range(1):
                    fr.set_cell(i+self._row,j+self._column,self._shape[i][j])
        else:
            self._column=coo_col
            for i in range(1):
                for j in range(1):
                    fr.set_cell(i+self._row,j+self._column,' ')


    def move_dragon(self,fr,drag,mando):
        for i in range(1):
            for j in range(1):
                fr.set_cell(i+self._row,j+self._column,' ')
        coo_col=self._column-1
        coo_row=self._row

        if (self.collision_check(coo_row,coo_col,fr,drag,mando)==False):
            self._column=coo_col
            for i in range(1):
                for j in range(1):
                    fr.set_cell(i+self._row,j+self._column,self._shape[i][j])
        else:
            self.remove(fr)

    def remove(self,fr):
        self._column-=1
        for i in range(1):
           for j in range(1):
              fr.set_cell(i+self._row,j+self._column,' ')
    def collision_check(self,row,column,fr,drag,mando):
        flag=0
        #drag_symbols=['.',',','f','6',')','(','"','_','o','~','*']
        drag_symbols=['\033[90m.\033[m','\033[90m,\033[m','\033[90mf\033[m','\033[90m6\033[m','\033[90m)\033[m','\033[90m(\033[m','\033[90m"\033[m','\033[90m_\033[m','\033[90mo\033[m','\033[90m~\033[m','\033[30m*\033[m']
        mando_symbols=[']','{','}']
        for i in range(1):
            for j in range(1):
                ch=fr.get_cell(row,column)    
                #if ch=='$':
                #   self._coins+=1
                    #return False
                if ch=='\033[91m-\033[m':
                    score=mando.coingetter()
                    score+=15
                    mando.coinsetter(score)
                    for k in range (0,7):
                        ch2=fr.get_cell(row,column+k-3)
                        if ch2=='\033[91m-\033[m':
                            fr.set_cell(row,column+k-3,' ')
                    flag=1    
                if ch=='\033[91m/\033[m':
                    score=mando.coingetter()
                    score+=15
                    mando.coinsetter(score)
                    for k in range(0,7):
                        ch2=fr.get_cell(row+k-3,column-k+3)
                        if ch2=='\033[91m/\033[m':
                            fr.set_cell(row+k-3,column-k+3,' ')
                    flag=1
                        
                    # if self._shield==0:
                    #     flag=1
                    #     self._lives-=1
                    #     if self._lives==0:
                    #         exit()
                    #     self._row=35
                    #     self.place(fr)
                    # if self._shield==1:
                    #     flag=1
                if ch=='\033[91m|\033[m':
                    score=mando.coingetter()
                    score+=15
                    mando.coinsetter(score)
                    for k in range(0,7):
                        ch2=fr.get_cell(row+k-3,column)
                        if ch2=='\033[91m|\033[m':
                            fr.set_cell(row+k-3,column,' ')
                    flag=1
                    # if self._shield==0:
                    #     flag=1
                    #     self._lives-=1
                    #     if self._lives==0:
                    #         exit()
                    #     self._row=35
                    #     self.place(fr)
                    # if self._shield==1:
                    #     flag=1
                # if ch=='m':
                #     flag=1
                if ch in drag_symbols:
                    drag_live=drag.getdraglives()
                    mando_cood=mando.getcood()
                    drag_cood=drag.getcood()
                    
                    if drag_cood[1]-mando_cood[1]<150:
                        drag_live-=1
                        score=mando.coingetter()
                        mando.coinsetter(score)
                    drag.setdraglives(drag_live)
                    if drag_live==0:

                        score=mando.coingetter()
                        score+=100

                        mando.coinsetter(score)
                        os.system('clear')
                        print("YOU WON\n YOUR SCORE is")
                        print(score)
                        
                        exit()
                    
                    #self.remove(fr)
                    flag=1
                if ch in mando_symbols:
                    #os.system('clear')
                    #print("BuLLLLLLLLLLLLLLLLEt")

                    isshield=mando.getshield()
                    mando_cood=mando.getcood()
                    drag_cood=drag.getcood()
                    mando_live=mando.lifegetter()
                    if drag_cood[1]-mando_cood[1]<150:
                        
                        if isshield==0:
                            mando_live-=1
                            print("BuLLLLLLLLLLLLLLLLEt")
                    if mando_live==0:
                        os.system('clear')
                        print("YOU LOST")
                        exit()
                    #mando.setcood()
                    #self.place(fr)
                    mando.lifesetter(mando_live)
        if flag==0:
            return False
        if flag==1:
            #self.remove(fr)
            return True

                
