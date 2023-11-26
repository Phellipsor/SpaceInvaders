import pygame

class Enemy:
    def __init__(self, surf):
        self.image = pygame.transform.scale(pygame.image.load("assets/enemy.png"), (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = ((surf.w/2, 100))
        
        