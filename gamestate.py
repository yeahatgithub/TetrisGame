# @Time    : 2018/4/30 15:32
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None
        self.timer_interval = TIMER_INTERVAL   #1000ms
        self.game_score = 0
        self.stopped = True
        self.paused = False
        self.session_count = 0

    def set_timer(self, timer_interval):
        pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)  #传入0表示清除定时器

    def add_score(self, score):
        self.game_score += score

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
        self.session_count += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False

    def pause_game(self):
        self.stop_timer()
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def touch_bottom(self):
        self.wall.add_to_wall(self.piece)
        self.add_score(self.wall.eliminate_lines())
        # print(game_state.game_score)
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0, c):
                # game_area.draw_gameover()   #在这里绘制文字是不起作用的。必须放到主循环中。
                self.stopped = True
                break
        if not self.stopped:
            self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)  #TODO: 新生成的方块撞到墙，意味着游戏结束。
        else:
            self.stop_timer()