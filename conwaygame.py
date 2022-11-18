"""
Universidad del valle 
Graficas por computadora
@author Marco Jurado 20308
"""
import time
import pygame
from OpenGL.GL import *
import random
import copy

pygame.init()

w,h = 800,600
pantalla = pygame.display.set_mode( (w,h), pygame.OPENGL | pygame.DOUBLEBUF )
red = (1,0,0)
white = (1,1,1)



def pixel(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y,10, 10)
    glClearColor(color[0], color[1], color[2], 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)

#generar patron inicial
coords_patron_inicial = [] #patron inicial
temp = random.randint(0,800)
for i in range(round(h/10)):
    temp_fila = []
    for i in range(round(w/10)):
        temp_fila.append(0)
    coords_patron_inicial.append(temp_fila)

for i in range(1, temp):
    # Generacion de varios numberos random para la posicion de los puntos
    cord_random_x = random.randint(0, 79)
    cord_random_y = random.randint(0, 59)
    coords_patron_inicial[cord_random_y][cord_random_x] = 1

#patron penta decathol
coords_patron_inicial[20][20] = 1
coords_patron_inicial[20][21] = 1
coords_patron_inicial[20][22] = 1
coords_patron_inicial[21][20] = 1
coords_patron_inicial[21][22] = 1
coords_patron_inicial[22][20] = 1
coords_patron_inicial[22][21] = 1
coords_patron_inicial[22][22] = 1
coords_patron_inicial[23][20] = 1
coords_patron_inicial[23][21] = 1
coords_patron_inicial[23][22] = 1
coords_patron_inicial[24][20] = 1
coords_patron_inicial[24][21] = 1
coords_patron_inicial[24][22] = 1
coords_patron_inicial[25][20] = 1
coords_patron_inicial[25][21] = 1
coords_patron_inicial[25][22] = 1
coords_patron_inicial[26][20] = 1
coords_patron_inicial[26][22] = 1
coords_patron_inicial[27][20] = 1
coords_patron_inicial[27][21] = 1
coords_patron_inicial[27][22] = 1


def Conway(copia_celdas, size):
    for j, row in enumerate(copia_celdas):
        for i, cell in enumerate(row):
            #recorrer todas las copia_celdas para verificar condiciones de juego
            copia_celdas_vivas = 0 # copia_celdas vecinas a la y
            if j > 0  and i > 0 and copia_celdas[j-1][i-1]:
                #si la fila existe
                copia_celdas_vivas += 1
            if j > 0  and copia_celdas[j-1][i]:
                #si la fila existe
                copia_celdas_vivas += 1
            if j > 0  and i< 79 and copia_celdas[j-1][i+1]:
                #si la fila existe
                copia_celdas_vivas += 1
            

            if i > 0 and copia_celdas[j][i-1]:
                #si la fila existe
                copia_celdas_vivas += 1
            if i < 79 and copia_celdas[j][i+1]:
                #si la fila existe
                copia_celdas_vivas += 1



            if j < 59 and i > 0 and copia_celdas[j+1][i-1]:
                #si la fila existe
                copia_celdas_vivas += 1

            if j < 59 and copia_celdas[j+1][i]:
                #si la fila existe
                copia_celdas_vivas += 1
            if j < 59 and i < 79 and copia_celdas[j+1][i+1]:
                #si la fila existe
                copia_celdas_vivas += 1

            # si detecta que copia_celdas en x][y = 1, si detecta que hay menos de dos copia_celdas vivas vecinas se muere la celda

            # si detecta que copia_celdas en x][y = 1, si detecta que hay más de 3 copia_celdas vivas vecinas se muere la celda

            # si detecta que copia_celdas en x][y = 1, si detecta que hay menor o igual a 3 copia_celdas vivas vecinas las copia_celdas muertas en x][y se vuelven = 1, y las revivo

            # si detecta que copia_celdas en x][y = 1, si detecta que hay menor o igual a 2 copia_celdas vivas vecinas las copia_celdas muertas en x][y se vuelven = 1, y las revivo
            if copia_celdas[j][i] == 1:
                if copia_celdas_vivas > 3: 
                    copia_celdas[j][i] = 0

                if copia_celdas_vivas < 2 : 
                    copia_celdas[j][i] = 0
                
            # else final si hay 3 copia_celdas vivas, entonces las celulas muertas se vuelven = 1 en x][y, y las revivo
            else:
                if copia_celdas_vivas == 3:
                    copia_celdas[j][i] = 1
                
            #ahora hay que llamar a pixel para que pinte la celda
            #pintar las copia_celdas que sean igual = 1 en x][y con funcion pixel
            if copia_celdas[j][i] == 1:
                pixel(i * size , j * size,  white)
            

            #devuelvo la recursion tratada
    return copia_celdas 

celdas = coords_patron_inicial
funcionar = True
while funcionar:
    celdas = Conway(copy.deepcopy(celdas), 10)
    time.sleep(0.5)
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            funcionar = False
    