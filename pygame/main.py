import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)

def draw_rectangle_grid(repeat, distance):
    x = 30
    y = 30
    wide = 80
    long = 80
    while repeat > 0:
        pygame.draw.rect(screen,BLACK,(x,y,wide,long))
        repeat -= 1
        x += wide + distance
        if WIDTH - x <= distance:
            y += long + distance
            x = 30

class Brectangle:
   def __init__(self,color,x,y,width,height):
      self.color = color
      self.x = x
      self.y = y
      self.width = width
      self.height = height
   # Draw
   # Collision
   pass

class Paddle(Brectangle):
   #
   #
   #
   pass

class Block(Brectangle):
   #
   #
   #
   pass


class Ball:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.velx = 3
        self.vely = 3

    def draw(self, screen):
        pygame.draw.circle(screen, (0,0,255), (self.x,self.y), 5)
    def update(self):
        self.x += self.velx
        self.y += self.vely
        if self.y >= HEIGHT - 5:
          self.vely = -self.vely
        elif self.y <= 5:
          self.vely = -self.vely
        elif self.x >= WIDTH - 5:
          self.velx = -self.velx
        elif self.x <= 5:
          self.velx = -self.velx


playerBall = Ball()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    draw_rectangle_grid(20,50)

    playerBall.draw(screen)
    playerBall.update()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
  
pygame.quit()
sys.exit()