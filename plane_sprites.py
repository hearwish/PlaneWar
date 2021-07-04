import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧数
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定义发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speedx=0, speedy=1):
        # 调用父类初始化方法
        super().__init__()
        # 定义对象的属性
        # 加载图片
        self.image = pygame.image.load(image_name)
        # 获取位置
        self.rect = self.image.get_rect()
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        # 在垂直方向移动
        self.rect.y += self.speedy
        self.rect.x += self.speedx


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵创建
        super().__init__("./images/background.png", 0, 1)
        # 2.判断是否是交替图像，是则设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类方法实现
        super().update()
        # 2.判断是否移除屏幕，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，指定图片
        super().__init__("./images/enemy1.png")

        # 2.指定敌机初始随机速度
        self.speedy = random.randint(1, 3)
        # 3.指定敌机初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        # 判断是否飞出屏幕，从精灵族移除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机销毁 %s " % self.rect)


class Hero(GameSprite):

    def __init__(self):
        # 1.调用父类方法，设置image&speed
        super().__init__("./images/me1.png", 0, 0)
        # 2.设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3.建立子弹精灵族
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄水平方向移动

        super().update()
        if self.rect.x < 0:
            self.rect.x = 0
            print(self.rect.x)
            # self.speedx = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_RECT.height:
            self.rect.y = 0
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy

    def fire(self):
        """发射子弹"""
        # 一次发射三枚
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)
        # 一次发射一枚
        #     bullet = Bullet()
        #     bullet.rect.bottom = self.rect.y - i * 20
        #     bullet.rect.centerx = self.rect.centerx
        #     self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法，设置图片，设置初始速度
        super().__init__("./images/bullet1.png", 0, -2)

    def update(self):
        super().update()
        # 判断字段是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass