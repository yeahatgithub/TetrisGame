# @Time    : 2018/4/24 14:58
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

from settings import *
from pygame import *
import pygame
from gamedisplay import GameDisplay

class Piece():
    def __init__(self, shape, screen, gamewall):
        self.x = 4
        self.y = 0
        self.shape = shape
        self.turn_times = 0   #翻转了几次，决定显示的模样
        self.screen = screen
        self.is_on_bottom = False    #到达底部了吗？
        self.game_wall = gamewall


    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn_times]
        #print(shape_turn)
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.y + r, self.x + c)

    def draw_cell(self, row, column):
        # cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1,
        #                  y * CELL_WIDTH + GAME_AREA_TOP + 1)
        # cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        # cell_rect = Rect(cell_position, cell_width_height)
        # pygame.draw.rect(self.screen, PIECE_COLORS[self.shape], cell_rect)
        GameDisplay.draw_cell(self.screen, row, column, PIECE_COLORS[self.shape])

    def move_right(self):
        '''方块向右移动1个单元格'''
        if self.can_move_right():
            self.x += 1

    def move_left(self):
        '''方块向左移动1格'''
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        '''方块向下移动1格。如果到达了底部，设置is_on_bottom属性为True.'''
        if self.can_move_down():
            self.y += 1
        else:
            self.is_on_bottom = True

    def fall_down(self):
        while not self.is_on_bottom:
            self.move_down()

    def can_move_right(self):
        shape_mtx = PIECES[self.shape][self.turn_times]  #姿态矩阵
        # print(shape_mtx)
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c >= COLUMN_NUM - 1 or self.game_wall.is_wall(self.y + r, self.x + c + 1):
                        return False
        return True

    def can_move_left(self):
        shape_mtx = PIECES[self.shape][self.turn_times]  #姿态矩阵
        # print(shape_mtx)
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c <= 0 or self.game_wall.is_wall(self.y + r, self.x + c - 1):
                        return False
        return True

    def can_move_down(self):
        shape_mtx = PIECES[self.shape][self.turn_times]  #姿态矩阵
        # print(shape_mtx)
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.y + r >= LINE_NUM - 1 or self.game_wall.is_wall(self.y + r + 1, self.x + c):
                        return False
        return True


    def turn(self):
        shape_list_len = len(PIECES[self.shape])
        if self.can_turn():
            self.turn_times = (self.turn_times + 1) % shape_list_len

    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) % shape_list_len
        shape_mtx = PIECES[self.shape][turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if (self.x + c < 0 or self.x + c >= COLUMN_NUM) or (self.y + r < 0 or self.y + r >= LINE_NUM) \
                            or self.game_wall.is_wall(self.y + r, self.x + c):
                        return False
        return True

    def hit_wall(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.game_wall.is_wall(self.y + r, self.x + c):
                        return True
        return False

