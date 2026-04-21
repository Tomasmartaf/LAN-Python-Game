import socket
import sys
import pygame

# Pygame promenne
sirkaHry = 1280
vyskaHry = 720
prostredHry_x = sirkaHry/2
prostredHry_y = vyskaHry/2
velikostSurface1_x = 50
velikostSurface1_y = 50

# základní věci pro pygame #
pygame.init()
screen = pygame.display.set_mode((sirkaHry, vyskaHry))
screen.fill('grey50')
pygame.display.set_caption("Spoj 4") # jmeno okna 
clock = pygame.time.Clock() # clock objekt

# SURFACE PRO TEST, TODO#
bomba_surface = pygame.Surface((velikostSurface1_x, velikostSurface1_y))
bomba_surface.fill('azure')

HOST = '192.168.0.170'
PORT = 6767
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((HOST, PORT))

while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bomba_surface,(prostredHry_x,prostredHry_y-velikostSurface1_y))

    pygame.display.update()
    clock.tick(60) #framerate jak casto ticknout hodinami
