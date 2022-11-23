import pygame, control
from gan import Gun
from pygame.sprite import Group
from stats import Stats
from scorse import Scorse


def run():
    pygame.init()
    screan = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0 , 0 , 0)
    gan = Gun(screan)
    bullets = Group()
    inos = Group()
    control.create_army(screan, inos)
    stats = Stats()
    sc = Scorse(screan, stats)


    while True:
        control.events(screan, gan, bullets) # Передвижение пушки
        if stats.run_game:
            gan.update_gan() # новая функция пушки
            control.update(bg_color, screan, stats, sc, gan, inos, bullets)
            control.update_bullets(screan, stats, sc,  inos, bullets)
            control.update_inos(stats, screan, sc, gan, inos, bullets)

run()
