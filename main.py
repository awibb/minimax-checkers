from tkinter import W
import pygame
from const import WIDTH, HEIGHT, SQUARE_SIZE
from game import Game
from piece import Piece
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("checkers-ui")


def x_y(pos):
    x,y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

def main():
    game_loop = True
    clock = pygame.time.Clock()
    gra = Game() 
    while game_loop:
        clock.tick(60)
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                game_loop = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = x_y(pos)
                userClick = gra.board.board[row][col]
                if type(userClick) == Piece and userClick.color == gra.turn:
                    gra.play(row,col)
                if type(userClick) == int and gra.prev_x != None and gra.prev_y != None:
                    gra.process_move(row,col)
        gra.board.draw(WINDOW)
        pygame.display.update()

    pygame.quit()


main()
