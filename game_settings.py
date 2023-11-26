import pygame

class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 1600
        self.bg = pygame.transform.scale(pygame.image.load("assets/bg.jpg"), (850, 1650))

        self.bullet_speed = 1
        self.bullet_reload = 2000
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = "#39FF14"