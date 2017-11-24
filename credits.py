import pygame as pg

pg.init()

texto_lista = '''
    "Cachimbo Bros"

    Con las participaciones de...
Anthony Del Pozo (C) As Programador Master
Jose Espinoza As Programador Junior/Diseñador
Josue Palomino As Diseñador Master
Luis Villanueva As Programador Junior/Diseñador
Gustavo Reyes As "El hombre sin sombra"

    Participaciones especiales de...

    H. Quintana
    F. Riccio
    M. Campos
    D. Cardenas
    D. Llamas

    Agradecimientos

"La Cumbia de Pueblo Lavanda"
"Pan con Pollo Doña Peta"
"Manos S.A"
"La tiendita de Don Pepe"
"Codigo Facilito"

    2017 © Copyright
Todos los derechos Reservados


    ¡¡ARRIBA PERÚ!!


    ¡¡ERA HOY RAMON!!
    ¡¡ERA HOY RAMON TE DIJEEE!!!

'''.split('\n')


class Credits:
    def __init__(self, screen_rect, lst):
        self.srect = screen_rect
        self.lst = lst
        self.size = 20
        self.color = (255,255,255)
        self.buff_centery = self.srect.height/2 + 5
        self.buff_lines = 35
        self.timer = 0.0
        self.delay = 0
        self.hacer_surfaces()

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
            #Se va moviendo hacia abajo
            for texto, rect in self.text:
                rect.y -= 1

    def materializar(self, surfa):
        for text, rect in self.text:
            surfa.blit(text, rect)

pantalla = pg.display.set_mode((800,600))
rect_pantalla = pantalla.get_rect()
clock = pg.time.Clock()
salir = False

credi = Credits(rect_pantalla, texto_lista)

while not salir:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            salir=True
    pantalla.fill((0,0,0))
    credi.update()
    credi.materializar(pantalla)
    pg.display.update()
    clock.tick(80)
