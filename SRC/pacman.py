import pygame
from hell import hell
import math
pygame.init()

height2 = 900
width2 = 930
WIDTH = 1200
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")
fps = 30
timer = pygame.time.Clock()
level = hell
color = "red"
PI = math.pi
game = False
font = pygame.font.Font("freesansbold.ttf", 24)
menu_command = 0
menu_command1 = 0
menu_command2 = 0
menu_command3 = 0
menu_command4 = 0

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pygame.draw.rect(screen, "blue", self.button, 0, 5)
        pygame.draw.rect(screen, "dark gray", self.button, 5, 5)
        text = font.render(self.text, True, "light gray")
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def draw_game():
    screen.fill("black")
    command = 0
    button = Button("Play", (470, 180))
    button1 = Button("Settings", (470, 240))
    button2 = Button("Exit", (470, 300))
    button.draw()
    button1.draw()
    button2.draw()
    if button.check_clicked():
        command = 1
    if button1.check_clicked():
        command = 2
    if button2.check_clicked():
        command = 3
    return command

def draw_levels():
    screen.fill("black")
    command = 0
    button = Button("Exit", (900, 550))
    button1 = Button("Hell", (120, 270))
    button2 = Button("Dark Forest", (470, 270))
    button3 = Button("Candy Land", (820, 270))
    button.draw()
    button1.draw()
    button2.draw()
    button3.draw()
    if button.check_clicked():
        command = 1
    if button1.check_clicked():
        command = 2
    return command

def draw_option():
    screen.fill("black")
    command = 0
    button1 = Button("Select difficulty", (120, 180))
    button2 = Button("Exit", (900, 550))
    button3 = Button("Skin change", (120, 240))
    button1.draw()
    button2.draw()
    button3.draw()
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    return command

def draw_difficulty():
    screen.fill("black")
    command = 0
    button1 = Button("Easy", (120, 180))
    button2 = Button("Normal", (120, 240))
    button3 = Button("Hard", (120, 300))
    button4 = Button("Exit", (900, 450))
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    if button4.check_clicked():
        command = 4
    return command

def draw_board():
    screen.fill("black")
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
    command = 0
    button = Button("Exit", (930, 350))
    button.draw()
    if button.check_clicked():
        command = 1
    return command
running = True
while running:
    screen.fill("black")
    screen.fill("black")
    timer.tick(fps)
    if game:
        menu_command = draw_game() 
        menu_command1 = draw_levels()
        menu_command2 = draw_option()
        menu_command3 = draw_board()
        menu_command4 = draw_difficulty()
        screen.fill("black")
        if menu_command or menu_command1 or menu_command2 or menu_command3 or menu_command4 > 0:
            game = False
    else:
        game = draw_game()
        
        match menu_command:
            case 0:
                None
            case 1:
                game = draw_levels()
            case 2:
                game = draw_option()
            case 3:
                running = False
        match menu_command1:
            case 0:
                None
            case 1:
                game = draw_game()
            case 2:
                game = draw_board()
        match menu_command2:
            case 0:
                None
            case 1:
                game = draw_difficulty()
            case 2:
                game = draw_game()
        match menu_command3:
            case 0:
                None
            case 1:
                game = draw_levels()
        match menu_command4:
            case 1:
                None
            case 2:
                None
            case 3:
                None
            case 4:
                game = draw_option()

                
        #if menu_command == 1:
         #  screen.fill("black")
         #   game = draw_levels()
        #elif menu_command == 2:
        #    screen.fill("black")
        #    game = draw_option()
        #elif menu_command == 3:
        #    sys.exit()
        #elif menu_command1 == 1:
        #    screen.fill("black")
        #    game = draw_game()
        #elif menu_command1 == 2:
        #    screen.fill("black")
        #   game = draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()