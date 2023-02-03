import pygame
import sys
from hell import hell
import math


pygame.init()
height = 600
width = 1200
screen = pygame.display.set_mode((width, height))
timer = pygame.time.Clock()
level = hell
color = "red"
PI = math.pi

def draw_board():

    #obrazki ścian
    pozioma_sciana_png = pygame.image.load("assets/walls/sciany_hell/sciana.png")
    pionowa_sciana_png = pygame.image.load("assets/walls/sciany_hell/pionowa_sciana.png")
    skret_lewo_png = pygame.image.load("assets/walls/sciany_hell/skret_lewo.png")
    skret_prawo_png = pygame.image.load("assets/walls/sciany_hell/skret_prawo.png")
    potrojny_dol_png = pygame.image.load("assets/walls/sciany_hell/potrojny_dol.png")
    potrojny_prawo_png = pygame.image.load("assets/walls/sciany_hell/potrojny_prawo.png")
    potrojny_lewo_png = pygame.image.load("assets/walls/sciany_hell/potrojny_lewo.png")
    potrojny_lewo_gora_png = pygame.image.load("assets/walls/sciany_hell/potrojny_lewo_gora.png")
    potrojny_prawo_gora_png = pygame.image.load("assets/walls/sciany_hell/potrojny_prawo_gora.png")

    #skalowanie grafik
    sciana_poziom1 = pygame.transform.scale(pozioma_sciana_png, (60, 80))
    sciana_poziom2 = pygame.transform.scale(pozioma_sciana_png, (80, 80))
    sciana_poziom3 = pygame.transform.scale(pozioma_sciana_png, (60, 170))
    sciana_poziom4 = pygame.transform.scale(pozioma_sciana_png, (80, 170))
    sciana_pion1 = pygame.transform.scale(pionowa_sciana_png, (90, 70))
    skret_lewo = pygame.transform.scale(skret_lewo_png, (200, 200))
    skret_prawo = pygame.transform.scale(skret_prawo_png, (200, 200))
    potrojny_dol = pygame.transform.scale(potrojny_dol_png, (150, 150))
    potrojny_prawo = pygame.transform.scale(potrojny_prawo_png, (158, 130))
    potrojny_lewo = pygame.transform.scale(potrojny_lewo_png, (158, 130))
    potrojny_lewo_gora = pygame.transform.scale(potrojny_lewo_gora_png, (215, 210))
    potrojny_prawo_gora = pygame.transform.scale(potrojny_prawo_gora_png, (215, 210))

    #krótkie poziome
    screen.blit(sciana_poziom1, (70, 106))
    screen.blit(sciana_poziom1, (470, 106))
    #długie poziome
    screen.blit(sciana_poziom2, (170, 376))
    screen.blit(sciana_poziom2, (350, 376))
    #grube poziome krótkie
    screen.blit(sciana_poziom3, (70, 1))
    screen.blit(sciana_poziom3, (470, 1))
    #grube poziome długie
    screen.blit(sciana_poziom4, (170, 1))
    screen.blit(sciana_poziom4, (350, 1))
    #pionowe
    screen.blit(sciana_pion1, (377, 297))
    screen.blit(sciana_pion1, (137, 297))
    #skręt w lewo
    screen.blit(skret_lewo, (57, 312))
    #skręt w prawo
    screen.blit(skret_prawo, (342, 312))
    #potrójny dół
    screen.blit(potrojny_dol, (225, 312))
    screen.blit(potrojny_dol, (225, 420))
    screen.blit(potrojny_dol, (225, 96))
    #potrójny w prawo
    screen.blit(potrojny_prawo, (127, 133))
    #potrójny w lewo
    screen.blit(potrojny_lewo, (315, 133))
    #potrójny lewo góra
    screen.blit(potrojny_lewo_gora, (343, 384))
    #potrójny prawo góra
    screen.blit(potrojny_prawo_gora, (40, 384))

    
    

    
    #rysowanie linii i kropek
    num1 = ((630 - 50) // 32)
    num2 = (600 // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            #małe kropki
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            #duże kropki
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            #pionowe linie
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            #poziome linie
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            #skręt z lewej w dół
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            #skręt z prawej w dół
            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            #skręt z prawej w górę
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            #skręt z lewej w górę
            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            #biała linia pozioma
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
 

            
    #działanie programu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        
draw_board()
