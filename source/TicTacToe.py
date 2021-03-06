from Screen import Screen
from buttons import TextButton
from random import random
from time import sleep
import pygame

class TicTacToe:
    def __init__(self):
        self.values=[]
        self.xTurn=True
        self.winner=None
        self.ended=False
        self.timer = 100
        for i in range(9):
            self.values.append(0)
            
        self.buttons=[]
        for i in range(3):
            
            button=TextButton(i* 200,0,2,1,210,210)
            button.set_text("")
            self.buttons.append(button)
        for i in range(3):
            
            button=TextButton(i* 200,200,2,1,210,210)
            button.set_text("")
            self.buttons.append(button)
        for i in range(3):
            
            button=TextButton(i* 200,400,2,1,210,210)
            button.set_text("")
            self.buttons.append(button)
    def show(self,screen):
        for b in self.buttons:
            b.act(screen)
        value=self.endGame()
        
        if(isinstance(value,(list,tuple))):
            self.ended=True
            self.timer-=1
            pygame.draw.line(screen.screen,(0,255,0),(self.buttons[value[0]].xpos+ 100,self.buttons[value[0]].ypos+ 100),(self.buttons[value[1]].xpos+ 100,self.buttons[value[1]].ypos+ 100),10)
            if(self.timer <=0):
                return -1
            if(self.values[value[0]]==1):
                player= "X"
            elif(self.values[value[0]]==2):
                 player="O"
            screen.showWords("PLAYER "+player,100,50,200)
            screen.showWords("WINS ",100,50,300)
        return 0     
                 
            
    def same(self,lista):
        value=None
        for i in lista:
            if(value==None):
                value=i
            if(i != value):
                return False,-1
        start=lista[0]
        end= lista[2]
        return (True,value)
    def endGame(self):
        ended=False
        if(self.values[0]!=0):
            for i in range(2):
                act= self.same((self.values[0],self.values[2*i +1],self.values[2*(2*i +1)]))
                ended+=act[0]
                if(ended):
                    return(0,2*(2*i+1))
##            ended+= self.same((self.values[0],self.values[1],self.values[2]))
##            ended+= self.same((self.values[0],self.values[3],self.values[6]))
        if(self.values[4]!=0):
            for i in range(4):
                act= self.same((self.values[i],self.values[4],self.values[8-i]))
                ended+=act[0]
                if(ended):
                    return(i,8-i)
        if(self.values[8]!=0):
            for i in range(2):
                act= self.same((self.values[6- 4 * i],self.values[7- i * 2],self.values[8]))
                ended+=act[0]
                if(ended):
                    return(6- 4 * i,8)
        return None
                

        
                
            
    def start(self,screen):
        screen.drawRect((0,0,0),(0,0,600,600))
        screen.drawRect((255,0,0),(100,100,400,400))
        screen.showWords("TIC",100,200,150,(0,200,0))
        sleep(1)
        act= screen.act()
        screen.showWords("TAC",100,200,250,(0,200,100))
        sleep(1)
        act= screen.act()
        screen.showWords("TOE",100,200,350,(146,200,250))
        sleep(1)
        
        act= screen.act()
        while(not isinstance(act, (list, tuple))):
            screen.drawRect((255,0,0),(100,100,400,400))
            screen.showWords("TIC",100,200,150,(0,200,0))
            screen.showWords("TAC",100,200,250,(0,200,100))
            screen.showWords("TOE",100,200,350,(146,200,250))
            screen.showWords("click to start",20,180,550,(255,255,255))
            act= screen.act()
            
    def setX(self,i):
        b= self.buttons[i]
        button =TextButton(b.xpos,b.ypos,1,1,210,210)
        button.set_text("X",None,200,button.xpos + button.sizeX/ 5,button.ypos - button.sizeY /10)
        button.press()
        self.buttons[i]=button
        self.values[i]=1
        self.xTurn=False
    def setO(self,i):
        b= self.buttons[i]
        button =TextButton(b.xpos,b.ypos,3,1,210,210)
        button.set_text("O",None,200,button.xpos + button.sizeX/ 5,button.ypos - button.sizeY /10)
        button.press()
        self.buttons[i]=button
        self.values[i]=2
        self.xTurn=True
    def press(self,pos):
      if(not self.ended):  
        for i in range(len(self.buttons)):
                if(self.buttons[i].inside(pos)):
                    if(self.values[i] ==0):
                        
                        self.buttons[i].press()
                        if(self.xTurn):
                            self.setX(i)
                            return 1
                        else:
                            self.setO(i)
                            return 1
                
      return 0
            

def main_old():

    screen=Screen(600,600)
    screen.start()
    b=[]
    active= True
    tic=TicTacToe()
    tic.start(screen)
    reset_counter= 0
    while(active):
        

        
        if(tic.show(screen)==-1):
            tic=TicTacToe()
            tic.start(screen)
            continue
        act= screen.act()
        if(isinstance(act, (list, tuple))):
          if(act[0]>=0):
            tic.press(act[1])
                
        if(act == -1 ):
            
            active = False
            break
        if(act=='r'or reset_counter< 0):
            tic=TicTacToe()
            tic.start(screen)
            reset_counter=0
        if( 0 not in tic.values ):
            if(reset_counter <=0):
                reset_counter= 101
            else:
                reset_counter-=2
    screen.close()

main_old()
