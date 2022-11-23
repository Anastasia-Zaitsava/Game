import pygame, sys
from bul import Bullet
from ino import Ino
import time


def events(screan, gan, bullets):
    '''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # передвижение вправо
            if event.key == pygame.K_d:
                gan.mright = True
            elif event.key == pygame.K_a: # передвижение влево
                gan.mleft = True
            elif event.key == pygame.K_SPACE: # пробел стрельба
                new_bullet = Bullet(screan, gan)
                bullets.add(new_bullet) # добавляем пулю в контейнер

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d: # передвижение вправо
                gan.mright = False
            elif event.key == pygame.K_a: # передвижение влево
                gan.mleft = False


def update(bg_color, screan, stats, sc, gan, inos, bullets):
    """"обновление экрана"""
    screan.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites(): # выводим пулю позади пушки
        bullet.draw_bullet()
    gan.output()
    inos.draw(screan)
    pygame.display.flip()


def update_bullets(screan, stats, sc,  inos, bullets):
    """обновлять позицию пули (обираем их, после выхода за пределы поля"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
#    print(len(bullets)) # проверка уходят ли пульки или нет
    collections = pygame.sprite.groupcollide(bullets, inos, True, True) # колизии (пересекаются) - при встрече удаляется и пуля и пришелец
    # ключ значение
    if collections:
        for inos in collections.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()

    if len(inos) == 0: # делаем бесконечную армию, на случай если уничтожим ряды
        bullets.empty()
        create_army(screan, inos)



def gan_kill(stats, screan, sc, gan, inos, bullets):
    """столкновение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty() # удаляем пришельцев
        bullets.empty() # удаляем пули
        create_army(screan, inos)
        gan.create_gan()
        time.sleep(1)
    else:
        stats.run_game = False # если заканчиваются жизни, то выход из игры
        sys.exit()


def update_inos(stats, screan, sc, gan, inos, bullets):
    """обнавляет позицию пришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gan, inos):
#        print('!!!!!!!!') # если пушка пересекается с пришельцами, выводиться !!!
        gan_kill(stats, screan, sc, gan, inos, bullets)
    inos_ckeck(stats, screan, sc, gan, inos, bullets)


def inos_ckeck(stats, screan, sc,  gan, inos, bullets):
    """проверка, когда ударяется пришельцы"""
    screan_rect = screan.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screan_rect.bottom: # если позиция пришельца пересекается с пушкой или экраном, то перезагружается
            gan_kill(stats, screan, sc, gan, inos, bullets)
            break

def create_army(screan, inos):
    """создание армии пришельцев"""
    ino = Ino(screan)
    ino_width = ino.rect.width # ширина пришельца
    number_ino_x = int((900 - 2 * ino_width)/ ino_width) # сколько прешельцев поместиться на экран, ширина экрана и формула
    ino_height = ino.rect.height # высота
    number_ino_y = int((600 - 100 - 2 * ino_height) / ino_height)


    for row_number in range(number_ino_y - 1):
          for ino_number in range(number_ino_x):
              ino = Ino(screan)
              ino.x = ino_width + ino_width * ino_number # ширина пришельца
              ino.y = ino_height + (ino_height * row_number)
              ino.rect.x = ino.x
              ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
              inos.add(ino)

def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score: # постоянно проверяет счет за одного прицельца
        stats.high_score = stats.score
        sc.image_high_score()
        with open("high_scote.txt", "w") as f:
            f.write(str(stats.high_score))

