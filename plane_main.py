from plane_sprite import *
from sys import exit


class PlaneGame(object):
    """
    飞机大战主程序
    """
    def __init__(self):
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()

        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4.设置定时器事件 - 创建敌机 1s，发射子弹500ms
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def __create_sprites(self):

        bg1 = BackGround()
        bg2 = BackGround(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        while True:
            # 1.设置刷新频率
            self.clock.tick(FRAME_PRE_SEC)

            # 2.设置事件监听
            self.__event_handler()

            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprite()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("创建敌机")
                # 敌机出场
                enemy = Enemy()
                self.enemy_group.add(enemy)

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # elif event.type == pygame.K_DOWN and event.key == pygame.K_RIGHT:
            #     向右移动
            #     self.hero.speed = 4

        # 使用键盘提供的方法获取键盘按键 - 按键元组
        pressed_key = pygame.key.get_pressed()

        # 判断元组对应的按键索引值 按下为1，否则为0
        if pressed_key[pygame.K_RIGHT]:
            self.hero.speed = 4

        elif pressed_key[pygame.K_LEFT]:
            self.hero.speed = -4

        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)

        # 2.敌机撞毁英雄
        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表有无内容
        if len(enemys) > 0:

            # 销毁英雄
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()


    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        print("游戏结束")
        exit()


if __name__ == '__main__':

    game = PlaneGame()
    game.start_game()