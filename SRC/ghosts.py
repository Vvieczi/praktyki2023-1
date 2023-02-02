import pygame
import sys

pygame.init()

timer = pygame.time.Clock()
WIDTH = 1200
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])


Fred_img = pygame.transform.scale(pygame.image.load('assets/ghosts/Fred.png'), (45,45))
Emily_img = pygame.transform.scale(pygame.image.load('assets/ghosts/Emily.png'), (45,45))
Jessie_img = pygame.transform.scale(pygame.image.load('assets/ghosts/Jessie.png'), (45,45))
Jordan_img = pygame.transform.scale(pygame.image.load('assets/ghosts/Jordan.png'), (45,45))
Thanos_img = pygame.transform.scale(pygame.image.load('assets/ghosts/thanos_ghost_animated.gif'), (45,45))
Dead_ghost_img = pygame.transform.scale(pygame.image.load('assets/ghosts/Dead_ghost.png'), (45,45))

class Ghost():
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 25
        self.center_y = self.y_pos + 25
        self.target = target
        self.speed = speed
        self.img = img
        self.direction = direct
        self.dead = dead
        self.id = id
        self.rect = self.draw()

    def draw(self):
        if True:
            screen.blit(self.img, (self.x_pos, self.y_pos))
            
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect

    



player_x = 156
player_y = 158
direction = 2
Fred_x = 156
Fred_y = 58
Fred_direction = 2
Emily_x = 256
Emily_y = 58
Emily_direction = 2
Jessie_x = 356
Jessie_y = 58
Jessie_direction = 2
Jordan_x = 456
Jordan_y = 58
Jordan_direction = 2
Thanos_x = 556
Thanos_y = 58
Thanos_direction = 2

eaten_ghost = [False, False, False, False, False]
targets = [(player_x,player_y), (player_x,player_y), (player_x,player_y), (player_x,player_y),(player_x,player_y)]

Fred_dead = False
Emily_dead = False
Jessie_dead = False
Jordan_dead = False
Thanos_dead = False

ghost_speed = 2


    
running = True
while running:
    Fred = Ghost(Fred_x, Fred_y, targets[0], ghost_speed, Fred_img, Fred_direction, Fred_dead, 0)
    Emily = Ghost(Emily_x, Emily_y, targets[1], ghost_speed, Emily_img, Emily_direction, Emily_dead, 1)
    Jessie = Ghost(Jessie_x, Jessie_y, targets[2], ghost_speed, Jessie_img, Jessie_direction, Jessie_dead, 2)
    Jordan = Ghost(Jordan_x, Jordan_y, targets[3], ghost_speed, Jordan_img, Jordan_direction, Jordan_dead, 3)
    Thanos = Ghost(Thanos_x, Thanos_y, targets[4], ghost_speed, Thanos_img, Thanos_direction, Thanos_dead, 4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.update()
pygame.quit()        




