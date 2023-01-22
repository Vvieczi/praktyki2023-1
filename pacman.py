import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
pygame.display.set_caption("Pac Man")
run = True
while run:
    timer.tick(fps)
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()