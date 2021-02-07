#-*-coding:GBK -*-
import json
import random
def yanzheng(uid,mima):
    try:
        file = open(f'E:/编程文件/Python/dubomoni/4.0数据存储/{uid}.json', mode='r', encoding='utf-8')
    except FileNotFoundError:
        return 'no'
    file_str = file.read()
    file_dic = json.loads(file_str)
    if str(file_dic['uid']) == uid  and file_dic['mima'] == mima:
        file.close()
        return file_dic
    else:
        return 'no'


def zhuce(zhuceyonghu,zhucemi):
    dic = {'uid':None,'name': None, 'mima': None, 'dubi': None, 'shifoulingqian': None, 'vip': None,
                        'guizudian': None,'xinxi':'无'}
    lst = []
    if zhuceyonghu == 'PengPeng3g' and zhucemi == '17720080806aa':
        return '管理员'
    else:
        zhufilestr = open('E:/编程文件/Python/dubomoni/4.0数据存储/uid数.json',mode = 'r',encoding = 'utf-8')
        zhucefiledic = zhufilestr.read()
        zhulst = json.loads(zhucefiledic)
        zhuuid = int(zhulst[0])
        zhuuid = zhuuid+1
        dic['uid'] = zhuuid
        dic['name'] = zhuceyonghu
        dic['mima'] = zhucemi
        dic['dubi'],dic['vip'],dic['guizudian'],dic['shifoulingqian'] = 0,0,0,'False'
        lst.append(zhuuid)
        json.dump(dic,open(f'E:/编程文件/Python/dubomoni/4.0数据存储/{zhuuid}.json',encoding='utf-8',mode = 'w'))
        json.dump(lst,open(f'E:/编程文件/Python/dubomoni/4.0数据存储/uid数.json',mode = 'w',encoding = 'utf-8'))
        zhufilestr.close()
        return lst[0]
def chongzhixiugai(uid,chongzhidubi):
    file = open(f'4.0数据存储/{uid}.json','r',encoding = 'utf-8')
    filestr = file.read()
    filedic = json.loads(filestr)
    vip = filedic['vip']
    dubi = filedic['dubi']
    vipdian = filedic['guizudian']
    dubi = dubi + int(chongzhidubi)
    vipdian = vipdian + int(chongzhidubi)
    if vipdian > 60000 and vip == 10:
        pass
    elif vipdian > 60000:
        vip = '10'
    elif vipdian > 50000:
        vip = '9'
    elif vipdian > 45000:
        vip = '8'
    elif vipdian > 40000:
        vip = '7'
    elif vipdian > 30000:
        vip = '6'
    elif vipdian > 25000:
        vip = '5'
    elif vipdian > 20000:
        vip = '4'
    elif vipdian > 10000:
        vip = '3'
    elif vipdian > 5000:
        vip = '2'
    elif vipdian > 1:
        vip = '1'
    filedic['vip'],filedic['guizudian'],filedic['dubi'] = vip,vipdian,dubi
    file.close()
    json.dump(filedic,open(f'4.0数据存储/{uid}.json',mode ='w',encoding='utf-8'))
def game(uid,jingcaishu,suijishu,zhu):
    if jingcaishu == suijishu:
        zhu = int(zhu)
        jieguo = '你赢了！！！'
        duxiubi(uid,zhu)
        return jieguo
    else:
        zhu = -int(zhu)
        jieguo = '你输了！！！'
        duxiubi(uid,zhu)
        return jieguo
def duxiubi(uid,dubi):
    file = open(f'4.0数据存储/{uid}.json','r',encoding = 'utf-8')
    filestr = file.read()
    filedic = json.loads(filestr)
    filedic['dubi']  = int(filedic['dubi']) + int(dubi)
    json.dump(filedic,open(f'4.0数据存储/{uid}.json','w',encoding = 'utf-8'))
    file.close()
def guanxiu(uid,xiugaixiang,zhi,gonghao):
    if gonghao == 'PengPeng3g':
        file = open(f'4.0数据存储/{uid}.json','r',encoding='utf-8')
        filestr = file.read()
        filedic = json.loads(filestr)
        filedic[xiugaixiang] = zhi
        json.dump(filedic,open(f'4.0数据存储/{uid}.json','w',encoding='utf-8'))
        file.close()
    else:
        return '非管理员'