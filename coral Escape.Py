import pygame
from pygame.locals import *
from sys import exit
from random import choice, randint

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
    "Vermelho": (255, 0, 0),
    }

tamanho_da_Tela= (500, 700)
tela= pygame.display.set_mode(tamanho_da_Tela)
texto=pygame.font.SysFont('arial', 30, True, True)
pygame.display.set_caption("Coral Escape")

background_topo = pygame.image.load("background_Topo.png")  
background_topo = pygame.transform.scale(background_topo, (500, 700))
mapa = pygame.image.load("Mapa-1.png")
#mapa = pygame.transform.scale(mapa, (400, 350))

#X e Y: 
cobra_x = (((500/2 + 10) /10) *10) 
cobra_y= ((((700/2) + 110) /10) *10)
moeda_x= (round(randint(60, 390) / 10) * 10)
moeda_y= (round(randint(320, 630)/10 ) *10 )
Linhas_y= (round(randint(300, 630) /10) * 10)
x_controle = 0
y_controle= 0
x_mapa = 50 
y_mapa = 300
#Variaveis diversas:
Cond_Linha = False
Cond_Mapa = True
velocidade=10
Mapa_cobra=[50,450,300,650]
Mapa_azul = [(50, 300, 400, 350)]
Eventos= randint(1,3)
Timer= 0
timer_segundo= 0
qnt_de_segundos = 7
Pontos=0
Relogio= pygame.time.Clock()
update= 10
tamanho_da_cobra= 3
pixels= []
eventos_disponiveis = [1,2,3,4]
timer_moeda = 0

def Desenhando_A_Tela():
    tela.fill(cores["preta"])
    tela.blit(background_topo, (0, 0))
    tela.blit(mapa, (x_mapa, y_mapa))
    
def desenhar_cobra(lista):
    cores_cobra = [cores["Vermelho"], cores["branca"], cores["preta"]]  
    for i, XeY in enumerate(lista):
        cor_atual = cores_cobra[i % len(cores_cobra)]  
        pygame.draw.rect(tela, cor_atual, (XeY[0], XeY[1], 10, 10))

def desenhar_linha():
    if Cond_Linha == False:
        pass
    
    if Cond_Linha == True:
        
        pygame.draw.line(tela, cores["Vermelho"], (50 , Linhas_y),(450, Linhas_y), 20)

def Movimento_do_Mapa():
    global x_mapa
    global y_mapa
    if Cond_Mapa == False:
        pass
    else:
        x_mapa += 2
        y_mapa += 2

#Funcionamento do Jogo 
while True:
    Relogio.tick(update)  
    Desenhando_A_Tela()
    pygame.draw.rect(tela, cores["amarela"], (moeda_x, moeda_y, 10, 10))
    msg= f"Pontuação: {Pontos}"
    Mensagem= texto.render(msg, True, cores["branca"])
    tela.blit(Mensagem, (250, 205))    
   
   #Timer(Funcionamento)
    if Timer < qnt_de_segundos:
        Timer+=1
    else:
        timer_segundo+=1
        tempo = texto.render("Tempo: "+str(timer_segundo), True, cores["branca"])
        Timer=0
    tempo = texto.render("Tempo: "+str(timer_segundo), True, cores["branca"])
    tela.blit(tempo, (50, 205)) 
    
    #loop de eventos do Jogo
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

    cobra_x += x_controle
    cobra_y += y_controle

    if cobra_x == moeda_x and cobra_y == moeda_y:
        moeda_x = (round(randint(60, 390) / 10) * 10)
        moeda_y = (round(randint(320, 630) / 10) * 10)
        Pontos += 1
        timer_moeda= 0
    
    if cobra_x != moeda_x and cobra_y != moeda_y:
        if timer_segundo > 0 and timer_segundo % 5 == 0:
            timer_moeda += 1 
        if timer_moeda == 5:
            moeda_x = (round(randint(60, 390) / 10) * 10)
            moeda_y = (round(randint(320, 630) / 10) * 10)
            timer_moeda = 0


    pixels.append([cobra_x, cobra_y])
    if len(pixels) > tamanho_da_cobra:
        del pixels[0]
   
    if cobra_x < Mapa_cobra[0] or cobra_x >= Mapa_cobra[1] or cobra_y < Mapa_cobra[2] or cobra_y >= Mapa_cobra[3]:
        print("FIM DE JOGO!")
        pygame.quit()
        exit()
    #Eventos Aleatórios 
    if timer_segundo > 1:
        if timer_segundo  % 15 == 0:
            if len(eventos_disponiveis) > 0:
                evento_atual= choice(eventos_disponiveis)
                if evento_atual == 1:
                    update = 30
                    qnt_de_segundos = 37
                    timer_segundo+=1
                elif evento_atual == 2:
                    Cond_Linha = True
                    timer_segundo+=1
                elif evento_atual == 3:
                    tamanho_da_cobra = 6
                    timer_segundo+=1
                '''elif evento_atual == 4: 
                    Cond_Mapa = True'''
                eventos_disponiveis.remove(evento_atual)
                
    if Cond_Linha == True:
        
        if cobra_y >= Linhas_y - 5  and cobra_y <= Linhas_y:
            print("Você bateu na linha vermelha! FIM DE JOGO!")
            pygame.quit()
            exit()
        
        if moeda_y+10 >= Linhas_y  and moeda_y+10 <= Linhas_y:
                moeda_x= (round(randint(60, 390) / 10) * 10)
                moeda_y= (round(randint(320, 630)/10 ) *10 )

    for pixel in pixels [:-3]:
        if pixel == [cobra_x, cobra_y]:
            print("Você bateu em si mesmo! FIM DE JOGO!")
            pygame.quit()
            exit()
    Movimento_do_Mapa()
    desenhar_linha()
    desenhar_cobra(pixels)
    pygame.display.update()