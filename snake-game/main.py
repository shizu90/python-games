import random
import pygame
import tkinter as tk
from tkinter import messagebox
import snake as s
import cube as c


def drawGrid(w, rows, surface):
    size_Btwn = w // rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + size_Btwn
        y = y + size_Btwn

        pygame.draw.line(surface, (0, 0, 20), (x, 0), (x, w))
        pygame.draw.line(surface, (0, 0, 20), (0, y), (w, y))

def redraw_Window(surface):
    global width, rows, snake, snack
    surface.fill((255,255,255))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def random_Snack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x, y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global width, rows, snake, snack
    width = 500
    rows = 20

    window = pygame.display.set_mode((width, width))

    snake = s.snake((255, 0, 0), (10,10))
    snack = c.cube(random_Snack(rows, snake), color = (0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = c.cube(random_Snack(rows, snake), color = (0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z:z.pos, snake.body[x+1:])):
                print('Score: ', len(snake.body))
                message_box("Game Over", "Try again")
                snake.reset((10,10))
                break
            else:
                break
        redraw_Window(window)
        

main()