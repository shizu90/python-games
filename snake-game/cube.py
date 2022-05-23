import pygame

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dir_x = 1, dir_y = 0, color = (255, 0 , 0)):
        self.pos = start
        self.dir_x = 1
        self.dir_y = 0
        self.color = color 
    
    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos  = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)

    def draw(self, surface, eyes = False):
        dis = self.w // self.rows 
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2)) 
        if eyes:
            center = dis//2
            radius = 3
            circleMiddle = (i*dis+center-radius, j*dis+8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)