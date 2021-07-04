import pygame
from plane_sprites import *
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480,700))
# 绘制背景图像
# 加载图像数据
bg = pygame.image.load("./images/background.png")
# 绘制图像
screen.blit(bg, (0,0))
# 更新屏幕显示
# pygame.display.update()
# 英雄的飞机
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (100,500))
pygame.display.update()
# 游戏时钟
clock = pygame.time.Clock()
# 记录飞机初始位置
hero_rect = pygame.Rect(150,300,102,126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵族
enemy_group = pygame.sprite.Group(enemy,enemy1)

# 游戏循环->游戏正式开始
while True:
    # 指定循环内部代码执行频率
    clock.tick(60)
    # 监听用户事件
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # 终止python程序
            exit()

    hero_rect.y -=1
    # 判断飞机位置
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 重画背景
    screen.blit(bg,(0,0))
    screen.blit(hero, hero_rect)
    # 让精灵组调用两个方法
    enemy_group.update()
    # 画到屏幕对象上
    enemy_group.draw(screen)
    pygame.display.update()
pygame.quit()