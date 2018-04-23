# @Time    : 2018/4/23 16:44
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import sys
import pygame

SCREEN_WIDTH = 1200      #窗口宽度
SCREEN_HEIGHT = 900     #窗口高度
CELL_WIDTH = 40         #方块在20*10个单元格组成的游戏区内移动。每个单元格的边长是40个像素。
GAME_AREA_WIDTH = CELL_WIDTH * 10       #一行10个单元格
GAME_AREA_HEIGHT = CELL_WIDTH * 20      #一共20行
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2      #游戏区左侧的空白区的宽度
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT          #游戏区顶部的空白区的宽度
EDGE_COLOR = (0, 0, 0)          #游戏区单元格边界线的颜色。今后，网格线会被去除。
CELL_COLOR = (100, 100, 100)    #单元格填充色。
BG_COLOR = (230, 230, 230)      #窗口背景色


def main():
    #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行。
    pygame.init()
    #创建屏幕对象
    screen = pygame.display.set_mode((1200, 900) )  #分辨率是1200*900
    pygame.display.set_caption("俄罗斯方块")  #窗口标题

    #屏幕背景色
    bg_color = (230, 230, 230)

    #游戏主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #设定屏幕背景色
        screen.fill(bg_color)
        #绘制直线
        draw_game_area(screen)
        #绘制小方块
        draw_cell(screen, GAME_AREA_LEFT + 4 * CELL_WIDTH, GAME_AREA_TOP)
        #让最近绘制的屏幕可见
        pygame.display.flip()

def draw_game_area(screen):
    '''绘制游戏区域'''
    for r in range(21):
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))
    for c in range(11):
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))

def draw_cell(screen, left, top):
    '''绘制单元格，也即绘制小方块'''
    '''
    left: 单元格离窗口左边界的距离。单位是像素。
    top: 单元格离窗口上边界的距离。
    '''
    cell_left_top = (left, top)    #小方块的左上角坐标点
    cell_width_height = (CELL_WIDTH, CELL_WIDTH)    #小方块的宽度和高度
    cell_rect = pygame.Rect(cell_left_top, cell_width_height)   #生成由左上角坐标和宽度高度定义的矩形
    pygame.draw.rect(screen, CELL_COLOR, cell_rect)    #绘制正方形



if __name__ == '__main__':
    main()