#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports

import unittest

class TestPlatforms(unittest.TestCase):
    def setUp(self):
        # Las siguientes variables simulan los atributos de los objetos necesarios para
        # validar el collide con los obstáculos
        # El formato es objeto_atributo

        self.player_pos_x = 1000
        self.player_image_width = 100
        self.player_dy = 2
        self.player_rect_y = 450
        self.player_image_height = 50

        self.platform_x1 = 1500
        self.platform_x2 = 1800
        self.platform_y = 450

        pass
    def tearDown(self):
        #Despues de la ejecución de nuestro caso de prueba
        pass

    def test_collide_correcto(self):
        result = False
        if self.player_pos_x +  self.player_image_width < self.platform_x1 - 440  or self.player_pos_x > self.platform_x2 - 480:
            result = False
        if not result and self.player_dy >= 0 and self.player_rect_y + self.player_image_height <= self.platform_y and self.player_rect_y + self.player_image_height + 10 >= self.platform_y:
            result = True

        self.assertEqual(result,False, "Operación collide correcto")

    def test_sumar_incorrecto(self):
        result = False
        if self.player_pos_x +  self.player_image_width < self.platform_x1 - 440  or self.player_pos_x > self.platform_x2 - 480:
            result = False
        if not result and self.player_dy >= 0 and self.player_rect_y + self.player_image_height <= self.platform_y and self.player_rect_y + self.player_image_height + 10 >= self.platform_y:
            result = True
        self.assertNotEqual(result,True, "Operación collide incorrecto")
        #Si res == 5 => Caso prueba ok
