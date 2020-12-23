"""
    VERSÃO 1.0
    - Background
    - Movimentos
    - Skin do personagem
"""

import pygame
pygame.init()

screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Camp test')
x = 500
y = 490
speed = 20
right = True
left = False
open_screen = True

player_R0 = pygame.image.load('player_sprite/player_R0.png')
player_L0 = pygame.image.load('player_sprite/player_L0.png')

while open_screen:
    pygame.time.delay(50)
    command = pygame.key.get_pressed()

    screen.fill(0)

    #  objetos de fundo
    pygame.draw.polygon(screen, (173, 173, 173), ((0, 600), (0, 800), (1500, 800), (1500, 600)), 0)
    pygame.draw.polygon(screen, (255, 204, 0), ((0, 0), (0, 600), (1500, 600), (1500, 0)), 0)

    # movimentação
    # direita
    if command[pygame.K_d]:
        right = True
        left = False
        screen.blit(player_R0, (x - 50, y - 85))
        x += speed
    elif command[pygame.K_d] == 0 and right:
        screen.blit(player_R0, (x - 50, y - 85))

    # esquerda
    if command[pygame.K_a] and command[pygame.K_d] == 0:
        right = False
        left = True
        screen.blit(player_L0, (x - 40, y - 85))
        x -= speed
    elif command[pygame.K_a] == 0 and left:
        screen.blit(player_L0, (x - 50, y - 85))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_screen = False

pygame.quit()
