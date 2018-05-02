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

    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def add_score(self, score):
        self.game_score += score

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)

    def pause_game(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)   #传入0表示清除定时器
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False