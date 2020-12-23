"""
    VERSÃO 2.0
    - Animação de movimentos
    - colisão
"""

import pygame
pygame.init()

screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Eye with legs')
x = 100
y = 510
speed = 20
left = False
open_screen = right = True

# Sprites do jogador
# -Direita
player_R0 = pygame.image.load('player_sprite/player_R0.png')
player_R1 = pygame.image.load('player_sprite/player_R1.png')
player_R2 = pygame.image.load('player_sprite/player_R2.png')
player_R3 = pygame.image.load('player_sprite/player_R3.png')
player_R4 = pygame.image.load('player_sprite/player_R4.png')
player_R5 = pygame.image.load('player_sprite/player_R5.png')
player_R6 = pygame.image.load('player_sprite/player_R6.png')
rond = 0

# -Esquerda
player_L0 = pygame.image.load('player_sprite/player_L0.png')
player_L1 = pygame.image.load('player_sprite/player_L1.png')
player_L2 = pygame.image.load('player_sprite/player_L2.png')
player_L3 = pygame.image.load('player_sprite/player_L3.png')
player_L4 = pygame.image.load('player_sprite/player_L4.png')
player_L5 = pygame.image.load('player_sprite/player_L5.png')
player_L6 = pygame.image.load('player_sprite/player_L6.png')
lond = 0

while open_screen:
    pygame.time.delay(50)
    command = pygame.key.get_pressed()
    screen.fill(0)

    #  Plano de fundo
    pygame.draw.polygon(screen, (173, 173, 173), ((0, 600), (0, 800), (1500, 800), (1500, 600)), 0)
    pygame.draw.polygon(screen, (255, 204, 0), ((0, 0), (0, 600), (1500, 600), (1500, 0)), 0)

    # movimentação e animação
    # -Direita
    if command[pygame.K_d] and command[pygame.K_a] == 0 and lond == 0:
        screen.blit(player_R1, (x - 100, y - 100))
        x += speed
        lond = 1
        right = True
        left = False
    elif command[pygame.K_d] and lond == 1:
        screen.blit(player_R2, (x - 100, y - 100))
        x += speed
        lond = 2
    elif command[pygame.K_d] and lond == 2:
        screen.blit(player_R3, (x - 100, y - 100))
        x += speed
        lond = 3
    elif command[pygame.K_d] and lond == 3:
        screen.blit(player_R4, (x - 100, y - 100))
        x += speed
        lond = 4
    elif command[pygame.K_d] and lond == 4:
        screen.blit(player_R5, (x - 100, y - 100))
        x += speed
        lond = 5
    elif command[pygame.K_d] and lond == 5:
        screen.blit(player_R6, (x - 100, y - 100))
        x += speed
        lond = 1
    elif command[pygame.K_d] == 0 and right:
        screen.blit(player_R0, (x - 100, y - 100))
        lond = 0
    else:
        lond = 0

    # -Esquerda
    if command[pygame.K_a] and command[pygame.K_d] == 0 and rond == 0:
        right = False
        left = True
        screen.blit(player_L1, (x - 100, y - 100))
        x -= speed
        rond = 1
    elif command[pygame.K_a] and rond == 1:
        screen.blit(player_L2, (x - 100, y - 100))
        x -= speed
        rond = 2
    elif command[pygame.K_a] and rond == 2:
        screen.blit(player_L3, (x - 100, y - 100))
        x -= speed
        rond = 3
    elif command[pygame.K_a] and rond == 3:
        screen.blit(player_L4, (x - 100, y - 100))
        x -= speed
        rond = 4
    elif command[pygame.K_a] and rond == 4:
        screen.blit(player_L5, (x - 100, y - 100))
        x -= speed
        rond = 5
    elif command[pygame.K_a] and rond == 5:
        screen.blit(player_L6, (x - 100, y - 100))
        x -= speed
        rond = 1
    elif command[pygame.K_a] == 0 and left:
        screen.blit(player_L0, (x - 100, y - 100))
        rond = 0
    else:
        rond = 0

    # colisão do jogador
    if x > 1450:
        x -= speed
    if x < 50:
        x += speed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_screen = False

pygame.quit()
