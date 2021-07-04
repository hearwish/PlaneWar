from plane_sprites import *
import pygame


class PlaneGame(object):
    def __init__(self):
        pygame.init()
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵族的创建
        self.__create_sprites()
        print("init")
        # 4.设置定时器事件 创建敌机 1s
        #pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bq1 = Background()
        bq2 = Background(is_alt=True)
        self.back_group = pygame.sprite.Group(bq1, bq2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵族
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("start...")
        while True:
            # 1.设置刷新帧
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵族
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # enemy.speedx = random.randint(0, 3)
                # 将敌机精灵加入到精灵族
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 使用键盘提供的方法提取键盘按键
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speedx = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speedx = -5
        else:
            self.hero.speedx = 0

        if keys_pressed[pygame.K_DOWN]:
            self.hero.speedy = 5
        elif keys_pressed[pygame.K_UP]:
            self.hero.speedy = -5
        else:
            self.hero.speedy = 0

    def __check_collide(self):
        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 2.敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.draw(self.screen)
        self.hero_group.update()
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()