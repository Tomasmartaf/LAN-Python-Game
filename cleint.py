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
# input for ip and connection to the second player/server #
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
screen.fill('grey50')
pg.display.set_caption("Spoj 4")
clock = pg.time.Clock()

# Proměnné pro game ui # 
pocetCtverecku = 0
size = 50
space = 0
spacing = size + 50
surfaceBlockSize_x = size
surfaceBlockSize_y = size
surface = []

for i in range(10):
    surface.append(pg.Surface((surfaceBlockSize_x, surfaceBlockSize_y)))

# Surface na testing #
bomba_surface = pg.Surface((velikostSurface1_x, velikostSurface1_y))
bomba_surface.fill('azure')


def mouseClick():
    mouse_pozice = pg.mouse.get_pos()
    if mouse_pozice[0] > ctverecek_x and mouse_pozice[1] > ctverecek_y:
        if mouse_pozice[0] < (ctverecek_x + velikostSurface1_x) and mouse_pozice[1] < (ctverecek_y + velikostSurface1_y):
            print('tlacitko i guess')

while True:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseClick()

    ctverecek_x = int(prostredHry_x)
    ctverecek_y = int(prostredHry_y-velikostSurface1_y)
    screen.blit(bomba_surface,(ctverecek_x, ctverecek_y))

    if pocetCtverecku < 3:
        space += spacing
        screen.blit(surface.__getitem__(pocetCtverecku),(velikostSurface1_x + space, velikostSurface1_y))
    pocetCtverecku += 1

    pg.display.update()
    clock.tick(60) #framerate hodin
