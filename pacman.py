import pygame
import sys
from hell import hell1, hell2
import math
import random
pygame.init()

height2 = 950
width2 = 900
WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")
fps = 30
timer = pygame.time.Clock()
level = hell1
level2 = hell2
color = "red"
PI = math.pi
game = False
font = pygame.font.Font("freesansbold.ttf", 24)
menu_command = 0
menu_command1 = 0
menu_command2 = 0
menu_command3 = 0
menu_command4 = 0
pacman_images = []
flicker = False
turns_allowed = [False, False, False, False]
direction_command = 0
pacman_speed = 2
score = 0
run1 = True; run2 = True; run3 = True
run11 = True; run22 = True; run33 = True
moving = False
background = pygame.image.load("C:/Users/kordian.zawiszewski/Desktop/praktyki2023-1/SRC/assets/background_resized.png")




Fred_x = 565
Fred_y = 185
Fred_direction = 2
Emily_x = 700
Emily_y = 600
Emily_direction = 2
Jessie_x = 356
Jessie_y = 550
Jessie_direction = 2
Jordan_x = 700
Jordan_y = 160
Jordan_direction = 2
Thanos_x = 120
Thanos_y = 700
Thanos_direction = 2
Fred_box = False
Emily_box = False
Jessie_box = False
Jordan_box = False
Thanos_box = False
ghost_speed = 2
Fre_images = []
Emil_images = []
Jorda_images = []
Thano_images = []
fremily_number = 0
jordan_number = 0
thanos_number = 0


for i in range(1, 4):
    pacman_images.append(pygame.transform.scale(pygame.image.load(f"C:/Users/kordian.zawiszewski/Desktop/praktyki2023-1/SRC/assets/pacman/{i}_pacman.png"), (45, 45)))
for i in range(1,8):
    Emil_images.append(pygame.transform.scale(pygame.image.load(f"C:/Users/kordian.zawiszewski/Desktop/praktyki2023-1/SRC/assets/duszki/emily/1.png"), (45, 45)))
for i in range(1,8):
    Fre_images.append(pygame.transform.scale(pygame.image.load(f"C:/Users/kordian.zawiszewski/Desktop/praktyki2023-1/SRC/assets/duszki/fred/1.png"), (45, 45)))
for i in range(1,7):
    Jorda_images.append(pygame.transform.scale(pygame.image.load(f"C:/Users/kordian.zawiszewski/Desktop/praktyki2023-1/SRC/assets/duszki/jordan/1.png"), (45, 45)))
for i in range(1,13):
    Thano_images.append(pygame.transform.scale(pygame.image.load(f"C:/Users/kordian.zawiszewski/Desktop/praktyki2023-1/SRC/assets/duszki/thanos/1.png"), (45, 45)))

#losowanie położenia owocka: Baklazan
while run1:
    i = random.randint(0, 32)
    j = random.randint(0, 29)
    if level[i][j] == 1 or 0:
        level[i][j] = 10
        run1 = False
#losowanie położenia owocka: Arbuz
while run2:
    i = random.randint(0, 32)
    j = random.randint(0, 29)
    if level[i][j] == 1 or 0:
        level[i][j] = 11
        run2 = False
#losowanie położenia owocka: Banan
while run3:
    i = random.randint(0, 32)
    j = random.randint(0, 29)
    if level[i][j] == 1 or 0:
        level[i][j] = 12
        run3 = False
#losowanie położenia owocka: Baklazan1
while run11:
    i = random.randint(0, 32)
    j = random.randint(0, 29)
    if hell2[i][j] == 1 or 0:
        hell2[i][j] = 10
        run11 = False
#losowanie położenia owocka: Arbuz1
while run22:
    i = random.randint(0, 32)
    j = random.randint(0, 29)
    if hell2[i][j] == 1 or 0:
        hell2[i][j] = 11
        run22 = False
#losowanie położenia owocka: Banan1
while run33:
    i = random.randint(0, 32)
    j = random.randint(0, 29)
    if hell2[i][j] == 1 or 0:
        hell2[i][j] = 12
        run33 = False


pacman_x = 450
pacman_y = 663
direction = 0
counter = 0
center_x = pacman_x + 23
center_y = pacman_y + 24

#--------------------------------------------#--------------------------------------------

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (180, 40))

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

#--------------------------------------------#--------------------------------------------

