#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports

import unittest

class TestScenarioPage(unittest.TestCase):
    def setUp(self):
        # Las siguientes variables simulan los atributos de los objetos necesarios para
        # validar que se objetos se va a pintar o que rutas alternativas se tomará
        # El formato es objeto_atributo

        self.manager_player_lifes1 = 1
        self.character_pos_x1 = 1000
        self.calc1 = -10

        self.manager_player_lifes2 = -1
        self.character_pos_x2 = 1000
        self.calc2 = -10

        self.manager_player_lifes3 = -1
        self.character_pos_x3 = 1000
        self.calc3 = 10

        self.manager_player_lifes4 = -1
        self.character_pos_x4 = 10000
        self.calc4 = -10

        self.manager_player_lifes5 = -1
        self.character_pos_x5 = 10000
        self.calc5 = 10

    def tearDown(self):
        #Despues de la ejecución de nuestro caso de prueba
        pass


    def test_collide_uno(self):
        result = []
        if self.manager_player_lifes1 <= 0:
            result.append('lifes_menor_igual_cero')
        if self.character_pos_x1 >= 9850:
            result.append('pos_x_mayor_igual_9850')

        # .
        # .
        # .
        # más lógica, no influye en el test

        if self.calc1 <= 0:
            result.append('calc_menor_igual_cero')
        elif self.calc1 > 0:
            result.append('calc_mayor_cero')

        # .
        # .
        # .
        # más lógica, no influye en el test

        self.assertEqual(result,['calc_menor_igual_cero'], "Se coincide con cero condiciones")


    def test_collide_dos_caso_a(self):
        result = []
        if self.manager_player_lifes2 <= 0:
            result.append('lifes_menor_igual_cero')
        if self.character_pos_x2 >= 9850:
            result.append('pos_x_mayor_igual_9850')

        # .
        # .
        # .
        # más lógica, no influye en el test

        if self.calc2 <= 0:
            result.append('calc_menor_igual_cero')
        elif self.calc2 > 0:
            result.append('calc_mayor_cero')

        # .
        # .
        # .
        # más lógica, no influye en el test

        self.assertEqual(result,['lifes_menor_igual_cero','calc_menor_igual_cero'], "Se coincide con dos condiciones")


    def test_collide_dos_caso_b(self):
        result = []
        if self.manager_player_lifes3 <= 0:
            result.append('lifes_menor_igual_cero')
        if self.character_pos_x3 >= 9850:
            result.append('pos_x_mayor_igual_9850')

        # .
        # .
        # .
        # más lógica, no influye en el test

        if self.calc3 <= 0:
            result.append('calc_menor_igual_cero')
        elif self.calc3 > 0:
            result.append('calc_mayor_cero')

        # .
        # .
        # .
        # más lógica, no influye en el test

        self.assertEqual(result,['lifes_menor_igual_cero','calc_mayor_cero'], "Se coincide con dos condiciones")


    def test_collide_tres_caso_a(self):
        result = []
        if self.manager_player_lifes4 <= 0:
            result.append('lifes_menor_igual_cero')
        if self.character_pos_x4 >= 9850:
            result.append('pos_x_mayor_igual_9850')

        # .
        # .
        # .
        # más lógica, no influye en el test

        if self.calc4 <= 0:
            result.append('calc_menor_igual_cero')
        elif self.calc4 > 0:
            result.append('calc_mayor_cero')

        # .
        # .
        # .
        # más lógica, no influye en el test

        self.assertEqual(result,['lifes_menor_igual_cero','pos_x_mayor_igual_9850','calc_menor_igual_cero'], "Se coincide con dos condiciones")


    def test_collide_tres_caso_b(self):
        result = []
        if self.manager_player_lifes5 <= 0:
            result.append('lifes_menor_igual_cero')
        if self.character_pos_x5 >= 9850:
            result.append('pos_x_mayor_igual_9850')

        # .
        # .
        # .
        # más lógica, no influye en el test

        if self.calc5 <= 0:
            result.append('calc_menor_igual_cero')
        elif self.calc5 > 0:
            result.append('calc_mayor_cero')

        # .
        # .
        # .
        # más lógica, no influye en el test

        self.assertEqual(result,['lifes_menor_igual_cero','pos_x_mayor_igual_9850','calc_mayor_cero'], "Se coincide con dos condiciones")
