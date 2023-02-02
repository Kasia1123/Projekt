import pygame
from pygame.locals import *
import random
import pygame_menu

wymiary = width, height = (900,900)
droga = int(width/1.6)
drogaznak_w = int(width/80)
Prawa_linia = width/2 + droga/4
Lewa_linia = width/2 - droga/4


pygame.init()
wlaczona = False

screen = pygame.display.set_mode(wymiary)
pygame.display.set_caption("Kasia GRA")
screen.fill((50,50,50))



def start():
    astronauta = pygame.image.load("astronauta.png")
    astronauta_loc = astronauta.get_rect()
    astronauta_loc.center = Prawa_linia, height * 0.8

    meteor = pygame.image.load("meteor.png")
    meteor_loc = meteor.get_rect()
    meteor_loc.center = Lewa_linia, height * 0.2
    wlaczona = True
    predkosc = 1
    licznik = 0

    while wlaczona:
        licznik += 1
        if licznik == 1024:
            predkosc  += 0.25
            licznik = 0
            print("POZIOM:", predkosc )
        meteor_loc[1] += predkosc
        if meteor_loc[1] > height:
            meteor_loc[1] = -200
            if random.randint(0, 1) == 0:
                meteor_loc.center = Prawa_linia, -200
            else:
                meteor_loc.center = Lewa_linia, -200
        if astronauta_loc[0] == meteor_loc[0] and meteor_loc[1] > astronauta_loc[1] - 250:
            print("PRZEGRALES")
            menu.mainloop(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                wlaczona = False
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    astronauta_loc = astronauta_loc.move([-int(droga / 2), 0])
                if event.key in [K_d, K_RIGHT]:
                    astronauta_loc = astronauta_loc.move([int(droga / 2), 0])

        pygame.draw.rect(screen, (50, 50, 50), (width / 2 - droga / 2, 0, droga, height))
        pygame.draw.rect(screen, (255, 255, 255), (width / 2 - droga / 2 + drogaznak_w * 2, 0, drogaznak_w, height))
        pygame.draw.rect(screen, (255, 255, 255), (width / 2 + droga / 2 - drogaznak_w * 3, 0, drogaznak_w, height))

        screen.blit(astronauta, astronauta_loc)
        screen.blit(meteor, meteor_loc)
        pygame.display.update()
    pygame.quit()


menu = pygame_menu.Menu('Witam', 500, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Imie :', default='Katarzyna Masiarz')
menu.add.button('Graj', start)
menu.add.button('Wyjdz', pygame_menu.events.EXIT)


menu.mainloop(screen)
pygame.quit()





