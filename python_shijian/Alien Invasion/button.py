import pygame.font   # 将文本渲染到屏幕上

class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # 亮绿色
        self.text_color = (255, 255, 255)
        self。fron
        self.rect.center = self.screen_rect.center

        # 按钮标签只需创造一次
        self.prep_msg = msg