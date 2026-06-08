import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))


#Title and caption
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load ('spaceship.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480


def player():
     screen.blit(playerImg, (playerX, playerY))

#Game Loop
running = True
while running:

    #RGB- Red, Green, Blue
    screen.fill ((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    player()

    pygame.display.update()