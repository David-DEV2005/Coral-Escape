import pygame

pygame.init()

tamanho_da_Tela= (800, 800)
tela= pygame.display.set_mode(tamanho_da_Tela)
pygame.display.set_caption("Coral Escape")


cores = {
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "amarela": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}

while True:
    for event in pygame.event.get():
        if event == quit:
            pygame.quit()
    pygame.display.update()
    