#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from States import AnimatedState, StaticState
from pygame.locals import *
from libs.CBForm import *
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
    def __init__(self, display, character, number_of_sprites, px, py, scale = 1, mode = 0):
        super(Character, self).__init__(display)
        # self.speed = character.velocity * 7
        self.speed = 80
        self.character = character
        self.paths = (character.photo_normal, character.photo_super, character.photo_ultra)
        self.number_of_sprites = number_of_sprites
        self.mode = mode
        self.load_image()
        self.image = self.current_state.get_sprite()
        self.rect = self.scale(scale)
        self.pos_x = px
        self.rect.x = px
        self.rect.y = py
        self.current_platform = None
        self.jumping = False
        self.base = 50
        self.alt = 1

    # Permite dimensionar la imagen escalándola de tamaño
    def scale(self,scale):
        return pygame.Rect(0,0,self.image.get_rect().width*scale,self.image.get_rect().height*scale)

    # Carga la imagen del personaje, los animados, los estáticos y el estado actual
    def load_image(self):
        path = self.paths[self.mode]
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
            self.dy = self.alt
        else:
            self.dy = self.dy + self.alt

    # Pausar al personaje
    def pause(self):
        self.dx = 0
        self.dy = 0
        self.alt = 0

    # Play al personaje
    def play(self):
        self.alt = 1

    # Método encargado del salto del personaje
    def jump(self, jump_force):
        effect = pygame.mixer.Sound('mp3/jump.wav')
        effect.play()
        self.impulse(self.dx, - jump_force)

    # Método encargado de las interacciones del teclado con el personaje (KEY_DOWN)
    def key_down(self, key):
        if key == pygame.K_UP:
            if not self.jumping:
                self.jump(15)
                self.jumping = True
        elif key == pygame.K_DOWN:
            pass
        elif key == pygame.K_LEFT:
            self.set_current_state("walking_left")
            self.dx = -self.speed
        elif key == pygame.K_RIGHT:
            self.set_current_state("walking_right")
            self.dx = self.speed
        elif key == pygame.K_RCTRL or key == pygame.K_LCTRL:
            self.mode = int(self.mode == 0)
            self.load_image()
            if(self.mode):
                pygame.mixer.music.load('mp3/practicante.ogg')
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()

    # Método encargado de las interacciones del teclado con el personaje (KEY_UP)
    def key_up(self, key):
        if key == pygame.K_UP:
            pass
        elif key == pygame.K_DOWN:
            pass
        elif key == pygame.K_LEFT:
            if self.dx < 0:
                self.set_current_state("resting_left")
                self.dx = 0
        elif key == pygame.K_RIGHT:
            if self.dx > 0:
                self.set_current_state("resting_right")
                self.dx = 0

    def key_update(self, event):
        if event.type == KEYDOWN:
            self.key_down(event.key)
        elif event.type == KEYUP:
            self.key_up(event.key)

    # Método que actualiza el estado y Sprite del Character
    def update(self, boss):
        if self.pos_x > 9330 and boss.status == Boss.STATUS_INITIAL:
            self.dx = 0
            boss.in_class = True
            return
        self.calculate_gravity()
        # print('platform',self.current_platform)
        if self.current_platform:
            if not self.current_platform.test(self):
                # self.jumping = False
                self.current_platform = None
        else:
            self.rect.y = self.rect.y + self.dy
            if self.rect.y+self.rect.height > self.display.get_height() - self.base:
                self.rect.y = self.display.get_height()-self.rect.height - self.base
                self.jumping = False
                self.dy = 0
        # print(self.rect)
        # print(self.display.get_width())
        if self.pos_x + self.dx > 0 and self.pos_x + self.dx < 9900:
            self.pos_x = self.pos_x + self.dx

        if self.pos_x > 9900 - 480 and self.rect.x + self.dx < 900:
            self.rect.x = self.rect.x + self.dx
        elif self.pos_x < 480 and self.rect.x + self.dx < 480:
            self.rect.x = self.rect.x + self.dx

        if self.rect.x <= 0:
            self.rect.x = 0
        # elif self.rect.x >= 850:
        #     self.rect.x = 850
        # elif self.rect.x + self.dx > 0 and self.rect.x + self.dx < 470:
        #     self.rect.x = self.rect.x + self.dx



        self.current_state.update(1)
        self.image = self.current_state.get_sprite()


