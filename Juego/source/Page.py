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
        title = Title(321,160,'Seleccionar Personaje',Color.YELLOW,'H1',2)
        # prettytitle = PrettyTitle(321,10,'Prueba',[' ','dos','tres'])
        background = Image(0,0,Config.PATH_FONDO_U_LIMA)
        logo = ImageGIF(0,0,Config.PATH_LOGO_CACHIMBO_BROS)

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
        self.form.add_child(logo)
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
        # width = self.screen.get_rect().width
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
                self.go_to_next_page()
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
                self.go_to_next_page()

    def go_to_next_page(self):
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
        self.manager.go_to_next_page()
        # self.manager.current_page = self.manager.scenario1
        # self.manager.current_page.manage()

class ScenarioPage(Page):

    DIFICULTY = {
        'EASY': {
            'cant_obstacles': 15
        },
        'MEDIUM': {
            'cant_obstacles': 20
        },
        'HARD': {
            'cant_obstacles': 25
        }
    }

    SCORE = {
        'book.png': {
            'score': 20
        },
        'contract.png':{
            'score': 100
        },
        'phone.png': {
            'score': - 10
        },
        'water.png': {
            'score': 10
        }
    }

    YEARS = ['2017-1','2017-2','2018-1','2018-2','2019-1']
    MUSIC = ['music.mp3','music.mp3','music.mp3','music.mp3','final_boss.mp3']

    def __init__(self, screen, scenario, manager, index = 0):
        self.screen = screen
        self.scenario = scenario
        self.index = index
        print(self.scenario.teacher.name)
        # print(self.scenario.teacher.course)
        # print(self.scenario.teacher.image)
        self.manager = manager
        background = pygame.image.load(scenario.image).convert()
        self.background = pygame.transform.scale(background, (10240,720))
        self.camera_pos = 0
        self.obstacles = []
        self.platforms = Platforms(manager)
        self.generate_obstacles()
        self.generate_platforms()
        # Play a la música


    def manage(self):
        # Objetos en pantalla
        # Corregir el nombre de la imagen, no en duro
        self.character = Character(self.screen,self.manager.player.character.character,3,50,470)
        self.boss = Boss(self.screen,self.scenario.teacher,3,400,420,1.2)
        self.form = Form(self.screen)
        self.name = Title(10,10,self.manager.player.name,Color.BLACK,'H5')
        self.year = Title(440,10,self.YEARS[self.index],Color.BLACK,'H3')
        self.form.add_child(self.name)
        self.form.add_child(self.year)

        print('MUSICAA')
        print('mp3/' + self.MUSIC[self.index])
        # pygame.mixer.music.load('mp3/' + self.MUSIC[self.index])
        # pygame.mixer.music.play(-1)

    def draw(self):
        if self.character.pos_x >= 9890:
            self.go_to_next_page()
        # print(pygame.time.get_ticks())
        calc = self.character.pos_x - self.screen.get_rect().width / 2
        if calc <= 0:
            calc = 0
        elif calc >= self.background.get_rect().width - self.screen.get_rect().width:
            calc = self.background.get_rect().width - self.screen.get_rect().width

        # screen_pos =  calc if self.character.pos_x  > calc else self.character.pos_x
        self.screen.blit(self.background, (-calc, -120))
        self.character.update(self.boss)
        self.platforms.do(self.character)
        self.collide_obstacles()
        self.character.draw()
        self.form.draw()
        font = pygame.font.SysFont(None, 60)
        title = font.render(str(self.manager.player.score), True, Color.BLACK)
        self.screen.blit(title, (880,10))
        # self.platforms.draw()

        # if self.manager.pause:
        #     s = pygame.Surface((1000, 1000))
        #     s.fill(Color.BLACK)
        #     s.set_colorkey(Color.BLACK)
        #     pygame.draw.rect(s, Color.BLACK,(0,0,self.manager.size[0],self.manager.size[1]), 0)
        #     s.set_alpha(75)
        self.boss.update(self.character)
        self.boss.draw()
        self.draw_hearts()

        # DRAW METHOD
        display = self.manager.screen
        for p in self.platforms.container:
            self.manager.screen.blit(self.image, (p.x1 - self.character.pos_x ,p.y))
            # pygame.draw.line(display, Color.WHITE, (p.x1 -self.character.pos_x , p.y), (p.x2 -self.character.pos_x, p.y),1)

        for obstacle in self.obstacles:
            self.screen.blit(obstacle['image'], (obstacle['pos_x'] -self.character.pos_x,obstacle['pos_y']))

    def key_update(self, event):
        if event.type == KEYDOWN and event.key == pygame.K_p and not self.manager.current_page == self.manager.initial_page:
            self.manager.pause = not self.manager.pause
        if self.manager.pause:
            self.character.pause()
            return
        else:
            self.character.play()
        if event.type == KEYDOWN:
            self.character.key_down(event.key)
            self.boss.key_down(event.key)
        elif event.type == KEYUP:
            self.character.key_up(event.key)

    def draw_hearts(self):
        for i in range(0,self.character.life):
            self.screen.blit(pygame.image.load(Config.PATH_OBJECTS + "hearts.png").convert_alpha(), (10 + i*50,40))

    def generate_obstacles(self):
        # self.obstacles_group = pygame.sprite.Group()
        pos_x = 1500
        path_obstacles = Config.PATH_OBSTACLES
        obstacles_name = ['book.png','phone.png','water.png','contract.png']
        max_limit = 3
        max = self.DIFICULTY[self.scenario.dificulty]['cant_obstacles']
        for x in range(0,max):
            rand = random.randint(0,max_limit)
            if(rand == 3):
                max_limit = 2
            name = obstacles_name[rand]
            pos_x = pos_x + random.randint(500,550)
            pos_y = random.randint(400, 500)
            obstacle_image = pygame.transform.scale(pygame.image.load(path_obstacles + name).convert_alpha(),(50,50))
            self.obstacles.append({
                'image': obstacle_image,
                'pos_x': pos_x,
                'pos_y': pos_y,
                'name': name
            })
            # self.obstacles_group.add(obstacle_image)

    def collide_obstacles(self):
        for index, obstacle in enumerate(self.obstacles):
            if(self.character.rect.y <= obstacle['pos_y'] and self.character.rect.y >= obstacle['pos_y'] - 110 and self.character.pos_x  + 500 >= obstacle['pos_x'] and self.character.pos_x + 500 <= obstacle['pos_x'] + 110):
                self.updateScore(self.SCORE[obstacle['name']]['score'])
                self.obstacles.pop(index)

            # print(self.character.pos_x)
            # print(self.character.rect.y)
            # print(obstacle['pos'])
            # print(pygame.sprite.spritecollide(self.image.get_rect(), obstacle['image'].get_rect(), True))
            # if(self.image.get_rect().colliderect(obstacle['image'].get_rect())):
                # print(obstacle['name'])

    def updateScore(self, score):
        new_score = self.manager.player.score + score
        if new_score >= 0:
            self.manager.player.score = new_score
        else:
            self.manager.player.score = 0

    def generate_platforms(self):
        self.image = pygame.image.load(Config.PATH_OBSTACLES + "obstacle.png").convert_alpha()
        for i in range(0, 20):
            self.platforms.add(Platform(1500 + i*400, random.randint(300,500), 200))

    def go_to_next_page(self):
        self.manager.go_to_next_page()

