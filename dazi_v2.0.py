xinxi = """
打字练习器
编译者：PengPeng3g
更新日志：
    v1.0
    v2.0 优化代码
当前版本：v2.0
编译时间：2020/12/12
"""
print(xinxi)
import random
import time
def suijishengcheng():
    num = random.randint(65,90)
    return chr(num)
def xunhuan(shurushu):
    a = 1
    lst = []
    while a <= int(shurushu):
        b = suijishengcheng()
        lst.append(b)
        a = a + 1
    return lst
class chuli:
    def __init__(self):
        self.geshu = input('输入的个数：').strip()
        self.yaoshuruneirong = xunhuan(self.geshu)
        self.dui = 0
        self.cuo = 0
        self.shiji = []
        self.time = 0
    def shuru(self):
        print("""
注意事项：
    1.在输入的时候，请注意不要输入错位。因技术限制，可能输错位1个，就有可能导致全错。
    2.请务必输全，若不敢保证，可以在输入完的时候随便输入。    
    3.在输入的时候，请不要输入空格。       
        """)
        time.sleep(20)
        print('--------------')
        time.sleep(5)
        print('你要输入的内容：',self.yaoshuruneirong)
        self.time_before = time.time()
        self.b = input('请输入：').strip().upper()
        self.time_after = time.time()
    def xiaoyan(self):
        for str in self.b:
            self.shiji.append(str)
        try:
            for xiaoyanduixiang in range(len(self.yaoshuruneirong)):
                if self.yaoshuruneirong[xiaoyanduixiang] == self.shiji[xiaoyanduixiang]:
                    self.dui = self.dui + 1
                else:
                    self.cuo = self.cuo + 1
        except IndexError:
            print('你输入少了')
    def xianshi(self):
        print('你要输入的内容：',self.yaoshuruneirong)
        print('实际输入的内容：',self.shiji)
        print('正确个数：',self.dui)
        print('错误个数：',self.cuo)
        print('你要输入的个数：',len(self.yaoshuruneirong))
        print('你实际输入的个数：',len(self.shiji))
        print('正确率：',self.dui/(len(self.yaoshuruneirong))*100,'%')
        print('输入所用时间：',self.time_after-self.time_before,'s')
b = chuli()
b.shuru()
b.xiaoyan()
b.xianshi()