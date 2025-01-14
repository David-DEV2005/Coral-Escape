import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#Criação de Variavéis e Funções. 

tamanho_da_Tela= (500, 700)
tela= pygame.display.set_mode(tamanho_da_Tela)
pygame.display.set_caption("Coral Escape")
x = 250
y= 500 



cores = {
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "amarela": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0),
    "Lime": (128, 255, 0),
    "Citrus": (230, 193, 0),
    "Vermelho": (255, 0, 0)
}

def desenhando_Tela():
    pygame.draw.rect(tela, cores["Lime"],(0,0,500,200))
    pygame.draw.rect(tela, cores["Citrus"], (0, 250 , 500, 450))
    pygame.draw.line(tela, cores["branca"], (0,200), (700, 200), 4)
    pygame.draw.line(tela, cores["branca"], (0,250), (700, 250), 4)
    pygame.draw.rect(tela, cores["Vermelho"],(x,y,10,20))



#Funcionamento do Jogo (Loop Infinito)
while True:
    desenhando_Tela()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                x= x + 5
            if event.key == K_a:
                x= x-5
            if event.key == K_w:
                y= y-5
            if event.key == K_s:
                y= y+5
    pygame.display.flip()
    pygame.display.update()

    