"""
二分法模块
作者：PengPeng3g
编译时间：2020/10/7
"""
def erfenfa(diyi,dier):
    a = 0
    zuojiduansuoyin = 0
    youjiduansuoyin = len(diyi) - 1
    zhongjianshusuoyin = (zuojiduansuoyin+youjiduansuoyin) // 2
    zhongjianshu = diyi[zhongjianshusuoyin]
    while a <= len(diyi):
        zhongjianshusuoyin = (zuojiduansuoyin+youjiduansuoyin) // 2
        if dier < diyi[zhongjianshusuoyin]:
            youjiduansuoyin = zhongjianshusuoyin - 1
            a = a + 1
        elif dier > diyi[zhongjianshusuoyin]:
            zuojiduansuoyin = zhongjianshusuoyin + 1
            a = a + 1
        else:
            print('有这个数字，索引：',zhongjianshusuoyin)
            break
    else:
        print('在这个列表中，没有这个数字')