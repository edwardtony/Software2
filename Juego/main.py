#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports
import pygame
import sys
from pygame.locals import *

from source.Utils import *
from source.Entities import *
from source.States import *
from source.CBForm import *
from source.Service import *
from source.Models import *
import random

size = width, height = (960,600)
screen = pygame.display.set_mode(size)
pygame.init()

class InitialPage():

    def __init__(self, screen, dt, characters, manager):
        self.screen = screen
        self.dt = dt
        self.characters = characters
        self.manager = manager
        self.manage()

    def manage(self):
        # Objetos en pantalla
        path_cachimbo = (self.characters['Cachimbo'].photo_normal, self.characters['Cachimbo'].photo_super)
        path_cachimba = (self.characters['Cachimba'].photo_normal, self.characters['Cachimba'].photo_super)
        path_fondo_u_lima = 'assets/img/scenarios/u-de-lima.png'
        drawable_sprites = pygame.sprite.Group()
        self.cachimbo = Character(self.screen,path_cachimbo,3,150,250,1.5)
        self.cachimba = Character(self.screen,path_cachimba,3,150,250,1.5)

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
        self.edit_text = EditText(500,390,320,35,2,'',True,20)
        self.button_cachimbo = Button(500,290,130,35,2,'Cachimbo',True,'Cachimbo')
        self.button_cachimba = Button(670,290,130,35,2,'Cachimba',False,'Cachimba')
        self.button_jugar = Button(600,490,110,35,2,'  Jugar',True)

        # Se crea el RadioButtonManager y se agrega los botones cachimbo y cachimba
        self.button_manager = RadioButtonManager()
        self.button_manager.add_button(self.button_cachimbo)
        self.button_manager.add_button(self.button_cachimba)

        # Se agregan los componentes al formulario
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
        pygame.draw.rect(screen, Color.YELLOW,(0,130,width,75),2)
        self.cachimbo.update(self.dt)
        self.cachimba.update(self.dt)
        if self.button_cachimbo.focus:
            self.cachimbo.draw()
        else:
            self.cachimba.draw()

    def key_update(self, event):
        if event.type == KEYDOWN:
            self.cachimbo.key_down(event.key)
            self.cachimba.key_down(event.key)
            self.edit_text.update(event)
        elif event.type == KEYUP:
            self.cachimbo.key_up(event.key)
            self.cachimba.key_up(event.key)
        elif event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            self.edit_text.collidepoint(mouse_position)
            self.button_cachimbo.collidepoint(mouse_position)
            self.button_cachimba.collidepoint(mouse_position)
            if self.button_jugar.rect.collidepoint(mouse_position):
                if self.edit_text.value != '':
                    self.create_characeter()

    def create_characeter(self):
        character_type = self.button_manager.get_button_focused().args
        character = self.characters[character_type]
        name = self.edit_text.value
        player = {
            'name': name,
            'character': character
        }
        self.manager.player = PlayerDB(player)
        self.manager.current_page = self.manager.scenario1
        self.manager.current_page.manage()


class ScenarioPage():

    def __init__(self, screen, dt, scenario, manager):
        self.screen = screen
        self.dt = dt
        self.scenario = scenario
        self.manager = manager
        background = pygame.image.load(scenario.image).convert()
        self.background = pygame.transform.scale(background, (10240,600))
        self.camera_pos = 0
        self.obstacles = []
        self.generate_obstacles()

    def manage(self):
        # Objetos en pantalla
        # Corregir el nombre de la imagen, no en duro
        path_character = (self.manager.player.character.photo_normal, self.manager.player.character.photo_super)
        self.character = Character(self.screen,path_character,3,150,250)
    def draw(self):
        rect = self.background.get_rect()
        self.screen.blit(self.background, (-self.character.pos_x, 0))
        self.character.update(self.dt)
        self.character.draw()
        for obstacle in self.obstacles:
            screen.blit(obstacle['image'], (obstacle['pos'] -self.character.pos_x,530))

    def key_update(self, event):
        if event.type == KEYDOWN:
            self.character.key_down(event.key)
        elif event.type == KEYUP:
            self.character.key_up(event.key)

    def generate_obstacles(self):
        pos_temp = 200
        path = 'assets/img/obstacles/'
        obstacles_name = ['book.png','phone.png','water.png']
        max = random.randint(3,7)
        for x in range(0,max):
            pos_temp = pos_temp + random.randint(300,1000)
            self.obstacles.append({
                'image': pygame.transform.scale(pygame.image.load(path + obstacles_name[random.randint(0,2)]),(50,50)),
                'pos': pos_temp
            })

class CBManager:

    # INITIAL_PAGE = 'initial_page'
    # SCENARIO_1 = 'scenario1'
    # SCENARIO_2 = 'scenario2'
    # SCENARIO_3 = 'scenario3'
    # SCENARIO_4 = 'scenario4'
    # SCENARIO_5 = 'scenario5'

    def __init__(self):
        self.service = DataService()
        self.player = None
        self.initial_page = None
        self.scenario1 = None
        self.scenario2 = None
        self.scenario3 = None
        self.scenario4 = None
        self.scenario5 = None
        self.current_page = None

    def manage(self):
        content = self.service.get_data()
        characters = {}
        scenarios = []
        for character in content['characters']:
            characters[character['name']] = CharacterDB(character)

        for scenario in content['scenarios']:
            scenarios.append(ScenarioDB(scenario))

        dt = pygame.time.Clock().tick(120)
        self.initial_page = InitialPage(screen, dt, characters, self)
        self.scenario1 = ScenarioPage(screen, dt, scenarios[0], self)
        self.scenario2 = ScenarioPage(screen, dt, scenarios[1], self)
        self.scenario3 = ScenarioPage(screen, dt, scenarios[2], self)
        self.scenario4 = ScenarioPage(screen, dt, scenarios[3], self)
        self.scenario5 = ScenarioPage(screen, dt, scenarios[4], self)
        self.current_page = self.initial_page

        i = 0
        # bg = pygame.image.load('assets/img/scenarios/scenario1.png').convert()
        # bg = pygame.transform.scale(bg, (10240, 600))
        while True:
            # if self.state == self.INITIAL_PAGE:
            #     self.initial_page.draw()
            # elif self.state == self.SCENARIO_1:
            #     self.scenario1.draw()
            # elif self.state == self.SCENARIO_2:
            #     self.scenario2.draw()
            # elif self.state == self.SCENARIO_3:
            #     self.scenario3.draw()
            # elif self.state == self.SCENARIO_4:
            #     self.scenario4.draw()
            # else:
            #     self.scenario5.draw()
            self.current_page.draw()

            for event in pygame.event.get():
                # Agregar KEY LONG PRESSED
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                else:
                    self.current_page.key_update(event)


            # Se pinta el formulario




            # for sprite in drawable_sprites.sprites():
            #     sprite.draw()

            # i = i - 3
            # print(i)
            # screen.blit(bg,(i,0))

            pygame.display.flip()


# Método principal que ejecuta todo el Hilo
def main():
    manager = CBManager()
    manager.manage()

if __name__ == '__main__':
    main()
