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
    pygame.key.set_repeat(100, 100)  # 一直按下某个键，每过100毫秒就引发一个KEYDOWN事件

    #屏幕背景色
    bg_color = (230, 230, 230)

    game_state = GameState(screen)
    game_resource = GameResource()
    game_resource.play_bg_music()
    #游戏主循环
    while True:
        #方块触底的话
        if game_state.piece and game_state.piece.is_on_bottom:
            game_state.touch_bottom()

        #监视键盘和鼠标事件
        check_events(game_state, game_resource)

        #设定屏幕背景
        screen.blit(game_resource.load_bg_img(), (0, 0))
        #绘制方块
        if game_state.piece:
            game_state.piece.paint()
        #绘制游戏区域网格线和墙体
        GameDisplay.draw_game_window(screen, game_state, game_resource)
        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events(game_state, game_resource):
    '''捕捉和处理键盘按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, game_state, game_resource)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_down()


def on_key_down(event, game_state, game_resource):
    if not game_state.paused and event.key == pygame.K_DOWN:
        # print("向下方向键被按下")
        if game_state.piece:
            game_state.piece.move_down()
    elif not game_state.paused and event.key == pygame.K_UP:
        # print("向上方向键被按下")
        if game_state.piece:
            game_state.piece.turn()
    elif not game_state.paused and event.key == pygame.K_RIGHT:
        # print("向右方向键被按下")
        if game_state.piece:
            game_state.piece.move_right()
    elif not game_state.paused and event.key == pygame.K_LEFT:
        # print("向左方向键被按下")
        if game_state.piece:
            game_state.piece.move_left()
    elif not game_state.paused and event.key == pygame.K_f:
        if game_state.piece:
            game_state.piece.fall_down()
    elif event.key == pygame.K_s and game_state.stopped:
        game_state.start_game()
    elif event.key == pygame.K_p and not game_state.stopped:
        if game_state.paused:
            game_state.resume_game()
        else:
            game_state.pause_game()
    elif event.key == pygame.K_r:
        game_state.start_game()  #按r键强制重新开始游戏
    elif event.key == pygame.K_m:
        game_resource.pause_bg_music()
    elif event.key == pygame.K_q:
        sys.exit()


if __name__ == '__main__':
    main()