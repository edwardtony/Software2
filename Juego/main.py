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
        self.game_over_page = None
        self.dt = pygame.time.Clock().tick(120)
        self.pause = False
        self.transition = False
        self.size = width, height = (960,600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.init()

    def load_service(self):
        content = self.service.get_data()
        highs_score = self.service.get_highs_score()
        # print(content)
        characters = []
        for character in content['characters']:
            characters.append(CharacterDB(character))


        self.game_over_page = GameOverPage(self.screen, self)
        self.initial_page = InitialPage(self.screen, characters, self)
        self.tutorial_page = TutorialPage(self.screen, self)
        self.high_score_page = HighScorePage(self.screen, self, highs_score)
        self.credits_page = CreditsPage(self.screen, self)

        self.first_page = FistPage(self.screen, self)
        self.first_page.initial_page = self.initial_page
        self.first_page.tutorial_page = self.tutorial_page
        self.first_page.high_score_page = self.high_score_page

        self.high_score_page.set_next_page(self.first_page)
        self.credits_page.set_next_page(self.first_page)
        self.tutorial_page.set_next_page(self.first_page)
        self.loading_page = LoadingPage(self.screen,self)
        self.loading_page.set_next_page(self.first_page)

        for index, scenario in enumerate(content['scenarios']):
            scenario_s = ScenarioDB(scenario)
            self.scenarios.append(ScenarioPage(self.screen, scenario_s, self, index))
        self.managePages()
        self.current_page = self.loading_page

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
            # print(self.transition)
            # if self.transition:
            #     pygame.time.wait(1000)
            #     self.transition = False

    def game_over(self):
        if self.current_page.effect:
            self.current_page.effect.stop()
        self.game_over_page.set_next_page(self.initial_page)
        self.current_page = self.game_over_page

    def managePages(self):
        self.initial_page.set_next_page(self.scenarios[0])
        for index, scenario in enumerate(self.scenarios):
            if not index + 1 == len(self.scenarios):
                self.scenarios[index].set_next_page(self.scenarios[index + 1])

    def go_to_next_page(self):
        # self.transition = True
        pygame.draw.rect(self.screen, Color.BLACK,(0,0,self.size[0],self.size[1]), 0)
        if self.current_page.effect:
            self.current_page.effect.stop()
        try:
            self.current_page = self.current_page.next_page
            self.current_page.manage()
        except Exception as e:
            self.current_page = self.credits_page

    def go_to_initial_page(self):
        self.current_page = self.current_page.initial_page
        self.current_page.manage()

    def go_to_tutorial_page(self):
        self.current_page = self.current_page.tutorial_page
        self.current_page.manage()

    def go_to_high_score_page(self):
        self.current_page = self.current_page.high_score_page
        self.current_page.manage()

    def go_to_credits(self):
        self.current_page = self.credits_page
        self.current_page.manage()

# Método principal que ejecuta todo el Hilo
def main():
    manager = CBManager()
    manager.manage()

if __name__ == '__main__':
    main()
