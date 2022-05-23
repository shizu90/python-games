import pygame
import random
import shapes
import pieces
import screen
import globalvars

pygame.font.init()
 

 

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
 
 


 
 

 
 
def clear_rows(grid, locked):
 
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
 
def main():
    global grid
 
    locked_positions = {}  
    grid = screen.create_grid(locked_positions)
 
    change_piece = False
    run = True
    current_piece = shapes.get_shape()
    next_piece = shapes.get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
 
    while run:
        fall_speed = 0.27
 
        grid = screen.create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
 
        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (shapes.valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not shapes.valid_space(current_piece, grid):
                        current_piece.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not shapes.valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not shapes.valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not shapes.valid_space(current_piece, grid):
                        current_piece.y -= 1
 
                if event.key == pygame.K_SPACE:
                   while shapes.valid_space(current_piece, grid):
                       current_piece.y += 1
                   current_piece.y -= 1
                   print(shapes.convert_shape_format(current_piece))
 
        shape_pos = shapes.convert_shape_format(current_piece)
 
        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
 
        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = shapes.get_shape()
            change_piece = False
 
            # call four times to check for multiple clear rows
            clear_rows(grid, locked_positions)
 
        screen.draw_window(win, grid)
        shapes.draw_next_shape(next_piece, win)
        pygame.display.update()
 
        # Check if user lost
        if check_lost(locked_positions):
            run = False
 
    screen.draw_text_middle("You Lost", 40, (255,255,255), win)
    pygame.display.update()
    pygame.time.delay(2000)
 
 
def main_menu():
    run = True
    while run:
        win.fill((0,0,0))
        screen.draw_text_middle('Press any key to begin.', 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()
 
 
win = pygame.display.set_mode((globalvars.screen_width, globalvars.screen_height))
pygame.display.set_caption('Tetris')
 
main_menu()  # start game