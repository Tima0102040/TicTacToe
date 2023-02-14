import pygame
import sys

pygame.init()
size_block=100
margin=15
width=heigth=size_block*3+margin*4

size_window=(width, heigth)
screen=pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic tac toe")

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
arr=[[0]*3 for i in range (3)]
query=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    for row in range(3):
        for col in range(3):
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, white, (x, y, size_block, size_block))
    pygame.display.update()