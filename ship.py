import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.screct = screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load("assets/alien.png"), (146,146))
        self.mirror_image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
        self.rect = self.image.get_rect()
        self.rect.center = ((self.screct.centerx, self.screct.h-150))
        self.move_right = False
        self.move_left = False
        self.last_move = True

    def update_pos(self):
        if self.move_right and self.rect.right < self.screct.right:
            self.rect.centerx += 1.5
        elif self.move_left and self.rect.left > self.screct.left:
            self.rect.centerx -= 2
        
    def blitme(self):
        if self.last_move == True:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.mirror_image, self.rect)