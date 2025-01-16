import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Criação de Variavéis e Funções. 
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

tamanho_da_Tela= (500, 700)
tela= pygame.display.set_mode(tamanho_da_Tela)
texto=pygame.font.SysFont('arial', 30, True, True)
pygame.display.set_caption("Coral Escape")
cobra_x = 500/2 + 10
cobra_y= ((700/2) + 110)
moeda_x= (round(randint(60, 390) / 10.0) * 10.0)
moeda_y= (round(randint(320, 630)/ 10.0) * 10.0)
velocidade_x= 0
velocidade_y= 0
Pontos= 0
Relogio= pygame.time.Clock
tamanho_da_cobra= 3
pixels= []

def Desenhando_A_Tela():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["Lime"],(0,0,500,200))
    pygame.draw.rect(tela, cores["Citrus"], (0, 250 , 500, 450), 50)
    pygame.draw.rect(tela, cores["azul"], (50, 300, 400, 350) )
    pygame.draw.line(tela, cores["branca"], (0,200), (700, 200), 4)
    pygame.draw.line(tela, cores["branca"], (0,250), (700, 250), 4)
    
'''def velocidade_cobra(tecla):
    if tecla == K_RIGHT:
        velocidade_x = 15
        velocidade_y = 0
    if tecla == K_LEFT:
        velocidade_x = -15
        velocidade_y = 0
    if tecla == K_UP:
        velocidade_x = 0
        velocidade_y-= -15
    if  tecla== K_DOWN:
        velocidade_x = 0
        velocidade_y+= +15
    
    return velocidade_x and velocidade_y'''

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, cores["branca"],[pixel[0], pixel[1], tamanho, tamanho])

#Funcionamento do Jogo
while True:
    Desenhando_A_Tela()
    moedas = pygame.draw.rect(tela, cores["amarela"],(moeda_x,moeda_y,10,10))
    msg= f"Pontuação: {Pontos}"
    Mensagem= texto.render(msg, True, cores["branca"])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_d:
                velocidade_x = 15
                velocidade_y = 0
            if event.key == K_a:
                velocidade_x = -15
                velocidade_y = 0
            if event.key == K_w:
                velocidade_x = 0
                velocidade_y-= -15
            if  event.key== K_s:
                velocidade_x = 0
                velocidade_y+= +15
        
        cobra_x+= velocidade_x
        cobra_y+= velocidade_y
        
        pixels.append([cobra_x, cobra_y])
        if len(pixels) > tamanho_da_cobra:
            del pixels[0]

        desenhar_cobra(tamanho_da_cobra, pixels)

        '''if jogador.colliderect(moedas):
            moeda_x= randint(60, 390)
            moeda_y= randint(320, 630)
            Pontos+= 1''' 
    
        #Deixar Pressionado: 
        '''if pygame.key.get_pressed() [K_d]:
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
            print('Uiii')'''
    tela.blit(Mensagem, (250, 200))

    pygame.display.flip()
    pygame.display.update()

    