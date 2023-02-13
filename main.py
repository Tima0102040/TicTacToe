import pygame
import sys

def check_win (mas, sign) :
    for row in mas:
        if row.count (sign) == 3:
            return sign
    for col in range (3):
        if mas [0][col]==sign and mas [1][col]==sign and mas [2][col]== sign :
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    return False


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