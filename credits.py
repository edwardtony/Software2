import pygame as pg

pg.init()

texto_lista = '''
    "Cachimbo Bros"

    Con las participaciones de...


'''.split('\n')


class Credits:
    def __init__(self, screen_rect, lst):
        self.srect = screen_rect
        self.lst = lst
        self.size = 16
        self.color = (255,255,255)
        self.buff_centery = self.srect.height/2 + 5
        self.buff_lines = 50
        self.timer = 0.0
        self.delay = 1
        self.make_surfaces()

    def hacer_texto(self, msj):
        #Creas la fuente
        font = pg.font.SysFont('comicsansms', self.size)
        #Creas el texto
        text = font.render(msj,True,self.color)
        #Obtener rect y redefinir center
        rect = text.get_rect(center=(self.srect.centerx, self.srect.centery + self.buff_centery))
        #Devolver texto y rect
        return text, rect

    def hacer_surfaces(self):
        #arreglo de lineas
        self.text = []
        #Se agregan las lineas al arreglo
        for i, line in enumerate(self.lst):
            l = self.hacer_texto(line)
            l[1].y += i*self.buff_lines
            self.text.append(l)

    def update(self):
        if pg.time.get_ticks() - self.timer > self.delay:
            self.timer = pg.time.get_ticks()
            for texto, rect in self.text:
                rect.y=-1            