class Ghost():
    def __init__(self, x_coord, y_coord, target, speed, img, direct, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 25
        self.center_y = self.y_pos + 25
        self.target = target
        self.speed = speed
        self.img = img
        self.direction = direct
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()

    def draw(self):
        if True:
            screen.blit(self.img, (self.x_pos, self.y_pos))
        
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect

    def check_collisions(self):
        num1 = ((HEIGHT-50)//32)
        num2 = (WIDTH//30)
        num3 = 15
        self.turns = [False, False, False , False]
        if self.center_x // 30 < 29:
            if level[self.center_y//num1][(self.center_x - num3)//num2] < 3 \
                or (level[self.center_y//num1][(self.center_x - num3)//num2] == 9 and (
                    self.in_box)):
                    self.turns[1] = True
            if level[self.center_y//num1][(self.center_x + num3)//num2] < 3 \
                or (level[self.center_y//num1][(self.center_x + num3)//num2] == 9 and (
                    self.in_box)):
                    self.turns[0] = True
            if level[(self.center_y + num3)//num1][self.center_x//num2] < 3 \
                or (level[(self.center_y + num3)//num1][self.center_x//num2] == 9 and (
                    self.in_box)):
                    self.turns[3] = True
            if level[(self.center_y - num3)//num1][self.center_x//num2] < 3 \
                or (level[(self.center_y - num3)//num1][self.center_x//num2] == 9 and (
                    self.in_box)):
                    self.turns[2] = True


            if self.direction == 2 or self.direction == 3:
                if 12 <= self.center_x % num2 <= 18:
                    if level[(self.center_y + num3)//num1][self.center_x//num2] < 3 \
                        or (level[(self.center_y + num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[3] = True
                    if level[(self.center_y - num3)//num1][self.center_x//num2] < 3 \
                        or (level[(self.center_y - num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[2] = True
                if 12 <= self.center_x % num1 <= 18:
                    if level[self.center_y//num1][(self.center_x - num2)//num2] < 3 \
                        or (level[self.center_y//num1][(self.center_x - num2)//num2] == 9 and (
                            self.in_box)):
                        self.turns[1] = True
                    if level[self.center_y//num1][(self.center_x + num2)//num2] < 3 \
                        or (level[self.center_y//num1][(self.center_x + num2)//num2] == 9 and (
                            self.in_box)):
                        self.turns[0] = True

            if self.direction == 0 or self.direction == 1:
                if 12 <= self.center_x % num2 <= 18:
                    if level[(self.center_y + num3)//num1][self.center_x//num2] < 3 \
                        or (level[(self.center_y + num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[3] = True
                    if level[(self.center_y - num3)//num1][self.center_x//num2] < 3 \
                        or (level[(self.center_y - num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[2] = True
                if 12 <= self.center_x % num1 <= 18:
                    if level[self.center_y//num1][(self.center_x - num3)//num2] < 3 \
                        or (level[self.center_y//num1][(self.center_x - num3)//num2] == 9 and (
                            self.in_box)):
                        self.turns[1] = True
                    if level[self.center_y//num1][(self.center_x + num3)//num2] < 3 \
                        or (level[self.center_y//num1][(self.center_x + num3)//num2] == 9 and (
                            self.in_box)):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x_pos < 550 and 370 < self.y_pos < 490:
            self.in_box = True
        else:
            self.in_box = False            

        return self.turns, self.in_box
    
    def move_fred(self):
    #podaza za graczem
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[0] < self.x_pos and self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction   

    def move_jordan(self):
        #po dotknieciu sciany idzie w strone gracza
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[2]:
                self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[3]:
                self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction

    def move_thanos(self):
        # dziala jak fred do gory i na dol, i jak jordan na lewo i prawo
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[3]:
                self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction

    def move_emily(self):
        # dziala jak fred na lewo i prawo, oraz jak jordan do gory i dolu
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[0] < self.x_pos and self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction  


class Ghost1():
    def __init__(self, x_coord, y_coord, target, speed, img, direct, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 25
        self.center_y = self.y_pos + 25
        self.target = target
        self.speed = speed
        self.img = img
        self.direction = direct
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions1()
        self.rect = self.draw()

    def draw(self):
        if True:
            screen.blit(self.img, (self.x_pos, self.y_pos))
        
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect

    
    def check_collisions1(self):
        num1 = ((HEIGHT-50)//32)
        num2 = (WIDTH//30)
        num3 = 15
        self.turns = [False, False, False , False]
        if self.center_x // 30 < 29:
            if level2[self.center_y//num1][(self.center_x - num3)//num2] < 3 \
                or (level2[self.center_y//num1][(self.center_x - num3)//num2] == 9 and (
                    self.in_box)):
                    self.turns[1] = True
            if level2[self.center_y//num1][(self.center_x + num3)//num2] < 3 \
                or (level2[self.center_y//num1][(self.center_x + num3)//num2] == 9 and (
                    self.in_box)):
                    self.turns[0] = True
            if level2[(self.center_y + num3)//num1][self.center_x//num2] < 3 \
                or (level2[(self.center_y + num3)//num1][self.center_x//num2] == 9 and (
                    self.in_box)):
                    self.turns[3] = True
            if level2[(self.center_y - num3)//num1][self.center_x//num2] < 3 \
                or (level2[(self.center_y - num3)//num1][self.center_x//num2] == 9 and (
                    self.in_box)):
                    self.turns[2] = True


            if self.direction == 2 or self.direction == 3:
                if 12 <= self.center_x % num2 <= 18:
                    if level2[(self.center_y + num3)//num1][self.center_x//num2] < 3 \
                        or (level2[(self.center_y + num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[3] = True
                    if level2[(self.center_y - num3)//num1][self.center_x//num2] < 3 \
                        or (level2[(self.center_y - num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[2] = True
                if 12 <= self.center_x % num1 <= 18:
                    if level2[self.center_y//num1][(self.center_x - num2)//num2] < 3 \
                        or (level2[self.center_y//num1][(self.center_x - num2)//num2] == 9 and (
                            self.in_box)):
                        self.turns[1] = True
                    if level2[self.center_y//num1][(self.center_x + num2)//num2] < 3 \
                        or (level2[self.center_y//num1][(self.center_x + num2)//num2] == 9 and (
                            self.in_box)):
                        self.turns[0] = True

            if self.direction == 0 or self.direction == 1:
                if 12 <= self.center_x % num2 <= 18:
                    if level2[(self.center_y + num3)//num1][self.center_x//num2] < 3 \
                        or (level2[(self.center_y + num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[3] = True
                    if level2[(self.center_y - num3)//num1][self.center_x//num2] < 3 \
                        or (level2[(self.center_y - num3)//num1][self.center_x//num2] == 9 and (
                            self.in_box)):
                        self.turns[2] = True
                if 12 <= self.center_x % num1 <= 18:
                    if level2[self.center_y//num1][(self.center_x - num3)//num2] < 3 \
                        or (level2[self.center_y//num1][(self.center_x - num3)//num2] == 9 and (
                            self.in_box)):
                        self.turns[1] = True
                    if level2[self.center_y//num1][(self.center_x + num3)//num2] < 3 \
                        or (level2[self.center_y//num1][(self.center_x + num3)//num2] == 9 and (
                            self.in_box)):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x_pos < 550 and 370 < self.y_pos < 490:
            self.in_box = True
        else:
            self.in_box = False            

        return self.turns, self.in_box


    def move_fred(self):
    #podaza za graczem
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[0] < self.x_pos and self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction   

    def move_jordan(self):
        #po dotknieciu sciany idzie w strone gracza
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[2]:
                self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[3]:
                self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction

    def move_thanos(self):
        # dziala jak fred do gory i na dol, i jak jordan na lewo i prawo
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[3]:
                self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction

    def move_emily(self):
        # dziala jak fred na lewo i prawo, oraz jak jordan do gory i dolu
        if self.direction == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                self.x_pos += self.speed
        elif self.direction == 1:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                self.x_pos -= self.speed
        elif self.direction == 2:
            if self.target[0] < self.x_pos and self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y_pos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
            elif self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direction = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direction  

#--------------------------------------------

def draw_game():
    screen.fill("black")
    screen.blit(background, (0, 0))
    command = 0
    button = Button("Play", (320, 180))
    button1 = Button("Settings", (320, 240))
    button2 = Button("Exit", (320, 300))
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

def get_targets(Fre_x, Fre_y, Emil_x, Emil_y, Jorda_x, Jorda_y, Thano_x ,Thano_y):
    if 340 < Fre_x < 520 and 435< Fre_y < 390:
        Fre_target = (400, 100)
    else:
        Fre_target = (pacman_x, pacman_y)
    if 340 < Emil_x < 520 and 435 < Emil_y < 390:
        Emil_target = (400, 100)
    else:
        Emil_target = (pacman_x, pacman_y)
    if 340 < Jorda_x < 520 and 435 < Jorda_y < 390:
        Jorda_target = (400, 100)
    else:
        Jorda_target = (pacman_x, pacman_y)
    if 340 < Thano_x < 520 and 435 < Thano_y < 390:
        Thano_target = (400, 100)
    else:
        Thano_target = (pacman_x, pacman_y)
    

    return [Fre_target, Emil_target, Jorda_target, Thano_target]
targets = [(pacman_x, pacman_y),(pacman_x, pacman_y),(pacman_x, pacman_y),(pacman_x, pacman_y)]


#--------------------------------------------#--------------------------------------------

def draw_levels():
    screen.blit(background, (0, 0))
    command = 0
    button = Button("Exit", (600, 750))
    button1 = Button("Hell-1", (320, 270))
    button2 = Button("Hell-2", (320, 450))
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

#--------------------------------------------#--------------------------------------------

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

#--------------------------------------------#--------------------------------------------

def draw_score():
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (10, 920))

def draw_endgame_screen_viktory():
    screen.fill("black")
    screen.blit(background, (0, 0))
    command = 0
    viktory_text = font.render("Zwycięstwo", True, (200, 200, 200))
    screen.blit(viktory_text, (380, 100))
    button1 = Button("Restart", (320, 380))
    button2 = Button("Main menu", (320, 440))
    button3 = Button("Exit", (320, 500))
    button1.draw()
    button2.draw()
    button3.draw()
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command

#--------------------------------------------#--------------------------------------------

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

#--------------------------------------------#--------------------------------------------


def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (height2 - 50) // 32
    num2 = (width2 // 30)
    num3 = 15
    if centerx // 30 < 29:
        if direction == 0:
            if level[centery // num1][(centerx - num3) // num2] < 3 or level[centery // num1][(centerx - num3) // num2] > 9:
                turns[1] = True
        if direction == 1:
            if level[centery // num1][(centerx + num3) // num2] < 3 or level[centery // num1][(centerx + num3) // num2] > 9:
                turns[0] = True
        if direction == 2:
            if level[(centery + num3)//num1][centerx // num2] < 3 or level[(centery + num3)//num1][centerx // num2] > 9:
                turns[3] = True
        if direction == 3:
            if level[(centery - num3)//num1][(centerx - num3) // num2] < 3 or level[(centery - num3)//num1][(centerx - num3) // num2] > 9:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3) // num1][centerx // num2] < 3 or level[(centery + num3) // num1][centerx // num2] > 9:
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 3 or level[(centery - num3) // num1][centerx // num2] > 9:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num2) // num2] < 3 or level[centery // num1][(centerx - num2) // num2] > 9:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 3 or level[centery // num1][(centerx + num2) // num2] > 9:
                    turns[0] = True

        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num1) // num1][centerx // num2] < 3 or level[(centery + num1) // num1][centerx // num2] > 9:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 3 or level[(centery - num1) // num1][centerx // num2] > 9:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num3) // num2] < 3 or level[centery // num1][(centerx - num3) // num2] > 9:
                    turns[1] = True
                if level[centery // num1][(centerx + num3) // num2] < 3 or level[centery // num1][(centerx + num3) // num2] > 9:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True
    return turns

def check_position2(centerx, centery):
    turns = [False, False, False, False]
    num1 = (height2 - 50) // 32
    num2 = (width2 // 30)
    num3 = 15
    if centerx // 30 < 29:
        if direction == 0:
            if level2[centery // num1][(centerx - num3) // num2] < 3 or level2[centery // num1][(centerx - num3) // num2] > 9:
                turns[1] = True
        if direction == 1:
            if level2[centery // num1][(centerx + num3) // num2] < 3 or level2[centery // num1][(centerx + num3) // num2] > 9:
                turns[0] = True
        if direction == 2:
            if level2[(centery + num3)//num1][centerx // num2] < 3 or level2[(centery + num3)//num1][centerx // num2] > 9:
                turns[3] = True
        if direction == 3:
            if level2[(centery - num3)//num1][(centerx - num3) // num2] < 3 or level2[(centery - num3)//num1][(centerx - num3) // num2] > 9:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level2[(centery + num3) // num1][centerx // num2] < 3 or level2[(centery + num3) // num1][centerx // num2] > 9:
                    turns[3] = True
                if level2[(centery - num3) // num1][centerx // num2] < 3 or level2[(centery - num3) // num1][centerx // num2] > 9:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level2[centery // num1][(centerx - num2) // num2] < 3 or level2[centery // num1][(centerx - num2) // num2] > 9:
                    turns[1] = True
                if level2[centery // num1][(centerx + num2) // num2] < 3 or level2[centery // num1][(centerx + num2) // num2] > 9:
                    turns[0] = True

        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level2[(centery + num1) // num1][centerx // num2] < 3 or level2[(centery + num1) // num1][centerx // num2] > 9:
                    turns[3] = True
                if level2[(centery - num1) // num1][centerx // num2] < 3 or level2[(centery - num1) // num1][centerx // num2] > 9:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level2[centery // num1][(centerx - num3) // num2] < 3 or level2[centery // num1][(centerx - num3) // num2] > 9:
                    turns[1] = True
                if level2[centery // num1][(centerx + num3) // num2] < 3 or level2[centery // num1][(centerx + num3) // num2] > 9:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True
    return turns
#--------------------------------------------#--------------------------------------------
#movement pacmana
def move_pacman(pacm_x, pacm_y):
    if direction == 0 and turns_allowed[0]:
        pacm_x += pacman_speed
    elif direction == 1 and turns_allowed[1]:
        pacm_x -= pacman_speed
    elif direction == 2 and turns_allowed[2]:
        pacm_y -= pacman_speed
    elif direction == 3 and turns_allowed[3]:
        pacm_y += pacman_speed
    return pacm_x, pacm_y

#--------------------------------------------#--------------------------------------------

def check_points(score2):
    num1 = (height2 - 50) // 32
    num2 = width2 // 30
    if 0 < pacman_x < 870:
        if level[center_y // num1][center_x // num2] == 1:
            level[center_y // num1][center_x // num2] = 0
            score2 += 10
        if level[center_y // num1][center_x // num2] == 2:
            level[center_y // num1][center_x // num2] = 0
            score2 += 50
    return score2

def check_points2(score2):
    num1 = (height2 - 50) // 32
    num2 = width2 // 30
    if 0 < pacman_x < 870:
        if level2[center_y // num1][center_x // num2] == 1:
            level2[center_y // num1][center_x // num2] = 0
            score2 += 10
        if level2[center_y // num1][center_x // num2] == 2:
            level2[center_y // num1][center_x // num2] = 0
            score2 += 50
    return score2
#--------------------------------------------#--------------------------------------------
#efekty owocków przy zebraniu
def check_fruit(speed):

    num1 = (height2 - 50) // 32
    num2 = width2 // 30
    if 0 < pacman_x < 870:

        if level[center_y // num1][center_x // num2] == 10:
            level[center_y // num1][center_x // num2] = 0
            print("Zjadłeś owocka: baklazan")
            speed = 3
        if level2[center_y // num1][center_x // num2] == 10:
            level2[center_y // num1][center_x // num2] = 0
            print("Zjadłeś owocka: baklazan")
            speed = 3
                

        if level[center_y // num1][center_x // num2] == 12:
            level[center_y // num1][center_x // num2] = 0
            print("Zjadłeś owocka: banan")
            speed = 1
        if level2[center_y // num1][center_x // num2] == 12:
            level2[center_y // num1][center_x // num2] = 0
            print("Zjadłeś owocka: banan")
            speed = 1

    return speed

#------------------------------------------------------------------------------------------

def check_fruit2(pac_x, pac_y):
    num1 = (height2 - 50) // 32
    num2 = width2 // 30
    if 0 < pacman_x < 870:

        if level[center_y // num1][center_x // num2] == 11:
            level[center_y // num1][center_x // num2] = 0
            print("Zjadłeś owocka: arbuz")
            num = random.randint(1, 4)
            match num:
                case 1:
                    pac_x = 450
                    pac_y = 663
                case 2:
                    pac_x = 660
                    pac_y = 410
                case 3:
                    pac_x = 200
                    pac_y = 207
                case 4:
                    pac_x = 800
                    pac_y = 657
        if level2[center_y // num1][center_x // num2] == 11:
            level2[center_y // num1][center_x // num2] = 0
            print("Zjadłeś owocka: arbuz")
            num = random.randint(1, 4)
            match num:
                case 1:
                    pac_x = 450
                    pac_y = 663
                case 2:
                    pac_x = 660
                    pac_y = 410
                case 3:
                    pac_x = 200
                    pac_y = 207
                case 4:
                    pac_x = 800
                    pac_y = 657
    return pac_x, pac_y


#--------------------------------------------#--------------------------------------------

def draw_board():

    run1 = True; run2 = True; run3 = True


    screen.fill("black")
    #obrazki ścian
    pozioma_sciana_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/pozioma_sciana.png")
    pionowa_sciana_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/pionowa_sciana.png")
    skret_lewo_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/skret_lewo.png")
    skret_prawo_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/skret_prawo.png")
    potrojny_dol_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_dol.png")
    potrojny_prawo_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_prawo.png")
    potrojny_lewo_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_lewo.png")
    potrojny_lewo_gora_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_lewo_gora.png")
    potrojny_prawo_gora_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_prawo_gora.png")

    #obrazki owocków
    baklazan_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/fruits/eggplant1.png")
    banan_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/fruits/banana.png")
    watermelon_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/fruits/watermelon.png")

    #skalowanie grafik
    sciana_poziom1 = pygame.transform.scale(pozioma_sciana_png, (90, 115))
    sciana_poziom2 = pygame.transform.scale(pozioma_sciana_png, (120, 138))
    sciana_poziom3 = pygame.transform.scale(pozioma_sciana_png, (90, 265))
    sciana_poziom4 = pygame.transform.scale(pozioma_sciana_png, (125, 265))
    sciana_pion1 = pygame.transform.scale(pionowa_sciana_png, (135, 115))
    skret_lewo = pygame.transform.scale(skret_lewo_png, (300, 310))
    skret_prawo = pygame.transform.scale(skret_prawo_png, (300, 310))
    potrojny_dol = pygame.transform.scale(potrojny_dol_png, (230, 230))
    potrojny_prawo = pygame.transform.scale(potrojny_prawo_png, (250, 215))
    potrojny_lewo = pygame.transform.scale(potrojny_lewo_png, (250, 215))
    potrojny_lewo_gora = pygame.transform.scale(potrojny_lewo_gora_png, (330, 340))
    potrojny_prawo_gora = pygame.transform.scale(potrojny_prawo_gora_png, (330, 340))
    baklazan_png1 = pygame.transform.scale(baklazan_png, (35, 35))
    bananna_png1 = pygame.transform.scale(banan_png, (35, 35))
    watermelon_png1 = pygame.transform.scale(watermelon_png, (35, 35))

    #krótkie poziome
    screen.blit(sciana_poziom1, (105, 170))
    screen.blit(sciana_poziom1, (705, 170))
    #długie poziome
    screen.blit(sciana_poziom2, (255, 580))
    screen.blit(sciana_poziom2, (525, 580))
    #grube poziome krótkie
    screen.blit(sciana_poziom3, (105, 1))
    screen.blit(sciana_poziom3, (705, 1))
    #grube poziome długie
    screen.blit(sciana_poziom4, (253, 1))
    screen.blit(sciana_poziom4, (523, 1))
    #pionowe
    screen.blit(sciana_pion1, (207, 460))
    screen.blit(sciana_pion1, (567, 460))
    #skręt w lewo
    screen.blit(skret_lewo, (85, 485))
    #skręt w prawo
    screen.blit(skret_prawo, (513, 485))
    #potrójny dół
    screen.blit(potrojny_dol, (335, 150))
    screen.blit(potrojny_dol, (335, 485))
    screen.blit(potrojny_dol, (335, 655))
    #potrójny w prawo
    screen.blit(potrojny_prawo, (185, 200))
    #potrójny w lewo
    screen.blit(potrojny_lewo, (465, 200))
    #potrójny lewo góra
    screen.blit(potrojny_lewo_gora, (512, 590))
    #potrójny prawo góra
    screen.blit(potrojny_prawo_gora, (58, 590))

    
    

    
    #rysowanie linii i kropek
    num1 = ((950 - 50) // 32)
    num2 = (900 // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            #małe kropki
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            #duże kropki
            if level[i][j] == 2 and not flicker:
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
            #baklazan
            if level[i][j] == 10:
                screen.blit(baklazan_png1,(j * num2 + ((0.1 * num2) - 5), i * num1 + ((0.1 * num1) - 5)))
            #watermelon
            if level[i][j] == 11:
                screen.blit(watermelon_png1,(j * num2 + ((0.1 * num2) - 5), i * num1 + ((0.1 * num1) - 5)))
            #bananna
            if level[i][j] == 12:
                screen.blit(bananna_png1,(j * num2 + ((0.1 * num2) - 5), i * num1 + ((0.1 * num1) - 5)))

    #RIGHT, LEFT, UP, DOWN
    if direction == 0:
        screen.blit(pacman_images[counter // 7], (pacman_x, pacman_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(pacman_images[counter // 7], True, False), (pacman_x, pacman_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 7], 90), (pacman_x, pacman_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 7], 270), (pacman_x, pacman_y))
    command = 0
    button = Button("Exit", (600, 900))
    button.draw()
    if button.check_clicked():
        command = 1
    return command

def draw_board2():
    level2 = hell2
    screen.fill("black")
    #obrazki ścian
    pozioma_sciana_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/pozioma_sciana.png")
    pionowa_sciana_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/pionowa_sciana.png")
    potrojny_lewo_gora_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_lewo_gora.png")
    potrojny_prawo_gora_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_prawo_gora.png")
    potrojne_nowe1_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojne_nowe1.png")
    potrojne_nowe2_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojne_nowe2.png")
    slalom1_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/slalom1.png")
    slalom2_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/slalom2.png")
    skret_prawo_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/skret_prawo_nowe.png")
    skret_lewo_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/skret_lewo_nowe.png")
    skret_prawo_dol_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/skret_prawo_dol.png")
    skret_lewo_dol_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/skret_lewo_dol.png")
    sciana_u_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/sciana_u.png")
    potrojny_nowy_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/walls/hell/potrojny_nowy.png")

    #obrazki owocków
    baklazan_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/fruits/eggplant1.png")
    banan_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/fruits/banana.png")
    watermelon_png = pygame.image.load("C:/Users/kordian.zawiszewski/praktyki2023-1/SRC/assets/fruits/watermelon.png")

    #skalowanie grafik
    sciana_poziom2 = pygame.transform.scale(pozioma_sciana_png, (180, 120))
    sciana_poziom3 = pygame.transform.scale(pozioma_sciana_png, (210, 240))
    sciana_poziom4 = pygame.transform.scale(pozioma_sciana_png, (90, 400))
    sciana_poziom5 = pygame.transform.scale(pozioma_sciana_png, (90, 520))
    sciana_pion1 = pygame.transform.scale(pionowa_sciana_png, (140, 115))
    potrojny_lewo_gora = pygame.transform.scale(potrojny_lewo_gora_png, (220, 250))
    potrojny_prawo_gora = pygame.transform.scale(potrojny_prawo_gora_png, (220, 250))
    #potrojne_nowe1 = pygame.transform.scale(potrojne_nowe1_png, (215, 210))
    baklazan_png1 = pygame.transform.scale(baklazan_png, (35, 35))
    bananna_png1 = pygame.transform.scale(banan_png, (35, 35))
    watermelon_png1 = pygame.transform.scale(watermelon_png, (35, 35))
   
    #długie poziome
    screen.blit(sciana_poziom2, (105, 419))
    screen.blit(sciana_poziom2, (615, 419))
    #długa gruba 
    screen.blit(sciana_poziom3, (345, 180))
    #krótkie grube
    screen.blit(sciana_poziom4, (195, 175))
    screen.blit(sciana_poziom4, (615, 175))
    #grube pionowe
    screen.blit(sciana_poziom5, (615, 358))
    screen.blit(sciana_poziom5, (195, 358))
    #pionowe
    screen.blit(sciana_pion1, (715, 545))
    screen.blit(sciana_pion1, (55, 545))
    #skręt w lewo górny
    screen.blit(skret_lewo_png, (650, 40))
    #skręt w prawo górny
    screen.blit(skret_prawo_png, (50, 40))
    #skręt w prawo dolny
    screen.blit(skret_prawo_dol_png, (65, 670))
    #skęt w lewo dolny
    screen.blit(skret_lewo_dol_png, (635, 670))
    #potrójny lewo góra
    screen.blit(potrojny_lewo_gora, (610, 88))
    #potrójny prawo góra
    screen.blit(potrojny_prawo_gora, (70, 88))
    #potrójne nowe
    screen.blit(potrojne_nowe1_png, (215, 40))
    screen.blit(potrojne_nowe2_png, (485, 40))
    #slalomy
    screen.blit(slalom1_png, (190, 645))
    screen.blit(slalom2_png, (475, 645))
    #ściana U
    screen.blit(sciana_u_png, (300, 455))
    #potrójny nowy
    screen.blit(potrojny_nowy_png, (350, 588))

    
    #rysowanie linii i kropek
    num1 = ((950 - 50) // 32)
    num2 = (900 // 30)
    for i in range(len(level2)):
        for j in range(len(level2[i])):
            #małe kropki
            if level2[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            #duże kropki
            if level2[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            #pionowe linie
            if level2[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            #poziome linie
            if level2[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            #skręt z lewej w dół
            if level2[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            #skręt z prawej w dół
            if level2[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            #skręt z prawej w górę
            if level2[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            #skręt z lewej w górę
            if level2[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            #biała linia pozioma
            if level2[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
             #baklazan
            if level2[i][j] == 10:
                screen.blit(baklazan_png1,(j * num2 + ((0.1 * num2) - 5), i * num1 + ((0.1 * num1) - 5)))
            #watermelon
            if level2[i][j] == 11:
                screen.blit(watermelon_png1,(j * num2 + ((0.1 * num2) - 5), i * num1 + ((0.1 * num1) - 5)))
            #bananna
            if level2[i][j] == 12:
                screen.blit(bananna_png1,(j * num2 + ((0.1 * num2) - 5), i * num1 + ((0.1 * num1) - 5)))
    #RIGHT, LEFT, UP, DOWN
    if direction == 0:
        screen.blit(pacman_images[counter // 7], (pacman_x, pacman_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(pacman_images[counter // 7], True, False), (pacman_x, pacman_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 7], 90), (pacman_x, pacman_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(pacman_images[counter // 7], 270), (pacman_x, pacman_y))
    command = 0
    button = Button("Exit", (600, 900))
    button.draw()
    if button.check_clicked():
        command = 1
    return command

#--------------------------------------------#--------------------------------------------

running = True
while running:
    screen.fill("black")
    timer.tick(fps)
    if game:
        menu_command = draw_game() 
        menu_command1 = draw_levels()
        menu_command2 = draw_option()
        menu_command3 = draw_board()
        menu_command4 = draw_difficulty()
        menu_command5 = draw_endgame_screen_viktory()
        screen.fill("black")
        if menu_command or menu_command1 or menu_command2 or menu_command3 or menu_command4 or menu_command5 > 0:
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
                player_circle = pygame.draw.circle(screen,'purple',(center_x,center_y), 15, 2)
                game = draw_board()
                if counter < 19:
                    counter += 1
                    if counter > 3:
                        flicker = False
                else:
                    counter = 0
                    flicker = True
                draw_score()
                if score >= 300:
                    game = draw_endgame_screen_viktory()
                    pygame.display.flip()
                    match menu_command5:
                        case 1:
                            game = draw_board()
                        case 2:
                            game = draw_game()
                        case 3:
                            running - False
                
                
                center_x = pacman_x + 23
                center_y = pacman_y + 24
                pacman_speed = check_fruit(pacman_speed)
                pacman_x, pacman_y = check_fruit2(pacman_x, pacman_y)
                turns_allowed = check_position(center_x, center_y)
                pacman_x, pacman_y = move_pacman(pacman_x, pacman_y)
                score = check_points(score)

                if score >= 50:
                    game = draw_endgame_screen_viktory()
                    pygame.display.flip()
                    match menu_command5:
                        case 1:
                            game = draw_board()
                        case 2:
                            game = draw_game()
                        case 3:
                            running - False

                Emily_images = Emil_images[fremily_number]
                Fred_images = Fre_images[fremily_number]
                Jordan_images = Jorda_images[jordan_number]
                Thanos_images = Thano_images[thanos_number]
                Fred = Ghost(Fred_x, Fred_y, targets[0], ghost_speed, Fred_images, Fred_direction, Fred_box, 0)
                Emily = Ghost(Emily_x, Emily_y, targets[1], ghost_speed, Emily_images, Emily_direction, Emily_box, 1)
                Jordan = Ghost(Jordan_x, Jordan_y, targets[2], ghost_speed, Jordan_images, Jordan_direction, Jordan_box, 2)
                Thanos = Ghost(Thanos_x, Thanos_y, targets[3], ghost_speed, Thanos_images, Thanos_direction, Thanos_box, 3) 
                targets = get_targets(pacman_x,pacman_y,pacman_x,pacman_y,pacman_x,pacman_y,pacman_x,pacman_y)
                fremily_number+=1
                jordan_number+=1
                thanos_number+=1
                if fremily_number >= 7:
                    fremily_number = 0
                if thanos_number >= 12:
                    thanos_number = 0
                if jordan_number >= 6:
                    jordan_number = 0
                Jordan_x, Jordan_y, Jordan_direction = Jordan.move_jordan()
                Fred_x, Fred_y, Fred_direction = Fred.move_fred()
                Emily_x, Emily_y, Emily_direction = Emily.move_emily()
                Thanos_x, Thanos_y, Thanos_direction = Thanos.move_thanos()
                if (player_circle.colliderect(Fred.rect)):
                    pygame.quit()
                    running = False
                if (player_circle.colliderect(Jordan.rect)):
                    pygame.quit()
                    running = False
                if (player_circle.colliderect(Emily.rect)):
                    pygame.quit()
                    running = False
                if (player_circle.colliderect(Thanos.rect)):
                    pygame.quit()
                    running = False
            case 3:
                player_circle = pygame.draw.circle(screen,'purple',(center_x,center_y), 15, 2)
                game = draw_board2()
                if counter < 19:
                    counter += 1
                    if counter > 3:
                        flicker = False
                else:
                    counter = 0
                    flicker = True
                draw_score()

                center_x = pacman_x + 23
                center_y = pacman_y + 24
                pacman_speed = check_fruit(pacman_speed)
                pacman_x, pacman_y = check_fruit2(pacman_x, pacman_y)
                turns_allowed = check_position2(center_x, center_y)
                pacman_x, pacman_y = move_pacman(pacman_x, pacman_y)
                score = check_points2(score)
                if score >= 500:
                    game = draw_endgame_screen_viktory()
                    pygame.display.flip()
                    match menu_command5:
                        case 1:
                            game = draw_board()
                        case 2:
                            game = draw_game()
                        case 3:
                            running - False

                Emily_images = Emil_images[fremily_number]
                Fred_images = Fre_images[fremily_number]
                Jordan_images = Jorda_images[jordan_number]
                Thanos_images = Thano_images[thanos_number]
                Fred = Ghost1(Fred_x, Fred_y, targets[0], ghost_speed, Fred_images, Fred_direction, Fred_box, 0)
                Emily = Ghost1(Emily_x, Emily_y, targets[1], ghost_speed, Emily_images, Emily_direction, Emily_box, 1)
                Jordan = Ghost1(Jordan_x, Jordan_y, targets[2], ghost_speed, Jordan_images, Jordan_direction, Jordan_box, 2)
                Thanos = Ghost1(Thanos_x, Thanos_y, targets[3], ghost_speed, Thanos_images, Thanos_direction, Thanos_box, 3) 
                targets = get_targets(pacman_x,pacman_y,pacman_x,pacman_y,pacman_x,pacman_y,pacman_x,pacman_y)
                fremily_number+=1
                jordan_number+=1
                thanos_number+=1
                if fremily_number >= 7:
                    fremily_number = 0
                if thanos_number >= 12:
                    thanos_number = 0
                if jordan_number >= 6:
                    jordan_number = 0
                Jordan_x, Jordan_y, Jordan_direction = Jordan.move_jordan()
                Fred_x, Fred_y, Fred_direction = Fred.move_fred()
                Emily_x, Emily_y, Emily_direction = Emily.move_emily()
                Thanos_x, Thanos_y, Thanos_direction = Thanos.move_thanos()
                if (player_circle.colliderect(Fred.rect)):
                    pygame.quit()
                    running = False
                if (player_circle.colliderect(Jordan.rect)):
                    pygame.quit()
                    running = False
                if (player_circle.colliderect(Emily.rect)):
                    pygame.quit()
                    running = False
                if (player_circle.colliderect(Thanos.rect)):
                    pygame.quit()
                    running = False
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
                None
        match menu_command4:
            case 1:
                None
            case 2:
                None
            case 3:
                None
            case 4:
                game = draw_option()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction


        
    if direction_command == 0 and turns_allowed[0]:
        direction = 0
    if direction_command == 1 and turns_allowed[1]:
        direction = 1
    if direction_command == 2 and turns_allowed[2]:
        direction = 2
    if direction_command == 3 and turns_allowed[3]:
        direction = 3

    if pacman_x > 900:
        pacman_x = -47
    elif pacman_x < -50:
        pacman_x = 897

    pygame.display.flip()
pygame.quit()