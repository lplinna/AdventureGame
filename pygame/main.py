import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (255,0,0)

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
   def draw(self, screen):
      pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
      
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
        self.velx = 4
        self.vely = 4
    def draw(self, screen):
        pygame.draw.circle(screen, (0,0,255), (self.x,self.y), 5)

    def inside_rectangle(self, brectangle):
       top_left = (brectangle.x < self.x + 5) and (brectangle.y < self.y + 5)
       bottom_right = (brectangle.x + brectangle.width > self.x - 5) and (brectangle.y + brectangle.height > self.y - 5)
       return top_left and bottom_right
    
    def collides_brectangle(self, brectangle):
       if self.inside_rectangle(brectangle):
        #print("Inside")
        if self.y > brectangle.y + brectangle.height:
           self.vely = -self.vely
        elif self.y < brectangle.y:
           self.vely = -self.vely
        if self.x < brectangle.x:
           self.velx = -self.velx
        elif self.x > brectangle.x + brectangle.width:
           self.velx = -self.velx
        return True
       else:
          return False

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
testRect = Brectangle(GREEN,WIDTH * 0.9,HEIGHT * 0.2,WIDTH * 0.4,HEIGHT * 0.1)

blocks = []
block_width = WIDTH / 20
block_height = block_width * 0.2
block_spacing = 5
b_x = 0
b_y = 0
for i in range(30):
   b_x += block_width + block_spacing
   if b_x > WIDTH:
      b_x = 0
      b_y += block_height + block_spacing
   blocks.append(Brectangle(GREEN, b_x, b_y, block_width, block_height))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    #draw_rectangle_grid(20,50)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
       testRect.x = max(testRect.x - 8, 0)
    if keys[pygame.K_RIGHT]:
       testRect.x = min(testRect.x + 8, WIDTH - testRect.width)


    playerBall.draw(screen)
    playerBall.update()
    testRect.draw(screen)
    playerBall.collides_brectangle(testRect)

    for block in blocks:
       block.draw(screen)
       if playerBall.collides_brectangle(block):
          blocks.remove(block)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
  
pygame.quit()
sys.exit()