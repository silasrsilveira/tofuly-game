import imp


import pygame
from bloco import Bloco
from config import tamanho_bloco
from jogador import Jogador

class Nivel:

    # Configuração de Nivel
    def __init__(self,dados_nivel,surface):
        self.display_surface = surface
        self.config_nivel(dados_nivel)

        #para tela seguir
        self.mundo_troca = 0

    def config_nivel(self,layout):
        self.blocos = pygame.sprite.Group()
        self.jogador = pygame.sprite.GroupSingle()


        for linha_indice,linha in enumerate(layout):
            for col_indice,celula in enumerate(linha):
                x = col_indice * tamanho_bloco
                y = linha_indice * tamanho_bloco

                if celula == 'X':
                    bloco = Bloco((x,y),tamanho_bloco)
                    self.blocos.add(bloco)

                if celula == 'P':
                    jogador_sprite = Jogador((x,y))
                    self.jogador.add(jogador_sprite)

    def run(self):
        self.blocos.update(self.mundo_troca)
        self.blocos.draw(self.display_surface)
        
        # Jogador
        self.jogador.draw(self.display_surface)