import socket
import sys
import pygame as pg

# Pygame variables # 
width = 300
height = 300
sizeSurface1_x = 50
sizeSurface1_y = 50
# variables for game ui # 
size = 50
spacing = 80
blockSize_x = size
blockSize_y = size
numberOfBlocks1 = 3
surfaceList = []
blockCord_x = []
blockCord_y = []
blockCord2_x = []
blockCord2_y = []
blockCord3_x = []
blockCord3_y = []
gameStateList = [[0,0,0],[0,0,0],[0,0,0]]
isPlaying = True

# socket connection setup #

HOST = '192.168.0.128'
PORT = 0
while HOST == '' or PORT == 0:
    HOST = input("Zadej ip serveru:")
    PORT = int(input("Zadej port serveru:"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

pg.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Tic Tac Toe")
clock = pg.time.Clock()

for i in range(10):
    surfaceList.append(pg.Surface((blockSize_x, blockSize_y)))

def mouseClick():
    if isPlaying == False:
        print("Not your turn now !")
    else:
        mouse_pozice = pg.mouse.get_pos()
        for i in range(numberOfBlocks1):
            if mouse_pozice[0] > blockCord_x[i] and mouse_pozice[1] > blockCord_y[i]:
                if mouse_pozice[0] < (blockCord_x[i] + blockSize_x) and mouse_pozice[1] < (blockCord_y[i] + blockSize_y):
                    gameStateList[0][i] = 2
                    print(gameStateList)

        for i in range(numberOfBlocks1):
            if mouse_pozice[0] > blockCord2_x[i] and mouse_pozice[1] > blockCord2_y[i]:
                if mouse_pozice[0] < (blockCord2_x[i] + blockSize_x) and mouse_pozice[1] < (blockCord2_y[i] + blockSize_y):
                    gameStateList[1][i] = 2
                    print(gameStateList)

        for i in range(numberOfBlocks1):
            if mouse_pozice[0] > blockCord3_x[i] and mouse_pozice[1] > blockCord3_y[i]:
                if mouse_pozice[0] < (blockCord3_x[i] + blockSize_x) and mouse_pozice[1] < (blockCord3_y[i] + blockSize_y):
                    gameStateList[2][i] = 2
                    print(gameStateList)
    
# calculation for coordinates of blocks for the 3x3 #
space = 0
for i in range(numberOfBlocks1):
    block_x = sizeSurface1_x + space
    block_y = sizeSurface1_y
    blockCord_x.append(block_x)
    blockCord_y.append(block_y)
    space += spacing

space2 = 0
for i in range(numberOfBlocks1):
    block2_x = sizeSurface1_x + space2
    block2_y = sizeSurface1_y + size + 20
    blockCord2_x.append(block2_x)
    blockCord2_y.append(block2_y)
    space2 += spacing

space3 = 0
for i in range(numberOfBlocks1):
    block3_x = sizeSurface1_x + space3
    block3_y = sizeSurface1_y + size + 90 
    blockCord3_x.append(block3_x)
    blockCord3_y.append(block3_y)
    space3 += spacing


while True:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseClick()

    screen.fill('white')

    for i in range(numberOfBlocks1):
        if (gameStateList[0][i] == 2):
            surfaceList[i].fill('blue')
        elif(gameStateList[0][i]==0):
            surfaceList[i].fill('grey')
    
        screen.blit(surfaceList[i],(blockCord_x[i], blockCord_y[i]))

    for i in range(numberOfBlocks1):
        if (gameStateList[1][i] == 2):
            surfaceList[i+numberOfBlocks1].fill('blue')
        elif(gameStateList[1][i]==0):
            surfaceList[i+numberOfBlocks1].fill('grey')

        screen.blit(surfaceList[i+numberOfBlocks1],(blockCord2_x[i], blockCord2_y[i]))

    for i in range(numberOfBlocks1):
        if (gameStateList[2][i] == 2):
            surfaceList[i+numberOfBlocks1].fill('blue')
        elif(gameStateList[2][i]==0):
            surfaceList[i+numberOfBlocks1].fill('grey')

        screen.blit(surfaceList[i+numberOfBlocks1],(blockCord3_x[i], blockCord3_y[i]))
 
    pg.display.update()
    clock.tick(60)
