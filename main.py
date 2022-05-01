import pygame
from const import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from game import Game
from piece import Piece
from time import sleep
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("checkers-ui")


def x_y(pos):
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE


def main():
    game_loop = True
    clock = pygame.time.Clock()
    gra = Game()
    while game_loop and gra.win == False:
        clock.tick(60)
        gra.board.draw(WINDOW)
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_loop = False

            if pygame.key.get_pressed()[pygame.K_F11]:
                print("minimax v minimax")
                gra.ai_move(gra.turn)
                gra.change_teams()

            elif(gra.turn == RED):

                #if event.type == pygame.MOUSEBUTTONDOWN:
                #     pos = pygame.mouse.get_pos()
                #     row, col = x_y(pos)
                #     userClick = gra.board.board[row][col]
                #     if type(userClick) == Piece and userClick.color == gra.turn:
                #         gra.play(row, col)
                #     if type(userClick) == int and userClick == 1 and gra.prev_x != None and gra.prev_y != None:
                #         gra.process_move(row, col)
                gra.board.draw(WINDOW)
                pygame.display.update()
                gra.ai_move(gra.turn)
                gra.change_teams()
                gra.board.draw(WINDOW)
                pygame.display.update()

            elif gra.turn == WHITE:
                gra.ai_move(WHITE)
                gra.change_teams()

    pygame.quit()


main()
