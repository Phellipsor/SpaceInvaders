import pygame
import sys
from bullet import Bullet


def check_events(ship):
    """Відстеження подій клавіатури та мишки"""
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                ship.move_right = True
                ship.last_move = True
            elif ev.key == pygame.K_LEFT:
                ship.move_left = True
                ship.last_move = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > ship.screct.centerx:
                ship.move_right = True
                ship.last_move = True
            elif pygame.mouse.get_pos()[0] < ship.screct.centerx:
                ship.move_left = True
                ship.last_move = False
        elif ev.type == pygame.KEYUP or ev.type == pygame.MOUSEBUTTONUP:
            ship.move_left = False
            ship.move_right = False


def update_screen(settings, screen, ship, bullets):
    screen.blit(settings.bg, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_shots(settings, screen, ship, bullets):
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)

