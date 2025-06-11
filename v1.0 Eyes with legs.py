"""
    VERSÃO 1.0
    - Background
    - Movimentos
    - Skin do personagem
"""

import pygame
pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Camp test')
x = 500
y = 520
right = True
left = False
speed = 20
open_screen = True

def player_spriter(image, posx, posy):
    player = pygame.image.load(f'player_spriter/player_{image}.png')
    return screen.blit(player, (posx - 100, posy - 100))

while open_screen:
    pygame.time.Clock().tick(60)
    command = pygame.key.get_pressed()

    screen.fill(0)

    #  objetos de fundo
    pygame.draw.polygon(screen, (173, 173, 173), ((0, 600), (0, 800), (1500, 800), (1500, 600)), 0)
    pygame.draw.polygon(screen, (255, 204, 0), ((0, 0), (0, 600), (1500, 600), (1500, 0)), 0)

    # movimentação
    # direita
    if command[pygame.K_d]:
        player_spriter('R1', x, y)
        x += speed
        right = True
        left = False
    elif command[pygame.K_d] == 0 and right:
        player_spriter('R0', x, y)

    # esquerda
    if command[pygame.K_a] and command[pygame.K_d] == 0:
        player_spriter('L1', x, y)
        x -= speed
        right = False
        left = True
    elif command[pygame.K_a] == 0 and left:
        player_spriter('L0', x, y)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_screen = False

pygame.quit()
