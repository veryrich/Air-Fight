import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 752)

# 每秒更新的帧数
FRAME_PRE_SEC = 60

# 创建定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):

        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class BackGround(GameSprite):
    """
    游戏背景精灵
    """
    def __init__(self, is_alt=False):

        # 调用父类方法实现父类的创建
        super().__init__("./image/background.png")

        # 判断是否为交替图像，如果是，需要设置初始位置
        if is_alt is True:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法实现y轴滚动
        super().update()

        # 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./image/enemy0.png")

        # 2.指定敌机的初始随机速度
        self.speed = random.randint(2, 3)

        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(self.rect.width, max_x)

    def update(self):

        # 1.调用父类方法，保持垂直方向的飞行
        super().update()

        # 2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("超出屏幕，从精灵组删除")
            self.kill()

        # 敌机销毁前调用
    def __del__(self):
        # print("敌机销毁成功 %s" % self.rect)
        pass


class Hero(GameSprite):
    """
    英雄精灵
    """

    def __init__(self):

        # 1.调用父类方法设置图片和速度
        super().__init__("./image/hero1.png", 0)

        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.创建子弹的精灵组
        self.bullet_group = pygame.sprite.Group()

    # 英雄x轴横向移动
    def update(self):
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 同时发射两颗子弹
        # for i in range(2):

        # 1.创建子弹精灵
        bullet = Bullet()
        # 2.设置精灵的位置
        bullet.rect.bottom = self.rect.y - 5
        bullet.rect.centerx = self.rect.centerx
        # 3.将精灵添加到精灵组
        self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):

        # 调用父类方法，设置子弹图片，设置初始速度。
        super().__init__("./image/bullet1.png", -2)

    def update(self):

        # 调用父类方法，让子弹垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


