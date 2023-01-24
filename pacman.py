import pygame
import sys
pygame.init()
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))
pygame.display.flip()

BLUE = (0, 0, 255)

sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 48)
draw_text = font.render("Menu", sysfont, True, BLUE)
draw_text1 = font.render("Worlds", sysfont, True, BLUE)
fonts = pygame.font.get_fonts()

click = False

def main_menu():
    while True:
        screen.fill((0,0,0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button1 = pygame.Rect(500, 100, 200, 50)
        button2 = pygame.Rect(500, 200, 200, 50)
        screen.blit(draw_text, (550, 20))
        if button1.collidepoint((mouse_x, mouse_y)):
            if click:
                game()
        if button2.collidepoint((mouse_x, mouse_y)):
            if click:
                pass
        pygame.draw.rect(screen, (255, 255, 0), button1)
        pygame.draw.rect(screen, (255, 255, 0), button2)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(draw_text1, (550, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)
main_menu()