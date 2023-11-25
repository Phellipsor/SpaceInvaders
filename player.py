import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.screct = screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load("assets/alien.png"), (186,186))
        self.rect = self.image.get_rect()
        self.rect.center = ((self.screct.centerx, self.screct.h-200))
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)