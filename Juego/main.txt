#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Imports
import pygame
import sys
from pygame.locals import *

from source.Utils import *
from source.Entities import *
from source.States import *


size = width, height = (960,600)
screen = pygame.display.set_mode(size)
pygame.init()


# Método para pintar el título
def draw_title(msg, color=Color.YELLOW):
    font = pygame.font.SysFont(None, 80)
    title = font.render(msg,True, color)
    screen.blit(title, (width - title.get_rect().width - 20,140))
    
# Método para pintar textos
def draw_label(msg, color=Color.YELLOW, x=0, y=0, size=40):
    font = pygame.font.SysFont(None, size)
    title = font.render(msg,True, color)
    screen.blit(title, (x, y))

# Método para pintar una imagen
def draw_image(path, x, y):
    image = pygame.image.load(path)
    rect = image.get_rect()
    screen.blit(image, rect)


class EditText():
    
    """ 
        Clase que genera un input en formato EditTExt
    """

    # Constructor
    def __init__(self, x=0, y=0, width=200, height=40, border=2, value='',focus=False , max=20):
        self.x = x
        self.y = y
        self.width = max * 7 if width < max * 7 else width
        self.height = height
        self.border = border
        self.value = value
        self.max = max
        self.focus = focus
        self.rect = self.draw()

    # Escribir dentro del input
    def type_char(self, char):
        if len(self.value) < self.max and self.focus:
            self.value = ''.join([self.value, char])

    # Cambiar el color de los bordes, se modifican con el atributo Focus
    def load_border_color(self):
        return Color.YELLOW   if self.focus else Color.BLACK

    # Dibujar el input en el Display
    def draw(self):
        margin = 5
        size = 40
        font = pygame.font.SysFont(None, size)
        title = font.render(self.value,True, Color.BLACK)
        screen.blit(title, (self.x + margin, self.y + margin))
        return pygame.draw.rect(screen, self.load_border_color(),(self.x,self.y,self.width,self.height),self.border)
    
    # Evaluar si hicieron click dentro de la input (caja)
    def collidepoint(self,mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.focus = True
        else:
            self.focus = False

    # Renderiza los nuevos cambios del input
    def update(self, e):
        self.draw()
        if e.type == KEYDOWN:
            # Catch enter
            if pygame.key.name(e.key) in ['up','down','left','right']:
                return
            if e.key == 'return':
                return True
            # Move cursor
            # elif key == 'left':
            #      self._cursor_back()
            # elif key == 'right':
            #     self._cursor_forward()
            # # Edit text
            # elif key == 'backspace':
            #      self._backspace()
            elif e.key == K_BACKSPACE:
                self.value = self.value[0:len(self.value)-1]
            elif e.key == K_SPACE:
                self.type_char(' ')
            elif len(e.unicode) == 1:
                self.type_char(e.unicode)
            # Signal event unused
            else:
                r = True
    

class RadioButtonManager():
    
    """ 
        Clase gestora del comportamiento de los radios buttons
    """

    # Constructor
    def __init__(self):
        self.buttons = []
    
    # Agrega botones al Radio Group
    def add_button(self,button):
        button.manager = self
        self.buttons.append(button)

    # Obtiene los botones del Radio Group
    def get_buttons(self,):
        return self.buttons

    # Elige el botón clickeado y deselecciona los otros botones
    def manage_select(self,clicked_button):
        for button in self.buttons:
            if button == clicked_button:
                button.focus = True
            else:
                button.focus = False

    

class Button():
    
    """ 
        Clase que genera y gestiona un botón 
    """

    # Constuctor
    def __init__(self, x=0, y=0, width=200, height=40, border=2, value='', focus=False):
        self.x = x
        self.y = y
        self.width = len(value) * 19 if width < len(value) * 19 else width
        self.height = height
        self.border = border
        self.value = value
        self.focus = focus 
        self.rect = self.draw()

    # Cambiar el color de los bordes, se modifican con el atributo Focus
    def load_border_color(self):
        return Color.YELLOW  if self.focus else Color.BLACK

    # Evalua si el botón fue clickeado
    def collidepoint(self,mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.manager.manage_select(self)
    
    # Renderiza el botón en el Display
    def draw(self):
        margin = 5
        size = 40
        font = pygame.font.SysFont(None, size)
        title = font.render(self.value,True, self.load_border_color())
        screen.blit(title, (self.x + margin, self.y + margin))
        return pygame.draw.rect(screen, self.load_border_color(),(self.x,self.y,self.width,self.height),self.border)

# Método principal que ejecuta todo el Hilo
def main():
    
    # Objetos en pantalla
    path_cachimbo = ('assets/img/characters/cachimbo/CACHIMBO_WALK.png','assets/img/characters/practicante/PRACTICANTE_WALK.png')
    path_cachimba = ('assets/img/characters/cachimba/CACHIMBA_WALK.png','assets/img/characters/cachimba/CACHIMBA_WALK.png')
    path_fondo_u_lima = 'assets/img/scenarios/u-de-lima.png'
    drawable_sprites = pygame.sprite.Group()
    cachimbo = Character(screen,path_cachimbo,3,150,250,2)
    cachimba = Character(screen,path_cachimba,3,150,250,2)
    edit_text = EditText(500,390,320,35,2,'',True,20)
    button_cachimbo = Button(500,290,130,35,2,'Cachimbo',True)
    button_cachimba = Button(670,290,130,35,2,'Cachimba')
    button_jugar = Button(600,490,110,35,2,'  Jugar',True)
    button_manager = RadioButtonManager()
    button_manager.add_button(button_cachimbo)
    button_manager.add_button(button_cachimba)
    
    while True:
        for event in pygame.event.get():
            # Agregar KEY LONG PRESSED
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                cachimbo.key_down(event.key)
                cachimba.key_down(event.key)
                edit_text.update(event)
            elif event.type == KEYUP:
                cachimbo.key_up(event.key)
                cachimba.key_up(event.key)
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                edit_text.collidepoint(mouse_position)
                button_cachimbo.collidepoint(mouse_position)
                button_cachimba.collidepoint(mouse_position)

        screen.fill((255,255,255))
        draw_image(path_fondo_u_lima,0,0)
        pygame.draw.rect(screen, Color.YELLOW,(0,130,width,75),2)
        draw_title('Seleccionar Personaje')
        edit_text.draw()
        button_cachimbo.draw()
        button_cachimba.draw()
        button_jugar.draw()
        draw_label('Elije a tu personaje favorito',Color.YELLOW,500,250)
        draw_label('Nombre',Color.YELLOW,500,350)
        draw_label('Presionar "ctrl" para transformar ',Color.YELLOW,5,height-20,20)
        dt = pygame.time.Clock().tick(120)

        cachimbo.update(dt)
        cachimba.update(dt)
        if button_cachimbo.focus:
            cachimbo.draw()
        else:
            cachimba.draw()


        for sprite in drawable_sprites.sprites():
            sprite.draw()

        pygame.display.flip()
        

if __name__ == '__main__':
    main()