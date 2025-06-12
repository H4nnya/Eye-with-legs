import pygame

pygame.init()
screen = pygame.display.set_mode([1200, 650])
pygame.display.set_caption('MENU')

# acesso as pastas de image
def spriter(folder, image, posx, posy):
    player = pygame.image.load(f'{folder}/{image}.png')
    screen.blit(player, (posx, posy))

#movimento
def move(spriter, lond):
    spriter('player_spriter', f'{spriter}{lond}', x, y)

#menu
def verificar(pos, area):
    px, py = pos
    x1, y1, x2, y2 = area
    return x1 <= px <= x2 and y1 <= py <= y2

play = (455, 300, 730, 390)

ppx = ppy = 200
bpx = bpy = 600
while True:
    png = 0
    side = 'R'
    move = False


    def motion(pic, rl):
        player = pygame.image.load(f'player_spriter/player_{pic}{rl}.png')
        screen.blit(player, (x, y))

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
                    y = 420
                    speed = 15
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
                        motion(side, png)

                        if move and png >= 0:
                            png += 1
                        if png == 5:
                            png = 1
                        if move == False:
                            png = 0

                        if command[pygame.K_d]:
                            side = 'R'
                            move = True
                            x += speed
                        elif command[pygame.K_a]:
                            side = 'L'
                            move = True
                            x -= speed
                        else:
                            move = False
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

