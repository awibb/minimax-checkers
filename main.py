from tkinter import W
import pygame
from const import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("checkers-ui")


def x_y(pos):
    x,y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

def main():
    game_loop = True
    clock = pygame.time.Clock()
    board = Board() 
    while game_loop:
        clock.tick(60)
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                game_loop = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # check for square and piece color
                pos = pygame.mouse.get_pos()
                row, col = x_y(pos)
                #debug 
                print("cordinates: ", row, col)
                if(board.board[row][col] != 0):
                    #debug 
                    print("piece color: ", board.board[row][col].color)
                
        board.draw(WINDOW)
        pygame.display.update()

    pygame.quit()


main()
