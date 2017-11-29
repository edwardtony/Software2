#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports

import unittest

class TestInitialPage(unittest.TestCase):
    def setUp(self):
        # Las siguientes variables simulan los atributos de los objetos necesarios para
        # actuar frente a los diferentes inputs del teclado
        # El formato es objeto_atributo

        self.event1_type = 'key_down'
        self.event1_key = 'k_return'
        self.mouse_position1 = 10

        self.event2_type = 'key_down'
        self.event2_key = 'anything'
        self.mouse_position2 = 10

        self.event3_type = 'key_up'
        self.event3_key = 'anything'
        self.mouse_position3 = 10

        self.event4_type = 'mousebuttondown'
        self.event4_key = 'anything'
        self.mouse_position4 = 10

        self.event5_type = 'mousebuttondown'
        self.event5_key = 'anything'
        self.mouse_position5 = 15


        pass
    def tearDown(self):
        #Despues de la ejecución de nuestro caso de prueba
        pass

    def test_key_update_result_next_page(self):
        result = None
        if self.event1_type == 'key_down':
            result = 'key_down'
            if self.event1_key == 'k_return':
                result = 'next_page'
                # .
                # .
                # .
                # más lógica, no influye en el test
        elif self.event1_type == 'key_up':
            result = 'key_up'
            # .
            # .
            # .
            # más lógica, no influye en el test
        elif self.event1_type == 'mousebuttondown':
            result = 'mousebuttondown'
            # .
            # .
            # .
            # más lógica, no influye en el test
            if self.mouse_position1 > 10 or self.mouse_position1 < 20:
                result = 'collidepoint'
        self.assertEqual(result,'next_page', "Ir a la siguiente página")


    def test_key_update_result_key_down(self):
        result = None
        if self.event2_type == 'key_down':
            if self.event2_key == 'k_return':
                result = 'next_page'
                # .
                # .
                # .
                # más lógica, no influye en el test
            result = 'key_down'
        elif self.event2_type == 'key_up':
            result = 'key_up'
            # .
            # .
            # .
            # más lógica, no influye en el test
        elif self.event2_type == 'mousebuttondown':
            result = 'mousebuttondown'
            # .
            # .
            # .
            # más lógica, no influye en el test
            if self.mouse_position2 > 10 or self.mouse_position2 < 20:
                result = 'collidepoint'
        self.assertEqual(result,'key_down', "Handle de Key Down")


    def test_key_update_result_key_up(self):
        result = None
        if self.event3_type == 'key_down':
            if self.event3_key == 'k_return':
                result = 'next_page'
                # .
                # .
                # .
                # más lógica, no influye en el test
            result = 'key_down'
        elif self.event3_type == 'key_up':
            result = 'key_up'
            # .
            # .
            # .
            # más lógica, no influye en el test
        elif self.event3_type == 'mousebuttondown':
            result = 'mousebuttondown'
            # .
            # .
            # .
            # más lógica, no influye en el test
            if self.mouse_position3 > 10 or self.mouse_position3 < 20:
                result = 'collidepoint'
        self.assertEqual(result,'key_up', "Handle de Key Up")


    def test_key_update_result_mousebuttondown(self):
        result = None
        if self.event4_type == 'key_down':
            if self.event4_key == 'k_return':
                result = 'next_page'
                # .
                # .
                # .
                # más lógica, no influye en el test
            result = 'key_down'
        elif self.event4_type == 'key_up':
            result = 'key_up'
            # .
            # .
            # .
            # más lógica, no influye en el test
        elif self.event4_type == 'mousebuttondown':
            result = 'mousebuttondown'
            # .
            # .
            # .
            # más lógica, no influye en el test
            if self.mouse_position4 > 10 and self.mouse_position4 < 20:
                result = 'collidepoint'
        self.assertEqual(result,'mousebuttondown', "Handle de MouseButtonDown")


    def test_key_update_result_collidepoint(self):
        result = None
        if self.event5_type == 'key_down':
            if self.event5_key == 'k_return':
                result = 'next_page'
                # .
                # .
                # .
                # más lógica, no influye en el test
            result = 'key_down'
        elif self.event5_type == 'key_up':
            result = 'key_up'
            # .
            # .
            # .
            # más lógica, no influye en el test
        elif self.event5_type == 'mousebuttondown':
            result = 'mousebuttondown'
            # .
            # .
            # .
            # más lógica, no influye en el test
            if self.mouse_position5 > 10 and self.mouse_position5 < 20:
                result = 'collidepoint'
        self.assertEqual(result,'collidepoint', "Handle de CollidePoint")
