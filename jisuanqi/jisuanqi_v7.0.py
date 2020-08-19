"""
计算器
编译者：PengPeng3g
v1.0 增加加法
v2.0 增加减，乘，除法
v3.0 可以多部计算，但需更改代码
v4.0 在v2.0的基础上更改，精简v2.0的代码
v5.0 精简代码
v6.0 精简代码
v7.0 增加循环节
当前版本：v7.0
"""
a=True

while a:

    diyigejiashu=int(input('加数'))

    diergejiashu=int(input('加数'))

    print('和', diyigejiashu+diergejiashu)



    beichushu=int(input('被除数'))

    chushu=int(input('除数'))

    print('商',beichushu/chushu)



    diyigechengshu=int(input('因数'))

    diergechengshu=int(input('因数'))

    print('积',diyigechengshu*diergechengshu)



    beijianshu=int(input('被减数'))

    jianshu=int(input('减数'))

    print('差',beijianshu-jianshu)

    b=input("是否继续计算？")

    if b == "是":
        a = True
    else:
        a = False