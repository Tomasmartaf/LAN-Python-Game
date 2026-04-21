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

# socket věci #
# input pro ip a port serveru/druhy hrac#
HOST = ''
PORT = 0
while HOST == '' or PORT == 0:
    HOST = input("Zadej ip serveru:")
    PORT = int(input("Zadej port serveru:"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((HOST, PORT))

# pygame hovna #
pg.init()
screen = pg.display.set_mode((sirkaHry, vyskaHry))
screen.fill('grey50')
pg.display.set_caption("Spoj 4")
clock = pg.time.Clock()

# SURFACE PRO TEST #
bomba_surface = pg.Surface((velikostSurface1_x, velikostSurface1_y))
bomba_surface.fill('azure')

while True:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(bomba_surface,(prostredHry_x,prostredHry_y-velikostSurface1_y))

    pg.display.update()
    clock.tick(60) #framerate hodin
