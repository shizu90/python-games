import pygame
import cube as c

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = c.cube(pos)
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dir_x = -1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_RIGHT]:
                    self.dir_x = 1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_UP]:
                    self.dir_x = 0
                    self.dir_y = -1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_DOWN]: 
                    self.dir_x = 0
                    self.dir_y = 1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

            for i, c in enumerate(self.body) :
                p = c.pos[:]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0], turn[1])
                    if i == len(self.body)-1:
                        self.turns.pop(p)

                else:
                    if c.dir_x == -1 and c.pos[0] <= 0: 
                        c.pos = (c.rows-1, c.pos[1])
                    elif c.dir_x == 1 and c.pos[0] >= c.rows-1: 
                        c.pos = (0, c.pos[1])
                    elif c.dir_x == 1 and c.pos[1] >= c.rows-1: 
                        c.pos = (0, c.pos[0], 0)
                    elif c.dir_x == -1 and c.pos[1] <= 0: 
                        c.pos = (c.pos[0], c.rows-1)
                    else: 
                        c.move(c.dir_x, c.dir_y)
    def reset(self, pos):
        self.head = c.cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1
    
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dir_x, tail.dir_y

        if dx == 1 and dy == 0:
            self.body.append(c.cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(c.cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(c.cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(c.cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dir_x = dx
        self.body[-1].dir_y = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)