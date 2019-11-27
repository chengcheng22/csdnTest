import sys
import pygame
import time

from alien import Alien
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from  game_stats import GameStats

def run_game():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()  # 初始化背景设置
    # screen = pygame.display.set_mode((1200, 800))  # 创建一个名为scree的显示窗口，这个游戏的所有图形元素都将在其中绘制（1200,800）为窗口大小
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    background = pygame.image.load('sky.bmp').convert()
    pygame.display.set_caption("Alien Invation")

    # 创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # aline = Alien(ai_settings, screen)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            # 每次循环时，都更新飞船的位置
            ship.update()
            # 注意写函数时，参数位置要一致
            gf.update_bullets(ai_settings, ship, screen, aliens, bullets)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)




run_game()

