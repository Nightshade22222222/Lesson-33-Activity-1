import math
import random
import pygame
playerX = 370
playerY = 380
playerX_change = 0
screen = pygame.display.set_mode((800, 500))
background = pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
playerImage = pygame.image.load("ufo.png")
def player(x, y):
    screen.blit(playerImage, (x, y))
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerX_change = -5
            if event.type == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    if playerX >= 740:
        playerX = 740
    player(playerX, playerY)
    pygame.display.update()
pygame.quit()