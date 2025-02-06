import pygame
from pygame.locals import *
from sys import exit
from random import choice, randint
import os

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
#definição da Tela, janela do jogo. 
tamanho_da_Tela= (500, 700)
tela= pygame.display.set_mode(tamanho_da_Tela)
texto=pygame.font.SysFont('arial', 30, True, True)
pygame.display.set_caption("Coral Escape")

#Imagens 
caminho_background= os.path.join('Assets', 'background.png')
background = pygame.image.load(caminho_background)  
caminho_mapa= os.path.join('Assets', 'mapa1.png')
mapa = pygame.image.load(caminho_mapa)
Imagem_inicio = os.path.join('Assets', 'Coral Escape.png')
Tela_de_Inicio = pygame.image.load(Imagem_inicio)
terremoto_load= os.path.join('Assets', 'terremoto.png')
terremoto = pygame.image.load(terremoto_load) 
terremoto_2_load = os.path.join('Assets', 'terremoto_2.png') 
terremoto_2=  pygame.image.load(terremoto_2_load) 
final_load= os.path.join('Assets', 'tela_de_fim.png')
tela_final= pygame.image.load(final_load)

#X e Y: 
cobra_x = (((500/2 + 10) /10) *10) 
cobra_y= ((((700/2) + 110) /10) *10)
moeda_x= (round(randint(60, 390) / 10) * 10)
moeda_y= (round(randint(320, 630)/10 ) *10 )
Linhas_y= (round(randint(300, 630) /10) * 10)
x_controle = 0
y_controle= 0

#Variaveis diversas:
Cond_Linha = False
Cond_Mapa = False
velocidade=10
Mapa_cobra=[50,450,300,650]
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
final= 0 
msg_final= ['Morreu batendo em si mesmo!', 'Bateu nas extremidades. Doeu!', 
'Caiu no terremoto! cuidado!']

def Desenhando_A_Tela():
    tela.blit(background, (0, 0))
    tela.blit (mapa, (Mapa_cobra[0], Mapa_cobra[2]))
    
    
def desenhar_cobra(lista):
    cores_cobra = [cores["Vermelho"], cores["branca"], cores["preta"]]  
    for i, XeY in enumerate(lista):
        cor_atual = cores_cobra[i % len(cores_cobra)]  
        pygame.draw.rect(tela, cor_atual, (XeY[0], XeY[1], 10, 10))

def desenhar_linha(): 
    global Linhas_y, terremoto_load, terremoto

    if Cond_Linha == True:
        if Cond_Mapa== False:
            tela.blit(terremoto, (50, Linhas_y))
        if Cond_Mapa == True:
            tela.blit(terremoto_2, (100, Linhas_y))

def diminuição_do_Mapa():
    global mapa 
    global caminho_mapa
    global Linhas_y
    if Cond_Mapa == False:
        pass
    if Cond_Mapa == True: 
        global Cond_Linha
        caminho_mapa= os.path.join('Assets', 'mapa1.png')
        mapa = pygame.image.load(caminho_mapa)
        mapa = pygame.transform.scale(mapa, (300, 250))
        Mapa_cobra[0] = 100
        Mapa_cobra[1] = 400
        Mapa_cobra[2] = 350
        Mapa_cobra[3] = 600

