"""
奖与罚
编译者：PengPeng3g
v1.0 增加奖与罚
v2.0 增加循环节,增加初中，高中成绩
编译时间：2020.8.16
当前版本：v2.0
"""

tuichugaozhong = False

tuichuchuzhong = False

tuichu = False

xuanzenianji=(input("输入年级（初中chuzhong,小学xiaoxue,高中gaozhong）"))

if xuanzenianji == "xiaoxue":
    tuichu = True
if xuanzenianji == 'chuzhong':
    tuichuchuzhong = True
if xuanzenianji == 'gaozhong':
    tuichugaozhong = True

while tuichu:

    xiaoxuechengji=int(input("输入你的成绩（输入888退出）："))

    if xiaoxuechengji == 300:
        print("任何东西")

    elif xiaoxuechengji == 888:
        tuichu = False

    elif xiaoxuechengji > 290:
        print("手机走起")

    elif xiaoxuechengji > 280:
        print('现金不定')

    elif xiaoxuechengji > 270:
        print("现金些许")

    elif xiaoxuechengji > 260:
        print("试卷一套")

    elif xiaoxuechengji > 250:
        print("补习班耶")

    else:
        print("舒服按摩")


while tuichuchuzhong:

        chuzhongchengji = int(input("输入你的成绩（输入888退出）："))

        if chuzhongchengji > 730:
            print("长辈夸赞+任何东西")

        elif chuzhongchengji == 888:
            tuichuchuzhong = False

        elif chuzhongchengji < 700:
            print("新手机一台")

        elif chuzhongchengji < 690:
            print("现金不等")

        elif chuzhongchengji < 500:
            print("还行")

        elif chuzhongchengji < 400:
            print("奖励试卷一套")

        elif chuzhongchengji < 200:
            print("最喜欢的大嘴巴子+一个假期的补习班")

        else:
            print("父母混合打")

while tuichugaozhong:

            gaozhongchengji=int(input("输入你的成绩（输入888退出）："))

            if gaozhongchengji > 720:
                print("任何东西")

            elif gaozhongchengji == 888:
                tuichugaozhong = False


            elif gaozhongchengji > 700:
                print("父母赞扬+现金不等")

            elif gaozhongchengji > 600:
                print("些许东西")

            elif gaozhongchengji > 500:
                print("一点东西")

            elif gaozhongchengji > 400:
                print("冷漠")

            elif gaozhongchengji > 200:
                print("父母混合打")

            else:
                print("父母失望")