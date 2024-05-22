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
  
   def draw(self,screen):
      pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))


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

    def collides_rectangle(self, rectangle):
      if ((rectangle.x+rectangle.width) >= (self.x-5)) and ((rectangle.x) <= (self.x+5)) and ((rectangle.y+rectangle.height) >= (self.y-5)) and (rectangle.y) <= ((self.y+5)):
        return True
      else:
        return False
      
    def bounce_rectangle(self, rectangle):
       if self.collides_rectangle(rectangle):
        if self.x > rectangle.width + rectangle.x:
          self.velx = -self.velx
          self.x = rectangle.width + rectangle.x + 5
        elif self.x < rectangle.x:
          self.velx = -self.velx
          self.x = rectangle.x - 5
        if self.y > rectangle.height + rectangle.y:
          self.vely = -self.vely
          self.y = rectangle.y + rectangle.height + 5
        elif self.y < rectangle.y:
          self.vely = -self.vely
          self.y = rectangle.y - 5

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
testRect = Brectangle(BLACK,30,30,120,20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    #draw_rectangle_grid(20,50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and testRect.x > 0:
       testRect.x -= 5
    if keys[pygame.K_RIGHT] and testRect.x < WIDTH - 120:
       testRect.x += 5

    playerBall.draw(screen)
    playerBall.update()

    testRect.draw(screen)
    playerBall.bounce_rectangle(testRect)


    pygame.display.flip()
    pygame.time.Clock().tick(60)
  
pygame.quit()
sys.exit()