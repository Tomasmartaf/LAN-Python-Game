import socket
import sys
import pygame as pg

# Pygame proměnné # 
sirkaHry = 1280
vyskaHry = 720
prostredHry_x = sirkaHry/2
prostredHry_y = vyskaHry/2
velikostSurface1_x = 50
velikostSurface1_y = 50

# socket connection setup #
HOST = ''
PORT = 0
while HOST == '' or PORT == 0:
    HOST = input("Zadej ip serveru:")
    PORT = int(input("Zadej port serveru:"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((HOST, PORT))

# pygame setup #
pg.init()
screen = pg.display.set_mode((sirkaHry, vyskaHry))
pg.display.set_caption("Spoj 4")
clock = pg.time.Clock()

# Proměnné pro game ui # 
pocetCtverecku = 10
size = 50
spacing = size + 50
surfaceBlockSize_x = size
surfaceBlockSize_y = size
surface = []
blockSouradnice_x = []
blockSouradnice_y = []
    
for i in range(10):
    surface.append(pg.Surface((surfaceBlockSize_x, surfaceBlockSize_y)))

def mouseClick():
    mouse_pozice = pg.mouse.get_pos()
    for i in range (pocetCtverecku):
        if mouse_pozice[0] > blockSouradnice_x[i] and mouse_pozice[1] > blockSouradnice_y[i]:
            if mouse_pozice[0] < (blockSouradnice_x[i] + velikostSurface1_x) and mouse_pozice[1] < (blockSouradnice_y[i] + velikostSurface1_y):
                print('tlacitko i guess')

while True:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseClick()

    screen.fill('grey50')
    
    # kresleni 1. rady, test #
    space = 0
    for i in range(pocetCtverecku):
        space += spacing
        block_x = velikostSurface1_x + space
        block_y = velikostSurface1_y
        blockSouradnice_x.append(block_x)
        blockSouradnice_y.append(block_y)
        screen.blit(surface[i],(block_x, block_y))

    pg.display.update()
    clock.tick(60) #framerate hodin
