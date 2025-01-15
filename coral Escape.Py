import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#Criação de Variavéis e Funções. 

tamanho_da_Tela= (500, 700)
tela= pygame.display.set_mode(tamanho_da_Tela)
pygame.display.set_caption("Coral Escape")
cobra_x = 250
cobra_y= 500 

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
jogador= pygame.draw.rect(tela, cores["Vermelho"],(cobra_x,cobra_y,10,20))

def Desenhando_A_Tela():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["Lime"],(0,0,500,200))
    pygame.draw.rect(tela, cores["Citrus"], (0, 250 , 500, 450), 50)
    pygame.draw.rect(tela, cores["azul"], (50, 300, 400, 350) )
    pygame.draw.line(tela, cores["branca"], (0,200), (700, 200), 4)
    pygame.draw.line(tela, cores["branca"], (0,250), (700, 250), 4)
    pygame.draw.rect(tela, cores["Vermelho"],(cobra_x,cobra_y, 10, 20))
    
#Funcionamento do Jogo
while True:
    Desenhando_A_Tela()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        """if event.type == KEYDOWN:
            if event.key == K_d:
                x= x + 10
            if event.key == K_a:
                x= x-10
            if event.key == K_w:
                y= y-10
            if event.key == K_s:
                y= y+10"""
        
        #Deixar Pressionado: 
        if pygame.key.get_pressed() [K_d]:
            cobra_x += 5
        if pygame.key.get_pressed() [K_a]:
            cobra_x-= 5
        if pygame.key.get_pressed() [K_s]:
            cobra_y+= 5
        if pygame.key.get_pressed() [K_w]:
            cobra_y-= 5
        if cobra_x<=50-5 or cobra_x>=450-5:
            print('COlidiu')
        if cobra_y<= 300-5:
            print('aii')
        if cobra_y>= 640:
            print('Uiii')
            
    pygame.display.flip()
    pygame.display.update()

    