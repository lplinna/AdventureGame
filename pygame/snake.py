import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GREEN = (144,238,144)
DARK_GREEN = (1,50,32)
APPLE = (144,0,0)

grid_size_pixels = 32
def draw_snake_grid(screen):
    x = 0
    y = 0
    size = 32
    while y < HEIGHT:
        pygame.draw.rect(screen,DARK_GREEN,(x,y,size,size))
        
        if x > WIDTH:
            y += 32
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