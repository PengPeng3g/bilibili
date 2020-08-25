"""
脏话过滤器
编译者：PengPeng3g
编译时间：2020/8/20
v1.0
v2.0 新增祖安语句持续更新
v3.0 新增不区分大小写
"""

a = "t"

while a == 't':

    mingancihui = input("请输入评论：").strip().upper()

    if "SB" in mingancihui or "NMSL" in mingancihui or "CNMB" in mingancihui or 'CTMD' in mingancihui  or '我是你爸爸' in mingancihui or '傻逼' in mingancihui or '艹' in mingancihui or 'WRNNN' in mingancihui or '二逼' in mingancihui or 'NSSBM' in mingancihui:
        a = 'f'
        print("您祖安了，系统自动驳回。")
        a = 't'

    else:
        print('您输入的评论：',mingancihui)
        a = 'f'
        a = 't'