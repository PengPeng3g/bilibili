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
        return render_template('hello.html',chenggong = '���ѵ�¼�ɹ�')
@app.route('/guizedeng')
def guizedeng():
    a = """
    ����ʱ��������һ�����������
    ����������Լ���Ϊ������
    ���������������������ַ�
    ������֮��ʼ����ע
    ע��Ϊ������
    һ���ǴΣ�һ���ǵ�
    �����һ����ǵ׵Ĵδη�
    Ӯ�û���õ�������
    ��Ļ���õ����������෴��
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
    if a == '����Ա':
        return render_template('guanliyuanjin.html')
    b = '��������uid:'+str(a)
    zhuce = 'ע��ɹ������¼'
    return render_template('hello.html',zhuce = zhuce,uuid = b)
@app.route('/chushi')
def chushi():
    global xinxi
    fil = open(f'4.0���ݴ洢/{uid}.json','r',encoding='utf-8')
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
    return render_template('chongzhi.html',jieguo = '�Ѿ���ֵ��ϣ������˳���ť')
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
    return render_template('game.html',jieguo = jieguo,suijishu = suijishu,jingcaishu = jingcaishu,ha = '����˳����س�ʼ����')
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
    if a == '�ǹ���Ա':
        return render_template('feiguanliyuan.html')
    else:
        return render_template('guanxiu.html',jieguo = '�޸ĳɹ�')
if __name__ == '__main__':
    app.run()