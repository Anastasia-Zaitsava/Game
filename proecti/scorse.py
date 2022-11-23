import pygame.font
from gan import Gun
from pygame.sprite import Group

class Scorse():
    """вывод игровой информации"""
    def __init__(self, screan, stats):
        """инициализируем подсчет очков"""
        self.screan = screan
        self.screan_rect = screan.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74) # цвет шрифта
        self.font = pygame.font.SysFont(None, 36) # рисуем шрифт и размер
        self.image_score() # текущий счет
        self.image_high_score() # рекорд
        self.image_guns() # количество жизней


    def image_score(self):
        """преобразовывает текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0)) # передаем счет, цвет и дт.
        self.score_rect = self.score_img.get_rect() # обьект для текущего счета
        self.score_rect.right = self.score_rect.right + 430 # рисуем счет в правом углу (40 пискелей)
        self.score_rect.top = 20 # отступ сверху

    def image_guns(self):
        """количество жизней"""
        self.guns = Group()
        for gan_number in range(self.stats.guns_left):
            gan = Gun(self.screan)
            gan.rect.x = 15 + gan_number * gan.rect.width
            gan.rect.y = 20
            self.guns.add(gan)


    def image_high_score(self):
        """преобразует рекорд в гарфичнское изоражение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.score_rect.centerx
        self.high_score_rect.top = self.screan_rect.top + 40

    def show_score(self):
        """вывод счета на экран"""
        self.screan.blit(self.score_img, self.score_rect)
        self.screan.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screan)

