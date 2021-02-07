#-*-coding:GBK -*-
from flask import Flask,request,render_template
import dubomonisimo
import json
import random
app = Flask(__name__)
uid = ''
mima = ''
xinxi = ''
@app.route('/')
def hello():
    return render_template('hello.html')
@app.route('/denglu',methods = ['POST'])
def yazheng():
    global uid,mima
    uid = request.form.get('name')
    mima = request.form.get('mima')
    a = dubomonisimo.yanzheng(uid,mima)
    if a == 'no':
        return render_template('denglushibai.html')
    else:
        return render_template('hello.html',chenggong = '您已登录成功')
@app.route('/guizedeng')
def guizedeng():
    a = """
    游玩时，会生成一个随机的数字
    玩家需输入自己认为的数字
    不得输入除数字外的其他字符
    输入完之后开始输入注
    注分为两部分
    一个是次，一个是底
    组合在一起就是底的次次方
    赢得话会得到这个结果
    输的话会得到这个结果的相反数
    """
    return render_template('guizedeng.html',guize = a)
@app.route('/zhuce')
def zhuce():
    return render_template('zhuce.html')
@app.route('/zhucechu',methods = ['POST'])
def zhucechu():
    ming = request.form.get('zhuceming')
    mima = request.form.get('zhucemima')
    a = dubomonisimo.zhuce(ming,mima)
    if a == '管理员':
        return render_template('guanliyuanjin.html')
    b = '这是您的uid:'+str(a)
    zhuce = '注册成功，请登录'
    return render_template('hello.html',zhuce = zhuce,uuid = b)
@app.route('/chushi')
def chushi():
    global xinxi
    fil = open(f'4.0数据存储/{uid}.json','r',encoding='utf-8')
    fi = fil.read()
    file = json.loads(fi)
    dubi = file['dubi']
    vip = file['vip']
    guizudian = file['guizudian']
    shifoulingqian = file['shifoulingqian']
    xinxi = file['xinxi']
    name = file['name']
    return render_template('gamestarts.html',uid = uid,dubi = dubi,vip = vip,guizudian = guizudian,shifoulingqian = shifoulingqian,xinxi = xinxi,name = name)
@app.route('/guanliyuanxinxi')
def guanliyuanxinxi():
    return render_template('guanliyuanxinxi.html',guanliyuanxinxi = xinxi)
@app.route('/chongzhi')
def chongzhi():
    return render_template('chongzhi.html')
@app.route('/chongzhichuli',methods = ['POST'])
def chongchu():
    chongzhishu = request.form.get('chongzhishu')
    uidd = request.form.get('uidd')
    dubomonisimo.chongzhixiugai(uidd,chongzhishu)
    return render_template('chongzhi.html',jieguo = '已经充值完毕，请点击退出按钮')
@app.route('/game')
def game():
    return render_template('game.html')
@app.route('/gamec',methods = ['POST'])
def chulig():
    jingcaishu = request.form.get('jingcaishu')
    dishu  = request.form.get('dishu')
    cishu = request.form.get('cishu')
    suijishu = random.randint(0,8800)
    zhu = int(dishu) ** int(cishu)
    jieguo = dubomonisimo.game(uid,jingcaishu,suijishu,zhu)
    return render_template('game.html',jieguo = jieguo,suijishu = suijishu,jingcaishu = jingcaishu,ha = '点击退出返回初始界面')
@app.route('/guanliyuan')
def guanliyuan():
    return render_template('guanliyuan.html')
@app.route('/guanliyuan/xiugai')
def guanxiu():
    return render_template('guanxiu.html')
@app.route('/guanliyuan/xiugai/chuli',methods = ['POST'])
def guanchuxiu():
    uid = request.form.get('uid')
    xiugaixiang = request.form.get('xiugaixiang')
    zhi = request.form.get('zhi')
    gonghao = request.form.get('gonghao')
    a = dubomonisimo.guanxiu(uid,xiugaixiang,zhi,gonghao)
    if a == '非管理员':
        return render_template('feiguanliyuan.html')
    else:
        return render_template('guanxiu.html',jieguo = '修改成功')
if __name__ == '__main__':
    app.run()