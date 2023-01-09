# from tkinter import *
#
# window = Tk()
# window.geometry("500x500")
# window.title("WELCOME TO SUDOKU")
# window.mainloop()

import pygame
from generator import grid
from main import solve,print_board

WIDTH = 550

bg_color = (255, 255, 255)
grid_ele_color = (170, 74, 68)
blue = (0, 0, 128)
green = (10, 255, 60)
button = 0

pygame.init()
win = pygame.display.set_mode(size=(WIDTH, WIDTH))
win.fill(bg_color)
myfont = pygame.font.SysFont('Comic Sans MS', 35)
pygame.display.set_caption("SUDOKU")

text3 = myfont.render("click anywhere.....", True, blue)
win.blit(text3, (50, 50))
pygame.display.update()

initial_text = """    WELCOME TO SUDOKU!\n\n
        Choose difficulty level:\n
             1. Beginner
             2. Intermediate
             3. Advanced"""


def blit_text(surface, text, pos, font, color=blue):
    global word_height
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def my_game():
    # win = pygame.display.set_mode(size=(WIDTH, WIDTH))
    # win.fill(bg_color)
    # myfont = pygame.font.SysFont('Comic Sans MS', 35)
    # pygame.display.set_caption("SUDOKU")
    if button == 1:
        win.fill(bg_color)
        blit_text(win, initial_text, (20, 20), myfont)
        pygame.display.update()
        pos = pygame.mouse.get_pos()
        # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
        print(pos)

    elif button == 2:
        win.fill(bg_color)
        for i in range(10):
            if (i % 3 == 0):
                pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
                pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 5)
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

        pygame.display.update()

        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                if (0 < grid[i][j] < 10):
                    value = myfont.render(str(grid[i][j]), True, grid_ele_color)
                    win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
        pygame.display.update()

        text2 = myfont.render("CLICK ANYWHERE TO SOLVE", True, blue)
        win.blit(text2, (20, 5))
        pygame.display.update()

    elif button == 3:
        solve(grid)
        win.fill(bg_color)
        for i in range(10):
            if (i % 3 == 0):
                pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
                pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 5)
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

        pygame.display.update()

        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                # if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, green)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
        pygame.display.update()

        text2 = myfont.render("SOLVED GRID", True, blue)
        win.blit(text2, (150, 5))
        pygame.display.update()

        print()

        print("--------SOLVED BOARD---------")

        print()

        print_board(grid)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button += 1
            my_game()