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
cobra_x = (((500/2 + 10) /10) *10) 
cobra_y= ((((700/2) + 110) /10) *10)
moeda_x= (round(randint(60, 390) / 10) * 10)
moeda_y= (round(randint(320, 630)/10 ) *10 )
x_controle = 0
y_controle= 0
velocidade=5
Pontos=0
Relogio= pygame.time.Clock()
tamanho_da_cobra= 3
pixels= []

def Desenhando_A_Tela():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["Lime"],(0,0,500,200))
    pygame.draw.rect(tela, cores["Citrus"], (0, 250 , 500, 450), 50)
    pygame.draw.rect(tela, cores["azul"], (50, 300, 400, 350) )
    pygame.draw.line(tela, cores["branca"], (0,200), (700, 200), 4)
    pygame.draw.line(tela, cores["branca"], (0,250), (700, 250), 4)
    
def desenhar_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 10, 10 ))
    
    

#Funcionamento do Jogo
while True:
    Relogio.tick(10)
    Desenhando_A_Tela()
    moedas = pygame.draw.rect(tela, cores["amarela"],(moeda_x,moeda_y,10,10))
    msg= f"Pontuação: {Pontos}"
    Mensagem= texto.render(msg, True, cores["branca"])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
             if event.type == KEYDOWN:
                if event.key == K_a:
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade
                        x_controle = 0
                if event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade
                        x_controle = 0

        cobra_x+= x_controle
        cobra_y+= y_controle
        if cobra_x == moeda_x and  cobra_y == moeda_y:
            moeda_x= (round(randint(60, 390) / 10) * 10)
            moeda_y= (round(randint(320, 630) /10 ) * 10 )
            Pontos+= 1

        desenhar_cobra(pixels)
        pixels.append([cobra_x, cobra_y])
        
        if len(pixels) > tamanho_da_cobra:
            del pixels[0]
    tela.blit(Mensagem, (250, 200))
    pygame.display.update()
   
    

    