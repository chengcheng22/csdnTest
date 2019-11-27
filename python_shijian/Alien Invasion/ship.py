import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船，并设置初始位置"""
        self.screen = screen
        # 飞船设置
        self.ai_settings = ai_settings
        # 加载飞船图像, 并获取其外接矩形
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每一艘飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值，rect将只存储这个值得整数部分
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        """在指定位置画飞船"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center而不是rect
        # 防止飞船位置在屏幕之外
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据center值更新rect值
        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
