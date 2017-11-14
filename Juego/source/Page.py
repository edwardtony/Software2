#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports

import pygame
from source.Models import *
from source.Entities import *
from source.libs.CBForm import *
from source.Utils import *
from source.Config import *
import random

class Page:

    def set_next_page(self,page):
        self.next_page = page

    def manage(self):
        pass

    def draw(self):
        pass

    def key_update(self):
        pass

class InitialPage(Page):

    def __init__(self, screen, characters, manager):
        self.screen = screen
        self.manager = manager
        self.characters = self.loadCharacter(characters)
        self.manage()
        self.character_buttons = []

    def loadCharacter(self, characters):
        characters_arr = []
        for character in characters:
            characters_arr.append(Character(self.screen,character,3,150,250,1.5))
        return characters_arr

    def manage(self):
        # Objetos en pantalla

        # path_cachimbo = (self.characters['Cachimbo'].photo_normal, self.characters['Cachimbo'].photo_super)
        # path_cachimba = (self.characters['Cachimba'].photo_normal, self.characters['Cachimba'].photo_super)
        path_fondo_u_lima = Config.PATH_FONDO_U_LIMA
        drawable_sprites = pygame.sprite.Group()
        # self.cachimbo = Character(self.screen,path_cachimbo,3,150,250,1.5)
        # self.cachimba = Character(self.screen,path_cachimba,3,150,250,1.5)

        # Se crea el formulario
        self.form = Form(self.screen)

        # Se crean título, fondo y labels
        title = Title(321,140,'Seleccionar Personaje')
        prettytitle = PrettyTitle(321,10,'Prueba',[' ','dos','tres'])
        background = Image(0,0,path_fondo_u_lima)

        label1 = Label(500,250,'Elije a tu personaje favorito')
        label2 = Label(500,350,'Nombre')
        label3 = Label(5,580,'Presionar "ctrl" para transformar',20)

        # Se crean los componentes del formulario
        self.edit_text = EditText(500,390,320,35,2,'Anthony',True,20)

        # for character in characters:
        #     self.character_buttons.append(Button(500,290,130,35,2,'Cachimbo',True,'Cachimbo'))
        self.button_cachimbo = Button(500,290,130,35,2,'Cachimbo',True,0)
        self.button_cachimba = Button(670,290,130,35,2,'Cachimba',False,1)
        self.button_jugar = Button(600,490,110,35,2,'  Jugar',True)

        # Se crea el RadioButtonManager y se agrega los botones cachimbo y cachimba
        self.button_manager = RadioButtonManager()
        self.button_manager.add_button(self.button_cachimbo)
        self.button_manager.add_button(self.button_cachimba)

        # Se agregan los componentes al formulario
        # OJO: Primero siempre va el background, sino tapará a los demás components
        self.form.add_child(background)
        self.form.add_child(title)

        # self.form.add_child(prettytitle)
        self.form.add_child(label1)
        self.form.add_child(label2)
        self.form.add_child(label3)
        self.form.add_child(self.edit_text) # Se podría poner una etiqueta para saber a quien borrar
        self.form.add_child(self.button_jugar)
        self.form.add_child(self.button_manager)

    def draw(self):
        self.form.draw()
        width = self.screen.get_rect().width
        pygame.draw.rect(self.screen, Color.YELLOW,(0,130,width,75),2)
        [character.update(self.manager.dt) for character in self.characters]

        # self.cachimbo.update(self.manager.dt)
        # self.cachimba.update(self.manager.dt)
        if self.button_cachimbo.focus:
            self.characters[0].draw()
        else:
            self.characters[1].draw()

    def key_update(self, event):
        if event.type == KEYDOWN and event.key == pygame.K_p and not self.manager.current_page == self.manager.initial_page:
            self.manager.pause = not self.manager.pause
        if self.manager.pause:
            return
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.create_characeter()
                return
            [character.key_update(event) for character in self.characters]
            # self.cachimbo.key_down(event.key)
            # self.cachimba.key_down(event.key)
            self.edit_text.update(event)
        elif event.type == KEYUP:
            [character.key_update(event) for character in self.characters]
            # self.cachimbo.key_up(event.key)
            # self.cachimba.key_up(event.key)
        elif event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            self.edit_text.collidepoint(mouse_position)
            self.button_cachimbo.collidepoint(mouse_position)
            self.button_cachimba.collidepoint(mouse_position)
            if self.button_jugar.rect.collidepoint(mouse_position):
                self.create_characeter()

    def create_characeter(self):
        if self.edit_text.is_empty():
            self.edit_text.empty_alert()
            return
        character_type = self.button_manager.get_button_focused().args
        character = self.characters[character_type]
        name = self.edit_text.value
        player = {
            'name': name,
            'character': character
        }
        self.manager.player = PlayerDB(player)
        self.manager.nextPage()
        # self.manager.current_page = self.manager.scenario1
        # self.manager.current_page.manage()


