import pygame

from game_settings import Settings
import game_functions as gf
from ship import Ship

def run_game():
    """Ініціалізація гри та створення обєкту екрана"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Defense")
    clock = pygame.time.Clock()
    ship = Ship(screen)
    bullets = pygame.sprite.Group()
    reloaded_bullet = pygame.USEREVENT + 1

    while True:

        pygame.time.set_timer(gf.update_shots(settings, screen, ship, bullets), settings.bullet_reload)
        gf.check_events(ship)
        ship.update_pos()
        bullets.update()
        gf.update_screen(settings, screen, ship, bullets)

run_game()