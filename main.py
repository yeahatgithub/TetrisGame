# @Time    : 2018/4/23 16:44
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import sys
import pygame

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
        #让最近绘制的屏幕可见
        pygame.display.flip()

def draw_game_area(screen):
    '''绘制游戏区域'''
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (200, 200))
    #绘制一条线。第二个参数(0, 0, 0)决定颜色是黑色。起点坐标是(100, 100)，终点是(200, 200)


if __name__ == '__main__':
    main()