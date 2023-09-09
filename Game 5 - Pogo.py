import pygame
from sys import exit

pygame.init()

height = 400
width = 800

screen = pygame.display.set_mode((width, height))

background = pygame.surface.Surface((800, 400))

player1 = pygame.surface.Surface((10, 50))
player1_rect = player1.get_rect(midbottom=(20, 200))
player1.fill('white')
player2 = pygame.surface.Surface((10, 50))
player2_rect = player2.get_rect(midbottom=(780, 200))
player2.fill('white')
clock = pygame.time.Clock()

speed_y = 2
speed_x = 4
x = 200
y = 200


points1 = 0
points2 = 0
font = pygame.font.Font('../Assets/font/Pixeltype.ttf', 100)
points = font.render(f'{points1} - {points2}', False, 'white')
points_rect = points.get_rect(midbottom=(400, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(player1, player1_rect)
    screen.blit(player2, player2_rect)
    screen.blit(points, points_rect)
    ball = pygame.draw.circle(screen, 'red', (x, y), 5, 10)

    if x > 800:
        points1 += 1
        x = 400
        y = 200
        points = font.render(f'{points1} - {points2}', False, 'white')
    if ball.x < 0:
        points2 += 1
        x = 400
        y = 200
        points = font.render(f'{points1} - {points2}', False, 'white')

    x += speed_x
    y += speed_y

    if ball.y > 400:
        speed_y = -2
    if ball.y < 0:
        speed_y = 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_rect.bottom -= 4
    if keys[pygame.K_DOWN]:
        player2_rect.bottom += 4
    if keys[pygame.K_w]:
        player1_rect.bottom -= 4
    if keys[pygame.K_s]:
        player1_rect.bottom += 4

    if ball.colliderect(player2_rect):
        speed_x = -4
    if ball.colliderect(player1_rect):
        speed_x = 4

    pygame.display.update()
    clock.tick(60)
