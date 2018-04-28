# @Time    : 2018/4/23 16:44
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import sys
import pygame
import random
from settings import *
from piece import Piece

def main():
    #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行。
    pygame.init()
    #创建屏幕对象
    screen = pygame.display.set_mode((1200, 900) )  #分辨率是1200*900
    pygame.display.set_caption("俄罗斯方块")  #窗口标题

    #屏幕背景色
    bg_color = (230, 230, 230)
    piece = None

    #游戏主循环
    while True:
        #生成方块对象
        if not piece or piece.is_on_bottom:
            piece = Piece(random.choice(PIECE_TYPES), screen)

        #监视键盘和鼠标事件
        check_events(piece)

        #设定屏幕背景色
        screen.fill(bg_color)
        #绘制游戏区域网格线
        draw_game_area(screen)
        #绘制方块
        piece.paint()
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

def check_events(piece):
    '''捕捉和处理键盘按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # print("向下方向键被按下")
                piece.move_down()
            elif event.key == pygame.K_UP:
                # print("向上方向键被按下")
                piece.turn()
            elif event.key == pygame.K_RIGHT:
                # print("向右方向键被按下")
                piece.move_right()
            elif event.key == pygame.K_LEFT:
                # print("向左方向键被按下")
                piece.move_left()


if __name__ == '__main__':
    main()