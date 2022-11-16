"""
Universidad del valle 
Graficas por computadora
@author Marco Jurado 20308
"""
import pygame
from OpenGL.GL import *

pygame.init()

w,h = 200,200
pantalla = pygame.display.set_mode( (w,h), pygame.OPENGL | pygame.DOUBLEBUF )

def Conway()