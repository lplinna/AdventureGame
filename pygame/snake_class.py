
class Snake:
    '''
    Constructor - give the Snake a variable called points that is an empty list.
    '''
    def __init__(self):
        self.points = []
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

    '''
    def draw(self, grid):
        for point in self.points:
                grid[point[0]][point[1]] = 2
            
    '''
    Move the snake one step in one direction.

    '''
    def move(self, grid):
        head = self.points[len(self.points)-1]
        tail = self.points.pop(0)
        self.add_point(head[0]+1,head[1])

        # Drawing part
        grid[tail[0]][tail[1]] = 0
        self.draw(grid)
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