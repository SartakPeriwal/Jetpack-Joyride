import os
import sys
from input import user_input
from board import Board 
from mando import Mando
from coins import Coin
from firebeam import Firebeam
from magnet import Magnet
from dragon import Dragon
from time import time
from bullet import Bullet
from random import randint
screen = Board(40,10000)
man=Mando(35,3)
man.place(screen)

drag=Dragon(30,500)
drag.place(screen)
for i in range (40):
    x=randint(5,30)
    y=randint(25,450)
    coin_p=Coin(x,y)
    coin_p.place(screen)

for j in range (10,30):
    x=randint(5,30)
    y=randint(50,350)
    beam=Firebeam(x,y)
    beam.place(screen)

mag=Magnet(2,80)
mag.place(screen)

counter3=time()
screen.print_board(0,man,drag)
#print("time left==")
#print(100-counter3)



count_gravity=0
count_magnet=0
count_board=0
print_range=0
count_pace=0
counter=time()
counter2=time()
counter_dragbull=0
while True:
    #getch = Get()
    ch = user_input()
    if ch == 'q':
        exit()
    if ch in ['a','d','w']:
        man.move(ch, screen)
    if ch =='p':
        count_pace+=2
    
    if ch==' ':
        if time()-counter2 > 60:
            man.setshield(1)
            counter2=time()
            counter = time()
    check_shield=man.getshield()
    if check_shield==1:
        if time()- counter > 10:
            counter = time()
            counter2 = time()
            man.setshield(0)


    if ch=='b':
        man.shoot(screen)
    if counter_dragbull %20==0:
        cood=man.getcood()
        cood_drag=drag.getcood()
        if cood_drag[1]-cood[1] < 200:
            drag.shoot(screen)
    
    for i in range(2):
        man.move_bullet(screen,drag,man)

    drag.move_bullet(screen,drag,man)


    count_gravity+=1.5

    count_magnet+=1

    count_board+=1
    counter_dragbull+=1

    # if count_setshield == 5:
    #     man.setshield(0)
    #     count_setshield=0

    #if counter3==100:
    #    os.system('clear')
    #    print("timeup speedup your game next time")
    #    exit()

    if count_gravity==6:
        man.gravity(screen)
        #print("gravity")
        count_gravity=0

    if count_magnet==7:
        mag.attraction(man,screen)
        count_magnet=0

    if count_board==4:
        print_range+=1
        count_board=0

    drag.follow(man,screen)
    os.system('clear')

    if count_pace==2:
        for i in range(0,4):
            print_range+=1
            print(screen.print_board(print_range,man,drag))
            print("time left==")
            counter4=time()-counter3

            print(100-counter4)
            os.system('clear')
        count_pace=0   
    
    print(screen.print_board(print_range,man,drag))
    print("time left==")
    counter4=time()-counter3
    print(100-counter4)
    if time()-counter3 > 100:
        os.system('clear')
        print("timeup speedup your game next time")
        exit()
        
