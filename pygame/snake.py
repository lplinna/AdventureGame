import pygame
import sys
import math
from snake_class import Snake

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GREEN = (144,238,144)
DARK_GREEN = (1,50,32)
APPLE = (144,0,0)

grid_size_pixels = 64

'''
Create the game snake.
'''
game_snake = Snake()
game_snake.add_point_colliding(0,5)
game_snake.add_point_colliding(1,5)
game_snake.add_point_colliding(2,5)

    

def make_grid():
    start = []
    for i in range(math.floor(WIDTH / grid_size_pixels)):
        middle = []
        for j in range(math.floor(HEIGHT / grid_size_pixels)):
            middle.append(0)
        start.append(middle)
    return start

'''
Create the game grid.
'''
main_grid = make_grid()
main_grid[1][1] = 1
main_grid[5][8] = 1
game_snake.draw(main_grid)
print(main_grid)




def get_color(x_screen,y_screen):
    x_grid = math.floor(x_screen / grid_size_pixels)
    y_grid = math.floor(y_screen / grid_size_pixels)
    x_clamped = max(0, min(x_grid,len(main_grid) - 1))
    col = main_grid[x_clamped]
    y_clamped = max(0, min(y_grid,len(col) - 1))
    row = col[y_clamped]
    if row == 1: # APPLE
        return APPLE
    elif row == 2: # SNAKE
        return LIGHT_GREEN
    else: # GRID
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
time = 0
while running:
    time += 1
    if time % 20 == 0:
        game_snake.move(main_grid)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        game_snake.dir = "left"
    elif key[pygame.K_RIGHT]:
        game_snake.dir = "right"
    elif key[pygame.K_UP]:
        game_snake.dir = "up"
    elif key[pygame.K_DOWN]:
        game_snake.dir = "down"

    for event in pygame.event.get(): ##
          if event.type == pygame.QUIT: ##
              running = False ## 
    screen.fill(DARK_GREEN)
    draw_snake_grid(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)