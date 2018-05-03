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

    def eliminate_lines(self):
        '''消行。如果一行没有空白单元格，就消掉该行。返回得分。'''
        '''
        计分规则：
        消掉0行：0分
        消掉1行：100分
        消掉2行：200分
        消掉3行：400分
        消掉4行：800分
        '''
        #需要消哪几行
        lines_eliminated = []
        for r in range(LINE_NUM):
            if self.is_full(r):
                lines_eliminated.append(r)

        #消行，更新墙体矩阵
        for r in lines_eliminated:
            self.copy_down(r)  #消掉r行，上面的各行依次下沉一行。
            for c in range(COLUMN_NUM):
                self.area[0][c] = WALL_BLANK_LABEL

        #根据消掉的行数，计算得分
        eliminated_num = len(lines_eliminated)
        assert(eliminated_num <= 4 and eliminated_num >= 0)
        if eliminated_num < 3:
            score = eliminated_num * 100
        elif eliminated_num == 3:
            score = 400
        else:
            score = 800
        return score

    def is_full(self, row):
        '''row行满了吗'''
        for c in range(COLUMN_NUM):
            if self.area[row][c] == WALL_BLANK_LABEL:
                return False

        return True

    def copy_down(self, row):
        '''把row行上面各行下沉一行。'''
        for r in range(row, 0, -1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r - 1][c]

    def clear(self):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                self.area[r][c] = WALL_BLANK_LABEL