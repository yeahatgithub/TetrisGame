# @Time    : 2018/4/29 7:54
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
from settings import *
import pygame


class GameDisplay():
    @staticmethod
    def draw_cell(screen, row, column, color):
        '''第row行column列的格子里填充color颜色。一种方块对应一种颜色。'''
        cell_position = (column * CELL_WIDTH + GAME_AREA_LEFT + 1,
                         row * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_game_area(screen, game_wall):
        '''绘制游戏区域'''
        for r in range(21):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
                             (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))
        for c in range(11):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
                             (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))

        GameDisplay.draw_wall(game_wall)

    @staticmethod
    def draw_wall(game_wall):
        '''绘制墙体'''
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, r, c, PIECE_COLORS[game_wall.area[r][c]])