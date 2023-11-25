import sys
import pygame

from player import Player
from enemy import Enemy


pygame.init()
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
bg_image = pygame.transform.scale(pygame.image.load("assets/bg.jpg"), (1080,2420))

player = Player(surface)
touched = False

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if player.rect.collidepoint(ev.pos):
                touched = True
                pygame.mouse.get_rel()
        elif ev.type == pygame.MOUSEBUTTONUP:
            touched = False
    
    clock.tick(60)
    player.screen.blit(bg_image, (0,0))  
    player.blitme() 
    if touched:
        player.rect.move_ip(pygame.mouse.get_rel())
    pygame.display.flip()
    
