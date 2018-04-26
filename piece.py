# @Time    : 2018/4/24 14:58
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

from settings import *
from pygame import *
import pygame

class Piece():
    def __init__(self, shape, screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.turn = 0   #翻转了几次，决定显示的模样
        self.screen = screen

    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn]
        #print(shape_turn)
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, x, y):
        cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1,
                         y * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, CELL_COLOR, cell_rect)

    def move_right(self):
        '''方块向右移动1个单元格'''
        if self.can_move_right():
            self.x += 1

    def move_left(self):
        '''方块向左移动1格'''
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        '''方块向下移动1格'''
        if self.can_move_down():
            self.y += 1

    def can_move_right(self):
        shape_mtx = PIECES[self.shape][0]  #姿态矩阵
        # print(shape_mtx)
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c >= COLUMN_NUM - 1:
                        return False
        return True

    def can_move_left(self):
        shape_mtx = PIECES[self.shape][0]  #姿态矩阵
        # print(shape_mtx)
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c <= 0:
                        return False
        return True

    def can_move_down(self):
        shape_mtx = PIECES[self.shape][0]  #姿态矩阵
        # print(shape_mtx)
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.y + r >= LINE_NUM - 1:
                        return False
        return True