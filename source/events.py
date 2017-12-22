import pygame




class Events:
    """
#######################################################################
##Clase Events: captura los eventos del raton y el teclado           ##
#######################################################################
-----------------------------------------------------------------------
Atributos:
    [*] LEFT,RIGHT,LEFT_RIGHT:
            botones del raton
Metodos:
    [*] get():
            captura todos los eventos ocurridos desde la ultima captura
    [*] act():
            devuelve un valor determinado dependiendo de la tecla o boton
            que se pulse o deje de pulsar
        
    """
    LEFT = (1,0,0)
    RIGHT = (0,0,1)
    LEFT_RIGHT= (1,0,1)
    def get(self):
        e=pygame.event.get()
        self.lista=e
    def getMouse(self):
        pos =pygame.mouse.get_pos()
        return pos
    def act(self):
        for event in self.lista:
            if(event.type == pygame.MOUSEBUTTONDOWN ):
                pos =pygame.mouse.get_pos()
                self.button =pygame.mouse.get_pressed()
                if(self.button == self.LEFT):
                    return (1,pos)
                elif(self.button == self.RIGHT):
                    return (2,pos)
                
            if(event.type == pygame.MOUSEBUTTONUP ):
                pos =pygame.mouse.get_pos()
                self.button =pygame.mouse.get_pressed()
                return (-1,pos)
                
            elif(event.type == pygame.KEYDOWN ):
                if (event.key == pygame.K_ESCAPE):
                    return -1
                if (event.key == pygame.K_SPACE):
                    return 's'
                if (event.key == pygame.K_c):
                    return 'c'
                if (event.key == pygame.K_r):
                    return 'r'
                pass
            elif(event.type == pygame.KEYUP ):
                pass
        return 0
