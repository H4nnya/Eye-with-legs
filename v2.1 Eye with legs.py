"""
    VERSÃO 2.1
    - Animação de movimentos
    - colisão
"""

import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption('Eye with legs')
x = 100
y = 510
speed = 20
left = False
open_screen = right = True

# Sprites do jogador
def player_spriter(image, posx, posy):
    player = pygame.image.load(f'player_spriter/player_{image}.png')
    return screen.blit(player, (posx - 100, posy - 100))


rond = lond = 0

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
        player_spriter('R1', x, y)
        x += speed
        lond = 1
        right = True
        left = False
    elif command[pygame.K_d] and lond == 1:
        player_spriter('R2', x, y)
        x += speed
        lond = 2
    elif command[pygame.K_d] and lond == 2:
        player_spriter('R3', x, y)
        x += speed
        lond = 3
    elif command[pygame.K_d] and lond == 3:
        player_spriter('R4', x, y)
        x += speed
        lond = 4
    elif command[pygame.K_d] and lond == 4:
        player_spriter('R5', x, y)
        x += speed
        lond = 5
    elif command[pygame.K_d] and lond == 5:
        player_spriter('R6', x, y)
        x += speed
        lond = 1
    elif command[pygame.K_d] == 0 and right:
        player_spriter('R0', x, y) #screen.blit(player_R0, (x - 100, y - 100))
        lond = 0
    else:
        lond = 0

    # -Esquerda
    if command[pygame.K_a] and command[pygame.K_d] == 0 and rond == 0:
        right = False
        left = True
        player_spriter('L1', x, y)
        x -= speed
        rond = 1
    elif command[pygame.K_a] and rond == 1:
        player_spriter('L2', x, y)
        x -= speed
        rond = 2
    elif command[pygame.K_a] and rond == 2:
        player_spriter('L3', x, y)
        x -= speed
        rond = 3
    elif command[pygame.K_a] and rond == 3:
        player_spriter('L4', x, y)
        x -= speed
        rond = 4
    elif command[pygame.K_a] and rond == 4:
        player_spriter('L5', x, y)
        x -= speed
        rond = 5
    elif command[pygame.K_a] and rond == 5:
        player_spriter('L6', x, y)
        x -= speed
        rond = 1
    elif command[pygame.K_a] == 0 and left:
        player_spriter('L0', x, y)
        rond = 0
    else:
        rond = 0

    # colisão do jogador
    if x > 1200:
        x -= speed
    if x < 50:
        x += speed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_screen = False

pygame.quit()
