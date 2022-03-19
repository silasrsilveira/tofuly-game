import pygame

### Configurar a sprite definir a posição e qual tamanhdo de cada bloco
class Bloco(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        ## um size será X e outro Y
        self.image = pygame.Surface((size,size))
        self.image.fill('turquoise')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_troca):
        self.rect.x += x_troca