def Inicio():
    while True:
        tela.blit(Tela_de_Inicio, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
        pygame.display.flip()

def fim():
    global Pontos, msg_final, msg_timer
    while True:
        tela.blit(tela_final, (0, 0))
        msg_timer= f"Pontuação: {Pontos}"
        Mensagem_timer= texto.render(msg_timer, True, cores["branca"])
        tela.blit(Mensagem_timer, (30, 190))    
        Fim_de_jogo= f"FIM DE JOGO!"
        Mensagem_final = texto.render(Fim_de_jogo, True, cores["branca"])
        tela.blit(Mensagem_final, (30, 230))
        Seu_final= f"{msg_final[final]}"
        Mensagem_final = texto.render(Seu_final, True, cores["branca"])
        tela.blit(Mensagem_final, (30, 270))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.flip()

def Jogo():
    global update, moeda_x, moeda_y, Pontos, Timer, timer_segundo, timer_moeda, x_controle, y_controle
    global cobra_x, cobra_y, Cond_Linha, Cond_Mapa, pixels, evento_atual, eventos_disponiveis, qnt_de_segundos
    global tamanho_da_cobra, Linhas_y, final
    while True:
        Relogio.tick(update)  
        Desenhando_A_Tela()
        pygame.draw.rect(tela, cores["amarela"], (moeda_x, moeda_y, 10, 10))
        msg_timer= f"Pontuação: {Pontos}"
        Mensagem_timer= texto.render(msg_timer, True, cores["branca"])
        tela.blit(Mensagem_timer, (250, 205))    

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
            if Cond_Mapa == False:
                moeda_x = (round(randint(60, 440) / 10) * 10)
                moeda_y = (round(randint(320, 630) / 10) * 10)
                Pontos += 1
                timer_moeda= 0
            if Cond_Mapa == True:
                moeda_x = (round(randint(110, 390) / 10) * 10)
                moeda_y = (round(randint(320, 590) / 10) * 10)
                Pontos += 1
                timer_moeda= 0

        if cobra_x != moeda_x and cobra_y != moeda_y:
            if Cond_Mapa == False:
                if timer_segundo > 0 and timer_segundo % 5 == 0:
                    timer_moeda += 1 
                if timer_moeda == 5:
                    moeda_x = (round(randint(60, 390) / 10) * 10)
                    moeda_y = (round(randint(360, 590) / 10) * 10)
                    timer_moeda = 0
            if Cond_Mapa == True:
                if  moeda_x+10 < Mapa_cobra[0] or moeda_x+10 > Mapa_cobra[1] or moeda_y+10 < Mapa_cobra [2] or moeda_y+10 > Mapa_cobra [3]:
                    moeda_x = (round(randint(110, 390) / 10) * 10)
                    moeda_y = (round(randint(320, 590) / 10) * 10)
                if timer_segundo > 0 and timer_segundo % 5 == 0:
                    timer_moeda += 1 
                if timer_moeda == 5:
                    moeda_x = (round(randint(110, 390) / 10) * 10)
                    moeda_y = (round(randint(320, 590) / 10) * 10)
                    Pontos += 1
                    timer_moeda= 0


        pixels.append([cobra_x, cobra_y])
        if len(pixels) > tamanho_da_cobra:
            del pixels[0]

        if cobra_x < Mapa_cobra[0] or cobra_x >= Mapa_cobra[1] or cobra_y < Mapa_cobra[2] or cobra_y >= Mapa_cobra[3]:
            final= 1
            fim()
            return
        #Eventos Aleatórios 
        if timer_segundo > 1:
            if timer_segundo  % 5 == 0:
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
                    elif evento_atual == 4:
                        Cond_Mapa = True
                        Cond_Linha = False
                        timer_segundo+=1
                        if 2 not in eventos_disponiveis:
                            eventos_disponiveis.append(2)
                        Linhas_y= (round(randint(350, 580) /10) * 10)
                    
                    eventos_disponiveis.remove(evento_atual)
                    
        if Cond_Linha == True:
            
            if cobra_y >= Linhas_y - 6  and cobra_y <= Linhas_y+10:
                final =2
                fim() 
                return
            if moeda_y+10 >= Linhas_y  and moeda_y+10 <= Linhas_y:
                    moeda_x= (round(randint(60, 390) / 10) * 10)
                    moeda_y= (round(randint(320, 630)/10 ) *10 )

        for pixel in pixels [:-3]:
            if pixel == [cobra_x, cobra_y]:
                final = 0
                fim()
                return
        
        diminuição_do_Mapa()
        desenhar_linha()
        desenhar_cobra(pixels)
        pygame.display.flip()
#Funcionamento do Jogo    
Inicio()
Jogo()