class Platform:
    def __init__(self,x,y,width):
        self.x1 = x
        self.y = y
        self.x2 = x + width

    def test(self,player):
        if player.pos_x  + player.image.get_rect().width < self.x1 - 440 or player.pos_x > self.x2 - 480: return None
        if player.dy >= 0 and player.rect.y + player.image.get_rect().height <= self.y and player.rect.y + player.image.get_rect().height + 10 >= self.y: return self
        return None

class Platforms:
    def __init__(self, manager):
        self.container = []
        self.manager = manager

    def add(self,p):
        self.container.append(p)

    def testCollision(self,player):
        if not player.jumping: return False
        for p in self.container:
            result = p.test(player)
            if result:
                player.current_platform = result
                player.y = result.y
                player.jumping = False
                return True
        return False

    def draw(self):
        display = self.manager.screen
        # image = pygame.image.load(Config.PATH_OBSTACLES + "obstacle.png")
        # self.display.blit(image, (self.rect.x, self.rect.y))
        for p in self.container:
            pass
            # print("p",p.x1,p.y)
            # self.manager.screen.blit(image, (500, 200))
            # self.display.blit(image, (self.rect.x, self.rect.y))
            # pygame.draw.line(display, Color.WHITE, (p.x1, p.y), (p.x2, p.y),1)

    def do(self, player):
        self.testCollision(player)
        self.draw()
