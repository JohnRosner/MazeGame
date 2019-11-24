import pygame
import generateMaze
from random import *
pygame.init()

width = 60
height = 40
cellWidth = 8

wallColor = (0,0,0)
pathColor = (255,255,255)
playerColor = (175,0,0)

disWidth = 2 * width * cellWidth + cellWidth
disHeight = 2 * height * cellWidth + cellWidth

window = pygame.display.set_mode((disWidth, disHeight))

pygame.display.set_caption("Maze Game")
run = True

maze = generateMaze.generateMaze(width, height)
#for i in range(0, width):
#    print(maze[i])

playerX = 1
playerY = 1

while run:
    pygame.time.delay(75) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and maze[playerX - 1][playerY]:
        playerX -= 1
    if keys[pygame.K_RIGHT] and maze[playerX + 1][playerY]:
        playerX += 1
    if keys[pygame.K_UP] and maze[playerX][playerY - 1]:
        playerY -= 1
    if keys[pygame.K_DOWN] and maze[playerX][playerY + 1]:
        playerY += 1

    
    for i in range(0, 2 * width + 1):
        for j in range(0, 2 * height + 1):
            if maze[i][j]:
                pygame.draw.rect(window, pathColor, (i * cellWidth, j * cellWidth, cellWidth, cellWidth))
            else:
                pygame.draw.rect(window, wallColor, (i * cellWidth, j * cellWidth, cellWidth, cellWidth))
            
    pygame.draw.rect(window, playerColor, (playerX * cellWidth, playerY * cellWidth, cellWidth, cellWidth))
                
    pygame.display.update()
    
pygame.quit()