class ScenarioPage(Page):

    DIFICULTY = {
        'EASY': {
            'cant_obstacles': 10
        },
        'MEDIUM': {
            'cant_obstacles': 15
        },
        'HARD': {
            'cant_obstacles': 20
        }
    }

    def __init__(self, screen, scenario, manager):
        self.screen = screen
        self.scenario = scenario
        print(self.scenario.teacher.name)
        print(self.scenario.teacher.course)
        print(self.scenario.teacher.image)
        self.manager = manager
        background = pygame.image.load(scenario.image).convert()
        self.background = pygame.transform.scale(background, (10240,720))
        self.camera_pos = 0
        self.obstacles = []
        self.generate_obstacles()

    def manage(self):
        # Objetos en pantalla
        # Corregir el nombre de la imagen, no en duro
        self.character = Character(self.screen,self.manager.player.character.character,3,50,470)
        self.boss = Boss(self.screen,self.scenario.teacher,3,400,470,1.2)

    def draw(self):
        calc = self.character.pos_x - self.screen.get_rect().width / 2
        if calc <= 0:
            calc = 0
        elif calc >= self.background.get_rect().width - self.screen.get_rect().width:
            calc = self.background.get_rect().width - self.screen.get_rect().width

        # screen_pos =  calc if self.character.pos_x  > calc else self.character.pos_x
        self.screen.blit(self.background, (-calc, -120))
        self.character.update(self.manager.dt)
        self.character.draw()
        # self.boss.update(self.manager.dt)
        # self.boss.draw()


        for obstacle in self.obstacles:
            self.screen.blit(obstacle['image'], (obstacle['pos'] -self.character.pos_x,530))

    def key_update(self, event):
        if event.type == KEYDOWN:
            self.character.key_down(event.key)
        elif event.type == KEYUP:
            self.character.key_up(event.key)

    def generate_obstacles(self):
        pos_temp = 1500
        path_obstacles = Config.PATH_OBSTACLES
        obstacles_name = ['book.png','phone.png','water.png']
        max = self.DIFICULTY[self.scenario.dificulty]['cant_obstacles']
        for x in range(0,max):
            pos_temp = pos_temp + random.randint(100,1000)
            self.obstacles.append({
                'image': pygame.transform.scale(pygame.image.load(path_obstacles + obstacles_name[random.randint(0,2)]),(50,50)),
                'pos': pos_temp
            })

class Platform:
    def __init__(self,x,y,width):
        self.x1 = x
        self.y = y
        self.x2 = x + width

    def test(self,player):
        if player.x < self.x1 or player.x > self.x2: return None
        # if player. <= self.y and player.y + player.velocity >= self.y: return self
        return None

class Platforms:
    def __init__(self):
        self.container = []

    def add(self,p):
        self.container.append(p)

    def testCollision(self,player):
        if not player.falling: return False
        for p in self.container:
            result = p.test(player)
            if result:
                player.current_platform = result
                player.y = result.y
                player.jumping = False
                return True
        return False

    def draw(self):
        display = pygame.display.get_surface()
        for p in self.container:
            pygame.draw.line(display, Color.WHITE, (p.x1, p.y), (p.x2, p.y),1)

    def do(self, player):
        self.testCollision(player)
        self.draw()
