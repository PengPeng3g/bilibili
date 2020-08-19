"""
奖与罚
编译者：PengPeng3g
v1.0 增加奖与罚
编译时间：2020.8.16
当前版本：v1.0
"""

chengji=int(input("输入成绩自动判断奖与罚："))

if chengji == 300:
    print("任何物品")

elif chengji > 290:
    print("手机走起")

elif chengji > 280:
    print("好吃滴，好喝滴")

elif chengji > 270:
    print("小型玩具")

elif chengji >260:
    print("奖励试卷一套")

elif chengji >250:
    print("奖励大嘴巴子")

else:
    print("奖励补习班一个假期")

