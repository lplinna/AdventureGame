import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GREEN = (144,238,144)
DARK_GREEN = (1,50,32)
APPLE = (144,0,0)

grid_size_pixels = 64

    

def make_grid():
    start = []
    for i in range(math.floor(WIDTH / grid_size_pixels)):
        middle = []
        for j in range(math.floor(HEIGHT / grid_size_pixels)):
            middle.append(0)
        start.append(middle)
    return start

main_grid = make_grid()
main_grid[1][1] = 1
main_grid[5][8] = 1


def get_color(x_screen,y_screen):
    x_grid = math.floor(x_screen / grid_size_pixels)
    y_grid = math.floor(y_screen / grid_size_pixels)
    col = main_grid[x_grid % len(main_grid)]
    row = col[y_grid % len(col)]
    if row == 1:
      return APPLE
    else:
      return DARK_GREEN


def draw_snake_grid(screen):
    x = 0
    y = 0
    size = grid_size_pixels
    while y < HEIGHT :
        
        pygame.draw.rect(screen,get_color(x,y),(x,y,size,size))
        
        if x > WIDTH:
            y += grid_size_pixels
            x = 0
        else:
            x += size

running = True
while running:
    for event in pygame.event.get(): ##
          if event.type == pygame.QUIT: ##
              running = False ## 
    screen.fill(LIGHT_GREEN)
    draw_snake_grid(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)