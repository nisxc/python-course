import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render('Welcome to pygame', True, (255, 255, 255))
screen.blit(text, ((width - text.get_width())) //
            2, (height - text.get_height()))
pygame.display.flip()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT\
            or e.type == pygame.MOUSEBUTTONUP\
                or e.type == pygame.KEYUP:
            run = False
