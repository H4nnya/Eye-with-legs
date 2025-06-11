import pygame

pygame.init()
screen = pygame.display.set_mode([1200, 650])
pygame.display.set_caption('MENU')

def spriter(folder, image, posx, posy):
    player = pygame.image.load(f'{folder}/{image}.png')
    return screen.blit(player, (posx, posy))

def verificar(pos, area):
    px, py = pos
    x1, y1, x2, y2 = area
    return x1 <= px <= x2 and y1 <= py <= y2

play = (455, 300, 730, 390)

ppx = ppy = 200
bpx = bpy = 600
while True:
    screen.fill(0)

    pos_mouse = pygame.mouse.get_pos()


    spriter('spriter', 'background', 0, 0)
    pygame.draw.circle(screen, (0, 250, 50), pos_mouse, 10)

    pygame.display.update()
    pygame.time.Clock().tick(60)

    for eventa in pygame.event.get():
        if eventa.type == pygame.QUIT:
            pygame.quit()

        if eventa.type == pygame.MOUSEBUTTONDOWN:
            if eventa.button == 1:
                if verificar(pos_mouse, play):
                    pygame.display.set_caption('Eye with legs')
                    x = 100
                    y = 500
                    speed = 10
                    left = jump = False
                    open_screen = right = True


                    # Sprites do jogador
                    def spriter(image, posx, posy):
                        player = pygame.image.load(f'player_spriter/player_{image}.png')
                        return screen.blit(player, (posx - 100, posy - 100))

                    rond = lond = 0
                    while open_screen:
                        command = pygame.key.get_pressed()
                        pygame.display.update()
                        pygame.time.Clock().tick(30)

                        #  Plano de fundo
                        pygame.draw.polygon(screen, (173, 173, 173), ((0, 600), (0, 800), (1500, 800), (1500, 600)), 0)
                        pygame.draw.polygon(screen, (255, 204, 0), ((0, 0), (0, 600), (1500, 600), (1500, 0)), 0)

                        # colisão do jogador
                        if x > 1150:
                            x -= speed
                        elif x < 50:
                            x += speed
                        if y > 510:
                            y -= 10

                        # movimentação e animação
                        # correr
                        if command[pygame.K_z]:
                            speed = 60
                        else:
                            speed = 20

                        # Direita
                        if command[pygame.K_d] and command[pygame.K_a] == 0 and lond == 0:
                            spriter('R1', x, y)
                            x += speed
                            lond = 1
                            right = True
                            left = False
                        elif command[pygame.K_d] and lond == 1:
                            spriter('R2', x, y)
                            x += speed
                            lond = 2
                        elif command[pygame.K_d] and lond == 2:
                            spriter('R3', x, y)
                            x += speed
                            lond = 3
                        elif command[pygame.K_d] and lond == 3:
                            spriter('R4', x, y)
                            x += speed
                            lond = 4
                        elif command[pygame.K_d] and lond == 4:
                            spriter('R5', x, y)
                            x += speed
                            lond = 5
                        elif command[pygame.K_d] and lond == 5:
                            spriter('R6', x, y)
                            x += speed
                            lond = 1
                        elif command[pygame.K_d] == 0 and right:
                            spriter('R0', x, y)  # screen.blit(player_R0, (x - 100, y - 100))
                            lond = 0
                        else:
                            lond = 0

                        # Esquerda
                        if command[pygame.K_a] and command[pygame.K_d] == 0 and rond == 0:
                            right = False
                            left = True
                            spriter('L1', x, y)
                            x -= speed
                            rond = 1
                        elif command[pygame.K_a] and rond == 1:
                            spriter('L2', x, y)
                            x -= speed
                            rond = 2
                        elif command[pygame.K_a] and rond == 2:
                            spriter('L3', x, y)
                            x -= speed
                            rond = 3
                        elif command[pygame.K_a] and rond == 3:
                            spriter('L4', x, y)
                            x -= speed
                            rond = 4
                        elif command[pygame.K_a] and rond == 4:
                            spriter('L5', x, y)
                            x -= speed
                            rond = 5
                        elif command[pygame.K_a] and rond == 5:
                            spriter('L6', x, y)
                            x -= speed
                            rond = 1
                        elif command[pygame.K_a] == 0 and left:
                            spriter('L0', x, y)
                            rond = 0
                        else:
                            rond = 0

                        # pular
                        if y <= 400:
                            jump = False
                            y += 30
                        elif command[pygame.K_SPACE] and y >= 500:
                            jump = True

                        if jump:
                            y -= 20
                        else:
                            jump = False
                            y += 7

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                
