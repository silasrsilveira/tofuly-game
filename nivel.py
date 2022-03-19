import imp


import pygame
from bloco import Bloco
from config import tamanho_bloco

class Nivel:

    # Configuração de Nivel
    def __init__(self,dados_nivel,surface):
        self.display_surface = surface
        self.config_nivel(dados_nivel)

        #para tela seguir
        self.mundo_troca = 0

    def config_nivel(self,layout):
        self.blocos = pygame.sprite.Group()
        for linha_indice,linha in enumerate(layout):
            for col_indice,celula in enumerate(linha):
                if celula == 'X':
                    x = col_indice * tamanho_bloco
                    y = linha_indice * tamanho_bloco
                    bloco = Bloco((x,y),tamanho_bloco)
                    self.blocos.add(bloco)

    def run(self):
        self.blocos.update(self.mundo_troca)
        self.blocos.draw(self.display_surface)