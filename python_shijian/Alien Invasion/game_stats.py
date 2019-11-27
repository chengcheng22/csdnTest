class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏一直处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化游戏在运行期间可能的变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit