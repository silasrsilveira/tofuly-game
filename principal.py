import pygame, sys
from config import *
from nivel import Nivel

# Pygame Setup
pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
fps = pygame.time.Clock()
nivel = Nivel(nivel_mapa,tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill('black')
    nivel.run()

    pygame.display.update()
    fps.tick(60)