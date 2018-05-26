# @Time    : 2018/4/24 14:46
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

SCREEN_WIDTH = 1200      #窗口宽度
SCREEN_HEIGHT = 900     #窗口高度
CELL_WIDTH = 40         #方块在20*10个单元格组成的游戏区内移动。每个单元格的边长是40个像素。
LINE_NUM = 20           #游戏区域共20行
COLUMN_NUM = 10         #游戏区域共10列
GAME_AREA_WIDTH = CELL_WIDTH * 10       #一行10个单元格
GAME_AREA_HEIGHT = CELL_WIDTH * 20      #一共20行
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2      #游戏区左侧的空白区的宽度
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT          #游戏区顶部的空白区的宽度
EDGE_COLOR = (0, 0, 0)          #游戏区单元格边界线的颜色。今后，网格线会被去除。
CELL_COLOR = (100, 100, 100)    #单元格填充色。
BG_COLOR = (230, 230, 230)      #窗口背景色

## 方块的形状矩阵
S_SHAPE_TEMPLATE = ['.OO.',
                     'OO..',
                     '....']

Z_SHAPE_TEMPLATE = ['OO..',
                     '.OO.',
                     '....']

I_SHAPE_TEMPLATE = ['.O..',
                     '.O..',
                     '.O..',
                     '.O..']

O_SHAPE_TEMPLATE = ['OO',
                     'OO']

J_SHAPE_TEMPLATE = ['..O.',
                     '..O.',
                     '.OO.']

L_SHAPE_TEMPLATE = ['.O..',
                     '.O..',
                     '.OO.']

T_SHAPE_TEMPLATE = ['.O..',
                     'OOO.',
                     '....']

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}