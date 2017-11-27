#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Este es el archivo que contiene clases y métodos útiles para el desarrollo del juego
"""

class Path:
    @staticmethod
    def get_path(path,source):
        return '{}{}'.format(path,source)

class Color:
    BLACK = (0,0,0)
    BLUE = (0,0,64)
    WHITE = (255,255,255)
    GRAY = (50,50,50)
    GREEN = (0, 255, 0)
    YELLOW = (247, 177, 33)
    RED = (255,0,0)
