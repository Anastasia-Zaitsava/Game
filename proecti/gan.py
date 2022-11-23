import pygame
from pygame.sprite import Sprite

class Gun(Sprite):
    def __init__(self, screen):
        """инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pyska.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False # для нажатия вправо
        self.mleft = False # влево



    def output(self):
        '''рисование пушки'''
        self.screen.blit(self.image, self.rect)

    def update_gan(self):
        '''обновление позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 4.5
        if self.mleft and self.rect.left > 0:
            self.center -= 4.5

        self.rect.centerx = self.center


    def create_gan(self):
        """расмещает пушку по центру внизу после сталкивания"""
        self.center = self.screen_rect.centerx