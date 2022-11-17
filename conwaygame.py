"""
Universidad del valle 
Graficas por computadora
@author Marco Jurado 20308
"""
import math
import time
import pygame
from OpenGL.GL import *
import random
import numpy

pygame.init()

w,h = 800,600
pantalla = pygame.display.set_mode( (w,h), pygame.OPENGL | pygame.DOUBLEBUF )
red = (1,0,0)
white = (1,1,1)



def pixel(x, y, color):
    print('holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa a   >   ',color)
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, 9, 9)
    glClearColor(color[0], color[1], color[2], 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)

#generar patron inicial
coords_patron_inicial = [] #patron inicial
temp = random.randint(50,100)
print('TEMP > ',temp)
for i in range(0, temp):
    # Generacion de varios numberos random para la posicion de los puntos
    cord_random_x = random.randint(200, 250)
    cord_random_y = random.randint(200, 250)
    coords_patron_inicial.append( [cord_random_x, cord_random_y] )


def Conway(celdas, size, updater_celdas):
    celdas_muertas = numpy.zeros((celdas.shape[0], celdas.shape[1])) #indice de cada celda (x,y)
    color = (1,0,0)

    for x,y in numpy.ndindex(celdas.shape[0], celdas.shape[1]):
        #recorrer todas las celdas para verificar condiciones de juego
        celdas_vivas = numpy.sum( celdas[ x-1:x+2, y-1:y+2 ] ) - celdas[x,y] # slices de python para obtener celdas vivas (valor de x,y)

        # condiciones
        # si detecta que celdas en x,y son = 0 la celda se apaga  ---> o se pintan
        if celdas[x,y] == 0: color = red
        if celdas[x,y == 1]: color = white

        # si detecta que celdas en x,y = 1, si detecta que hay menos de dos celdas vivas vecinas se muere la celda

        # si detecta que celdas en x,y = 1, si detecta que hay más de 3 celdas vivas vecinas se muere la celda

        # si detecta que celdas en x,y = 1, si detecta que hay menor o igual a 3 celdas vivas vecinas las celdas muertas en x,y se vuelven = 1, y las revivo

        # si detecta que celdas en x,y = 1, si detecta que hay menor o igual a 2 celdas vivas vecinas las celdas muertas en x,y se vuelven = 1, y las revivo
        if celdas[x,y] == 1:
            if celdas_vivas > 3 and updater_celdas == True: color = red
            if celdas_vivas < 2 and updater_celdas == True: color = red
            if celdas_vivas <= 3:
                celdas_muertas[x,y] = 1
                if updater_celdas == True: color = white
            if celdas_vivas >= 2:
                celdas_muertas[x,y] = 1
                if updater_celdas == True: color = white
            
        # else final si hay 3 celdas vivas, entonces las celulas muertas se vuelven = 1 en x,y, y las revivo
        else:
            if celdas_vivas == 3:
                celdas_muertas[x,y] = 1
                if updater_celdas == True: color = white
            
        #ahora hay que llamar a pixel para que pinte la celda
        #pintar las celdas que sean igual = 1 en x,y con funcion pixel
        pixel(x * size , y * size,  color)

        #devuelvo la recursion tratada
        print('celdas > ', celdas_muertas)
        return celdas_muertas 

#recorrer coordenadas para generar el patron inicial
#para generar celdas
temp_w = w
temp_h = h
ceros_boundbox = (round(temp_w),round(temp_h))
celdas = numpy.zeros(ceros_boundbox) #llena mapa de ceros
print('celda> > ', celdas.size)
Conway(celdas, 10, False)
pygame.display.flip()
for i in coords_patron_inicial:
    i[0] #primer valor de celdas en x
    i[1] #segundo valor de celdas en y
    celdas[  round(i[0]), round(i[1])  ] = 1
    print(' la nueva zelda > ',celdas[  round(i[0]), round(i[1])  ])
    Conway(celdas, 10, False)

funcionar = True
while funcionar:
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            funcionar = False
        else:
            temp_updater = True
            Conway(celdas, 10, False)
            
        if temp_updater == True:
            celdas = Conway(celdas, 10 , True)
            pygame.display.flip()
            time.sleep(0.2)