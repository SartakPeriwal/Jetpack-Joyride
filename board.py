class Board:
    def __init__(self,rows,columns):
        self._columns = columns 
        self._rows = rows
        self._grid = [[' ' for i in range(10000)] for j in range(rows)]

        for i in range(10000):
            self._grid[0][i] = '\033[94m^\033[m'
            self._grid[1][i] = '\033[94m^\033[m'
            self._grid[rows-2][i] = '\033[42mT\033[m'
            self._grid[rows-1][i] = '\033[42m|\033[m'


    def print_board(self,start,man,drag): 
        str_B = ""
        coods=man.getcood()
        drag_lives=drag.getdraglives()
        if coods[1]<start:
            for i in range(2):
                man.move('d',self)
        if (coods[1]>200+start):
            for i in range(2):
                man.move('a',self)

        for line in self._grid:
            str_B += ''.join(line[start:start+200]) + '\n'
        
        coins=man.coingetter()
        lives_rem=man.lifegetter()
        str_B += "Total score-"
        str_B += str(coins)
        str_B += "\n"
        str_B += "Total lives remaining-"
        str_B += str(lives_rem)
        str_B += "\n"
        str_B += "Press Q to exit.\n"
        #str_B += "Drag-lives"
        #str_B += str(drag_lives)
        return str_B
    
    def set_cell(self, row, column, ch):
        self._grid[row][column] = ch

    def get_cell(self, row, column):
        return self._grid[row][column]


