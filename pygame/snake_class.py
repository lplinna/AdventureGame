
class Snake:
    '''
    Constructor - give the Snake a variable called points that is an empty list.
    '''
    def __init__(self):
        self.points = []
        self.dir = "up"
        self.dead = False
        pass
    
    '''
    Add a point to the snake.
    '''
    def add_point(self, x, y):
        self.points.append((x,y))
    
    '''
    Add a point to the snake ONLY IF it won't collide with existing points.
    Otherwise, shout something
    '''
    def add_point_colliding(self, x, y):
        new_point = (x,y)
        if new_point in self.points:
           print("Colliding")
           self.dead = True
        else:
           self.points.append(new_point)

    '''
    Determine if the snake is colliding with itself
    '''
    def is_colliding(self):
        for i in range(len(self.points)):
            for o in range(len(self.points)):
                 if self.points[i] == self.points[o] and i != o:
                    return True
        return False
    
    '''
    Draw the snake on the game grid.

    
    len(main_grid) // How many columns
    len(main_grid[0]) // How many rows



    '''

    def draw(self, grid):
        for point in self.points:
                if point[0] > -1 and point[1] > -1 and point[0] <  len(grid) and point[1] < len(grid[0]):
                    grid[point[0]][point[1]] = 2
                
                #self.draw_snake_point_smart(grid,point,2)

    '''
    def draw_snake_point_smart(self, grid, point, value):
        looped_x = point[0] % len(grid)
        looped_y = point[1] % len(grid[0])
        grid[looped_x][looped_y] = value
    '''


    '''
    Move the snake one step in one direction.
    IN THE FUTURE:
    Grow the snake if apple is eatenz

    '''
    def move(self, grid):
        head = self.points[len(self.points)-1]
        tail = self.points.pop(0)

        # Moving part
        walk_direction = [0,0]
        if self.dir == "right":
            walk_direction = [1,0]
        elif self.dir == "left":
            walk_direction = [-1,0]
        elif self.dir == "up":
            walk_direction = [0,-1]
        elif self.dir == "down":
            walk_direction = [0,1]
        new_snake_head = [head[0] + walk_direction[0], head[1] + walk_direction[1]]

        if new_snake_head[0] > -1 and new_snake_head[1] > -1 and new_snake_head[0] <  len(grid) and new_snake_head[1] < len(grid[0]):
            if grid[new_snake_head[0]][new_snake_head[1]] == 1:
                print("Apple eaten")
                self.points.append(tail)
        
        self.add_point_colliding(new_snake_head[0], new_snake_head[1])

                
        # Drawing part
        self.draw(grid)

        if tail[0] > -1 and tail[1] > -1 and tail[0] <  len(grid) and tail[1] < len(grid[0]):
            grid[tail[0]][tail[1]] = 0
        print(self.points)


'''
s = Snake()
s.add_point(3,0)
s.add_point(4,0)
s.add_point(5,0)
s.add_point(5,1)
s.add_point(5,2)
s.add_point(4,2)
s.add_point(3,2)
s.add_point(3,1)
s.add_point(3,0)
print(s.points)
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
s.move()
'''