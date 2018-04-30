# @Time    : 2018/4/29 7:38
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
from settings import *
from gamedisplay import GameDisplay

class GameWall():
    '''游戏区墙体类。记住落到底部的方块组成的“墙”。'''
    def __init__(self, screen):
        '''游戏开始时，游戏区20*10个格子被'-'符号填充。“墙”是空的。'''
        self.screen = screen
        self.area = []
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])

    def print(self):
        '''打印20*10的二维矩阵self.area的元素值。用于调试。'''
        print(len(self.area), "rows", len(self.area[0]), "colums")
        for line in self.area:
            print(line)


    def set_cell(self, row, column, shape_label):
        '''把第row行column列的格子打上方块记号（如S, L...），因为该格子被此方块占据。'''
        self.area[row][column] = shape_label


    def add_to_wall(self, piece):
        '''把方块piece砌到墙体内'''
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.set_cell(piece.y + r, piece.x + c, piece.shape)


    def is_wall(self, row, column):
        return self.area[row][column] != WALL_BLANK_LABEL