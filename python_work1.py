'''
题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
通过猜拳来确定谁打谁
谁的hp先为0，那么谁就输了
'''
import random

#定义打拳游戏函数
def fight():
    # 给敌我双方的血量、攻击力赋初始值
    my_hp = 1000
    enemy_hp = 1000
    my_power = 200
    enemy_power = 180
    count = 0
    while 1 == 1:
        if random.randint(1, 2) == 1:
            enemy_hp = enemy_hp - my_power
            print("第", count, "回合我猜拳赢了，我打你一拳！你剩余血量：", enemy_hp)
        else:
            my_hp = my_hp - enemy_power
            print("第", count, "回合你猜拳赢了，你打我一拳！我剩余血量：", my_hp)
        count+=1
        if my_hp <= 0:
            print("你赢了！")
            break
        elif enemy_hp <= 0:
            print("我赢了！")
            break
#游戏函数调用
fight()
