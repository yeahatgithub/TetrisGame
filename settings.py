# @Time    : 2018/4/24 14:46
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

SCREEN_WIDTH = 1200      #窗口宽度
SCREEN_HEIGHT = 900     #窗口高度
CELL_WIDTH = 40         #方块在20*10个单元格组成的游戏区内移动。每个单元格的边长是40个像素。
LINE_NUM = 20           #游戏区域共20行
COLUMN_NUM = 10         #游戏区域共10列
GAME_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM     #游戏区域宽度（单位：像素）
GAME_AREA_HEIGHT = CELL_WIDTH * LINE_NUM      #游戏区域高度
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2      #游戏区左侧的空白区的宽度
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT - 50       #游戏区顶部的空白区的宽度
EDGE_COLOR = (0, 0, 0)          #游戏区单元格边界线的颜色。今后，网格线会被去除。
CELL_COLOR = (100, 100, 100)    #单元格填充色。
BG_COLOR = (230, 230, 230)      #窗口背景色

#S型方块的姿态序列。首先是未翻转的姿态，接着是向右翻转90度的姿态。再翻转90度，将回到未翻转前的姿态。
S_SHAPE_TEMPLATE = [['.OO.',
                     'OO..',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '..O.']]

Z_SHAPE_TEMPLATE = [['OO..',
                     '.OO.',
                     '....'],
                    ['..O.',
                     '.OO.',
                     '.O..']]

I_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.O..',
                     '.O..'],
                    ['....',
                     'OOOO',
                     '....',
                     '....']]

O_SHAPE_TEMPLATE = [['OO',
                     'OO']]

J_SHAPE_TEMPLATE = [['.O.',
                     '.O.',
                     'OO.'],
                    ['O..',
                     'OOO',
                     '...'],
                    ['OO.',
                     'O..',
                     'O..'],
                    ['OOO',
                     '..O',
                     '...']]

L_SHAPE_TEMPLATE = [['O..',
                     'O..',
                     'OO.'],
                    ['...',
                     'OOO',
                     'O..'],
                    ['OO.',
                     '.O.',
                     '.O.'],
                    ['..O',
                     'OOO',
                     '...']]

T_SHAPE_TEMPLATE = [['.O.',
                     'OOO',
                     '...'],
                    ['.O.',
                     '.OO',
                     '.O.'],
                    ['...',
                     'OOO',
                     '.O.'],
                    ['..O',
                     '.OO',
                     '..O']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE
          }

PIECE_TYPES = ['S', 'Z', 'J', 'L', 'I', 'O', 'T']

PIECE_COLORS = {
    'S': (0, 255, 128),
    'Z': (255, 128, 255),
    'J': (128, 0, 255),
    'L': (0, 0, 255),
    'I': (0, 128, 0),
    'O': (255, 0, 0),
    'T': (255, 128, 0)
}

WALL_BLANK_LABEL = '-'   #墙体矩阵中表示无砖块
TIMER_INTERVAL = 1000   #方块自动落下的等待时间初始值。

SCORE_LABEL_COLOR = (0, 0, 0)
SCORE_COLOR = (255, 0, 0)
TITLE_COLOR = (0, 0, 255)
HANZI_COLOR = (0, 0, 0)

EDGE_WIDTH = 5      #游戏区域外框线宽度
MARGIN_WIDTH = 40   #游戏区域外框线与其他窗口元素之间的间距

DIFFICULTY_LEVEL_INTERVAL = 5000   #每过5000分，难度升1级
TIMER_DECREASE_VALUE = 50           #难度每升1级，定时器加快50ms发出闹铃信号