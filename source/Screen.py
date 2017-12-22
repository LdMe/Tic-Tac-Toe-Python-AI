
import pygame
from time import sleep

import datetime
from events import Events
class Screen:
    """
#######################################################################
##Clase Screen: realiza las funciones basicas de una interfaz grafica##
#######################################################################
-----------------------------------------------------------------------
Atributos:
    [*] X,Y :
            ancho,largo de la pantalla
    [*] event:
            objeto que captura los eventos y
            devuelve un valor dependiendo del evento
    [*] screen:
            pantalla, clase de pygame:
                pygame.display.set_mode((X,Y))
        
Metodos:
    [*] __init__(X,Y,name):
          (X,Y)->(ancho,largo) de la interfaz
          name -> nombre
    [*] capture():
            captura de pantalla
    [*] plot( x,color):
            dibuja lineas entre los elementos (xi,yi) del array x
    [*] start():
            Inicializa la interfaz grafica
    [*] load(image,x,y):
            carga la imagen con las medidas x,y
    [*] show(image,X):
            muestra la imagen 'image' en pantalla, en la posicion X (X0,X1)
    [*] close():
            cierra la interfaz grafica
    [*] drawRect(color,rect,width):
            dibuja la recta introducida 
    [*] act():
            actualiza las imagenes
    [*] showWords(words,size,x,y,color):
            muestra en pantalla una frase
                words -> frase a mostrar
                size -> escala de la fuente
                x,y -> coordenadas en la pantalla
                color -> color de las letras, (r,g,b)
    """
    def __init__(self,X,Y,name="game"):
        self.X=X
        self.Y=Y
        self.start()
        self.event= Events()
        self.game = pygame.init()
    def capture(self):
        pygame.image.save(self.screen,"ScreenCapture"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+".jpg")
    def plot(self,lista,color=(0,0,0)):
        last= None
        for (x,y) in lista:
            if(not last):
                last=(x,y)
            else:
                pygame.draw.line(self.screen,color,last,(x,y),1)
                last=(x,y)
            
    def start(self):
        
        self.screen = pygame.display.set_mode((self.X,self.Y))
        pygame.display.set_caption('game')
    def load(self,image,x=0,y=0):
        if((x,y)==(0,0)):
            x= self.X
            y=self.Y
        fondo = pygame.image.load(image)
        fondo = pygame.transform.scale(fondo,(x,y))
        return fondo
    def show(self,image,X=(0,0)):
        self.screen.blit(image,X)
    def close(self):
        pygame.quit()
    def drawRect(self,color,Rect,width=0):
        pygame.draw.rect(self.screen,color,Rect,width)
    def update(self):
        pygame.display.update()
    def act(self):
        pygame.display.update()
        self.event.get()
        return self.event.act()
    def showWords(self,words, size, x, y, color = (255,255,0)):
        
        myfont = pygame.font.SysFont("monospace", size)

# render text
        label = myfont.render(words, 1, color)
        self.show(label,(x,y))


if __name__== "__main__":
	def prueba1(x,y):
		a=Screen(x,y,"prueba")
		f=a.load("LED_game.png")
		a.show(f)
		a.showWords("prueba",x/10,x/2,y/2)
		a.act()
		sleep(2)
		a.close()
		a.start()
		sleep(1)
		a.close()

		
	prueba1(400,400)
