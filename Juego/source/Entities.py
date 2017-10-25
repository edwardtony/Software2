#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from States import AnimatedState, StaticState

"""
    Este es el archivo que se encargará de trabajar todas entidades del juego
"""

class GameEntity(pygame.sprite.Sprite):

    """
        Entidad Padre que se encarga de implementar el modelo de los personajes,
        gestionar sus estados y firmar el método Update para los renderizados de los
        Sprites.
    """

    # Constuctor
    def __init__(self, display):
        super(GameEntity, self).__init__()

        self.display = display
        self.states_dict = {}
        self.current_state = None
        self.dx = 0
        self.dy = 0
        self.image = None
        self.jumping = False

    # Método para asignar un estado actual (Sprite)
    def set_current_state(self, key):
        self.current_state = self.states_dict[key]

    # Método que asigna los nuevos valores de la posición del Character
    def impulse(self, dx, dy):
        self.dx = dx
        self.dy = dy

    # Método que actualiza el estado y Sprite del Character, debe ser sobreescrito debido a que los algunos Characters tienen comportamientos diferentes.
    def update(self, dt):
        raise NotImplementedError("The update method must be called in any child class")

    # Método que imprime en el Display al Character
    def draw(self):
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.display.blit(self.image, (self.rect.x, self.rect.y))

class Character(GameEntity):

    """
        Clase encargada de gestionar la configuración y acciones de un personaje,
        Extiende de GameEntity
    """

    # Constructor
    def __init__(self, display, path, number_of_sprites, px, py, scale = 1, mode = 0):
        super(Character, self).__init__(display)
        self.speed = 7
        self.path = path
        self.number_of_sprites = number_of_sprites
        self.mode = mode
        self.load_image()
        self.image = self.current_state.get_sprite()
        self.rect = self.scale(scale)
        self.pos_x = px
        self.rect.x = px
        self.rect.y = py
        self.accelerating = False
        self.jumping = False

    # Permite dimensionar la imagen escalándola de tamaño
    def scale(self,scale):
        return pygame.Rect(0,0,self.image.get_rect().width*scale,self.image.get_rect().height*scale)

    # Carga la imagen del personaje, los animados, los estáticos y el estado actual
    def load_image(self):
        path = self.path[self.mode]
        self.walking_images = pygame.image.load(path)

        self.walking_right_state = AnimatedState(self.walking_images.subsurface(0,0,
                                                 self.walking_images.get_width(),
                                                 self.walking_images.get_height()/2),
                                                 self.number_of_sprites, 150, "walking_right")
        self.walking_left_state = AnimatedState(self.walking_images.subsurface(0,
                                                self.walking_images.get_height()/2,
                                                self.walking_images.get_width(),
                                                self.walking_images.get_height()/2),
                                                self.number_of_sprites, 150, "walking_left")

        self.resting_left_state = StaticState(self.walking_images.subsurface(0,
                                              self.walking_images.get_height()/2,
                                              self.walking_images.get_width()/self.number_of_sprites,
                                              self.walking_images.get_height()/2),
                                               "resting_left")

        self.resting_right_state = StaticState(self.walking_images.subsurface(0,0,
                                               self.walking_images.get_width()/self.number_of_sprites,
                                               self.walking_images.get_height()/2),
                                               "resting_right")

        self.states_dict["walking_right"] = self.walking_right_state
        self.states_dict["walking_left"] = self.walking_left_state
        self.states_dict["resting_left"] = self.resting_left_state
        self.states_dict["resting_right"] = self.resting_right_state
        self.set_current_state("resting_right")

    # Método encargado de gestionar la lógica de la gravedad, gravedad es la velocidad con la cual caen los objetos en el juego
    def calculate_gravity(self):
        if self.dy == 0:
            self.dy = 0.7
        else:
            self.dy = self.dy + 0.7

    # Método encargado del salto del personaje
    def jump(self, jump_force):
        self.impulse(self.dx, -jump_force)

    # Método encargado de las interacciones del teclado con el personaje (KEY_DOWN)
    def key_down(self, key):
        if key == pygame.K_UP:
            if not self.jumping:
                self.jump(15)
                self.jumping = True
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_LEFT:
            self.set_current_state("walking_left")
            self.dx = -self.speed
        if key == pygame.K_RIGHT:
            self.set_current_state("walking_right")
            self.dx = self.speed
        if key == pygame.K_RCTRL or key == pygame.K_LCTRL:
            self.mode = int(self.mode == 0)
            self.load_image()

    # Método encargado de las interacciones del teclado con el personaje (KEY_UP)
    def key_up(self, key):
        if key == pygame.K_UP:
            pass
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_LEFT:
            if self.dx < 0:
                self.set_current_state("resting_left")
                self.dx = 0
        if key == pygame.K_RIGHT:
            if self.dx > 0:
                self.set_current_state("resting_right")
                self.dx = 0


    # Método que actualiza el estado y Sprite del Character
    def update(self, dt):
        self.calculate_gravity()
        # print(self.rect)
        if self.pos_x + self.dx > 0 and self.pos_x + self.dx < 10240:
            self.pos_x = self.pos_x + self.dx

        if self.pos_x + self.dx > 420:
            pass
        elif self.rect.x + self.dx > 0 and self.rect.x + self.dx < 850:
           self.rect.x = self.rect.x + self.dx

        self.rect.y = self.rect.y + self.dy

        if self.rect.y+self.rect.height > self.display.get_height():
            self.rect.y = self.display.get_height()-self.rect.height
            self.jumping = False
            self.dy = 0

        self.current_state.update(dt)
        self.image = self.current_state.get_sprite()
