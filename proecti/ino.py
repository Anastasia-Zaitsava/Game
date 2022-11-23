import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screan):
        """инициализируем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screan = screan
        self.image = pygame.image.load('images/inos.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        """вывод пришельца на экран"""
        self.screan.blit(self.image, self.rect)

    def update(self):
        """перемещает прищельцев"""
        self.y += 0.1
        self.rect.y = self.y
