# @Time    : 2018/4/23 16:44
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import sys
import pygame
import random
import time
from settings import *
from piece import Piece
from gamewall import GameWall
from gamedisplay import GameDisplay
from gamestate import GameState
from gameresource import GameResource

def main():
    #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行。
    pygame.init()
    #创建屏幕对象
    screen = pygame.display.set_mode((1200, 900) )  #分辨率是1200*900
    pygame.display.set_caption("俄罗斯方块")  #窗口标题
    pygame.key.set_repeat(10, 100)  # 一直按下某个键，每过100毫秒就引发一个KEYDOWN事件

    #屏幕背景色
    bg_color = (230, 230, 230)

    random.seed(int(time.time()))    #产生不同的随机序列
    game_state = GameState(screen)
    game_resource = GameResource()
    #游戏主循环
    while True:
        #方块触底的话
        if game_state.piece and game_state.piece.is_on_bottom:
            game_state.wall.add_to_wall(game_state.piece)
            game_state.add_score(game_state.wall.eliminate_lines())
            # print(game_state.game_score)
            game_state.piece = Piece(random.choice(PIECE_TYPES), screen, game_state.wall)

        #监视键盘和鼠标事件
        check_events(game_state)

        #设定屏幕背景色
        screen.fill(bg_color)
        #绘制游戏区域网格线和墙体
        GameDisplay.draw_game_area(screen, game_state, game_resource)
        #绘制方块
        if game_state.piece:
            game_state.piece.paint()
        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events(game_state):
    '''捕捉和处理键盘按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, game_state)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_down()


def on_key_down(event, game_state):
    if event.key == pygame.K_DOWN:
        # print("向下方向键被按下")
        if game_state.piece:
            game_state.piece.move_down()
    elif event.key == pygame.K_UP:
        # print("向上方向键被按下")
        if game_state.piece:
            game_state.piece.turn()
    elif event.key == pygame.K_RIGHT:
        # print("向右方向键被按下")
        if game_state.piece:
            game_state.piece.move_right()
    elif event.key == pygame.K_LEFT:
        # print("向左方向键被按下")
        if game_state.piece:
            game_state.piece.move_left()
    elif event.key == pygame.K_f:
        if game_state.piece:
            game_state.piece.fall_down()
    elif event.key == pygame.K_s and game_state.stopped:
        game_state.start_game()


if __name__ == '__main__':
    main()