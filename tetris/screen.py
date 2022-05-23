import globalvars
import pygame


def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

def draw_grid(surface, row, col):
    sx = globalvars.top_left_x
    sy = globalvars.top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + globalvars.play_window_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + globalvars.play_window_height))  # vertical lines

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('Arial', size, bold=True)
    label = font.render(text, 1, color)
 
    surface.blit(label, (globalvars.top_left_x + globalvars.play_window_width/2 - (label.get_width() / 2), 
    globalvars.top_left_y + globalvars.play_window_height/2 - label.get_height()/2))


def draw_window(surface, grid):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('Arial', 60)
    label = font.render('TETRIS', 1, (255,255,255))
 
    surface.blit(label, (globalvars.top_left_x + globalvars.play_window_width / 2 - (label.get_width() / 2), 30))
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (globalvars.top_left_x + j* 30, globalvars.top_left_y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (globalvars.top_left_x, globalvars.top_left_y, globalvars.play_window_width, globalvars.play_window_height), 5)
    # pygame.display.update()
 