class Boss(GameEntity):

    """
        Clase encargada de gestionar la configuración y acciones de un boss,
        Extiende de GameEntity
    """

    STATUS_INITIAL = "INITIAL"
    STATUS_DEFEATED = "DEFEATED"

    # Constructor
    def __init__(self, display, boss, number_of_sprites, px, py, scale = 1):
        super(Boss, self).__init__(display)
        self.speed = 10
        self.boss = boss
        self.number_of_sprites = number_of_sprites
        self.load_image()
        self.image = self.current_state.get_sprite()
        self.rect = self.scale(scale)
        self.rect.x = px
        self.rect.y = py
        self.rect.x = 5500
        self.status = Boss.STATUS_INITIAL
        self.in_class = False
        self.message = Message(self.display, "HOLA")

    # Permite dimensionar la imagen escalándola de tamaño
    def scale(self,scale):
        return pygame.Rect(0,0,self.image.get_rect().width*scale,self.image.get_rect().height*scale)

    # Carga la imagen del personaje, los animados, los estáticos y el estado actual
    def load_image(self):
        path = self.boss.image
        self.walking_images = pygame.image.load(path)

        self.walking_left_state = AnimatedState(self.walking_images.subsurface(0,0,
                                                self.walking_images.get_width(),
                                                self.walking_images.get_height()),
                                                self.number_of_sprites, 150, "walking_left")

        self.resting_left_state = StaticState(self.walking_images.subsurface(0,0,
                                              self.walking_images.get_width()/self.number_of_sprites,
                                              self.walking_images.get_height()),
                                               "resting_left")

        self.states_dict["walking_left"] = self.walking_left_state
        self.states_dict["resting_left"] = self.resting_left_state
        self.set_current_state("resting_left")

    # Método que actualiza el estado y Sprite del Character
    def update(self, character):
        if self.in_class:
            self.show_message()
            return
        self.image = self.current_state.get_sprite()
        self.rect.x = self.rect.x - character.dx / 2

    def show_message(self):
        self.message.update()

    # def update(self, dt):
    #     if self.pos_x + self.dx > 0 and self.pos_x + self.dx < 9900:
    #         self.pos_x = self.pos_x + self.dx
    #
    #     if self.pos_x > 9900 - 480 and self.rect.x + self.dx < 900:
    #         self.rect.x = self.rect.x + self.dx
    #     elif self.pos_x < 480 and self.rect.x + self.dx < 480:
    #         self.rect.x = self.rect.x + self.dx
    #
    #     if self.rect.x <= 0:
    #         self.rect.x = 0
    #     # elif self.rect.x >= 850:
    #     #     self.rect.x = 850
    #     # elif self.rect.x + self.dx > 0 and self.rect.x + self.dx < 470:
    #     #     self.rect.x = self.rect.x + self.dx

class Message(GameEntity):

    def __init__(self,display, message):
        super(Message, self).__init__(display)
        self.path = "assets/img/objects/globo_dialogo.png"
        self.image = pygame.image.load(self.path)
        self.form = Form(display)
        self.dialog_manager = DialogManager()
        self.dialog_manager.add_dialog(Dialog(200,100,'Hola, soy el profesor Riccio y hoy conoceras el poder de las BDs '))
        self.dialog_manager.add_dialog(Dialog(200,140,'Me conocen como el padre de Oracle!!! '))
        self.dialog_manager.add_dialog(Dialog(200,180,'Pregunta1: Que es una base de datos? '))
        self.dialog_manager.add_dialog(Dialog(200,220,'    a) cualquier cosa '))
        self.dialog_manager.add_dialog(Dialog(200,260,'    b) cualquier cosa '))
        self.dialog_manager.add_dialog(Dialog(200,300,'    c) cualquier cosa '))
        self.dialog_manager.add_dialog(Dialog(200,340,'(Presionar la tecla que corresponda a tu respuesta) '))
        self.form.add_child(self.dialog_manager)
    def update(self):
        self.display.blit(self.image, (150,50))
        self.form.draw()
