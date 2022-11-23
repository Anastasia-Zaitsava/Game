import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screan, gan):
        """создаем пулю в позиции пушка"""
        super(Bullet, self).__init__()
        self.screan = screan
        self.rect = pygame.Rect(0, 0, 8, 12) # рисуем пулю(прямоугольную), координаты, ширина и высота
        self.color = 139, 195, 74
        self.speed = 8.5
        self.rect.centerx = gan.rect.centerx
        self.rect.top = gan.rect.top # пуля появляется в верхней части пушки
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed # скорость заданной пули
        self.rect.y = self.y # перемещение пули вверх

    def draw_bullet(self):
        """рисуем пулю"""
        pygame.draw.rect(self.screan, self.color, self.rect)

