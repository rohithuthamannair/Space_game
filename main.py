import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))


#Title and caption
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load ('spaceship.png')
pygame.display.set_icon(icon)


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB- Red, Green, Blue
    screen.fill ((250, 0, 0))
    pygame.display.update()