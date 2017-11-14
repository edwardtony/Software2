#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports
import pygame
import sys
from pygame.locals import *

from source.Utils import *
from source.Entities import *
from source.States import *
from source.Service import *
from source.Models import *
from source.Page import *

size = width, height = (960,600)
screen = pygame.display.set_mode(size)
pygame.init()

# class Config:
#     def __init__(self):
#

class CBManager:

    def __init__(self):
        self.service = DataService()
        self.player = None
        self.initial_page = None
        self.scenarios = []
        self.current_page = None
        self.dt = pygame.time.Clock().tick(60)
        self.pause = False

    def load_service(self):
        content = self.service.get_data()
        # print(content)
        characters = []
        for character in content['characters']:
            characters.append(CharacterDB(character))

        self.initial_page = InitialPage(screen, characters, self)

        for scenario in content['scenarios']:
            scenario_s = ScenarioDB(scenario)
            self.scenarios.append(ScenarioPage(screen, scenario_s, self))
        self.managePages()
        self.current_page = self.initial_page

    def manage(self):
        self.load_service()

        while True:

            self.current_page.draw()

            for event in pygame.event.get():
                # Agregar KEY LONG PRESSED
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                else:
                    self.current_page.key_update(event)
            pygame.display.flip()

    def managePages(self):
        self.initial_page.set_next_page(self.scenarios[0])
        for index, scenario in enumerate(self.scenarios):
            if not index + 1 == len(self.scenarios):
                self.scenarios[index].set_next_page(self.scenarios[index + 1])

    def nextPage(self):
        self.current_page.next_page.manage()
        self.current_page = self.current_page.next_page

# Método principal que ejecuta todo el Hilo
def main():
    manager = CBManager()
    manager.manage()

if __name__ == '__main__':
    main()
