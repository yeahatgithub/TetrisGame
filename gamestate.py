# @Time    : 2018/4/30 15:32
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
import time
class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None
        self.next_piece = None
        self.timer_interval = TIMER_INTERVAL   #1000ms
        self.game_score = 0
        self.stopped = True
        self.paused = False
        self.session_count = 0
        self.difficulty = 1

    def set_timer(self, timer_interval):
        pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)  #传入0表示清除定时器

    def add_score(self, score):
        self.game_score += score
        difficulty = self.game_score // DIFFICULTY_LEVEL_INTERVAL + 1
        if difficulty > self.difficulty:
            self.difficulty += 1
            self.timer_interval -= TIMER_DECREASE_VALUE
            pygame.time.set_timer(pygame.USEREVENT, self.timer_interval)

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = self.new_piece()  #生成第一个方块。此时self.piece=None, self.next_piece引用方块对象。
        self.piece = self.new_piece()  #生成第二个方块，此时self.piece引用方块对象。
        self.session_count += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False
        random.seed(int(time.time()))  #每次游戏，使用不同的随机数序列

    def pause_game(self):
        self.stop_timer()
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def touch_bottom(self):
        self.wall.add_to_wall(self.piece)
        self.add_score(self.wall.eliminate_lines())
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0, c):
                self.stopped = True
                break
        if not self.stopped:
            self.piece = self.new_piece()
            if self.piece.hit_wall():
                self.stopped = True
        if self.stopped:
            self.stop_timer()

    def new_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)

        return self.piece