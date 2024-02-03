import pygame
from random import *


pygame.init()
size = 700
sc_size = 700, 700
cell_size = 50
v = 5

screen = pygame.display.set_mode(sc_size)
timer = pygame.time.Clock()
running = True
point_counter = 0

le = 1
x, y = randrange(cell_size, size - cell_size, cell_size), randrange(cell_size, size - cell_size, cell_size)
dx, dy = 0, 0
snake = [(x, y)]
point = randrange(cell_size, size - cell_size, cell_size), randrange(cell_size, size - cell_size, cell_size)

point_colors = ['#D87093', '#755D9A', '#009B76', '#F984E5', '#ABCDEF', '#6A5ACD', '#FC0FC0', '#08E8DE', '#7B68EE']
point_color = choice(point_colors)
snake_color = choice(point_colors)

screen_color = '#003153'
key = pygame.key.get_pressed()


while running:
    screen.fill(screen_color)
    fontObj = pygame.font.Font(None, 50)
    textSurfaceObj = fontObj.render(str(point_counter), True, 'white')
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (350, 50)

    screen.blit(textSurfaceObj, textRectObj)
    [pygame.draw.rect(screen, snake_color, (i, j, cell_size, cell_size)) for i, j in snake]
    pygame.draw.rect(screen, point_color, (*point, cell_size, cell_size))
    x += dx * cell_size
    y += dy * cell_size
    snake.append((x, y))
    snake = snake[-le:]
    if snake[-1] == point:
        point_counter += 1
        snake_color = point_color
        point_color = choice(point_colors)
        point = randrange(cell_size, size - cell_size, cell_size), randrange(cell_size, size - cell_size, cell_size)
        v += 1
        le += 1
    if x < 0 or y < 0 or x > size - cell_size or y > size - cell_size:
        point_counter = 0
        le = 1
        v = 5
        x, y = randrange(0, size, cell_size), randrange(0, size, cell_size)
        snake = [(x, y)]


    key = pygame.key.get_pressed()

    if key[pygame.K_DOWN]:
        dx, dy = 0, 1
    if key[pygame.K_UP]:
        dx, dy = 0, -1
    if key[pygame.K_LEFT]:
        dx, dy = -1, 0
    if key[pygame.K_RIGHT]:
        dx, dy = 1, 0
    if key[pygame.K_SPACE]:
        dx, dy = 0, 0


    pygame.display.flip()
    timer.tick(v)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()