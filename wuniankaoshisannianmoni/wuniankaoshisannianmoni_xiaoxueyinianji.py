"""
五年考试三年模拟小学二年级版
编译者：PengPeng3g
说明：运行此程序时，python编译器版本为3.5以上
"""
a = """
**绝密·启用前
2019~2020学年度二年级期末考试
    90分钟 满分：100分
         数学

一．填空。（20分）
1.1m=（ ）cm，1张课桌的长度=60（ ）
2.小明拿了20元钱，小牛拿的钱数比小明少5元，小牛拿了（ ）元？
3.锐角比直角（ ），钝角比直角（ ），钝角比锐角（ ）。
4.小明有3颗糖，小黄的颗数是小明的3倍，小黄有（ ）颗糖。
5.大象有3只，猴子的只数是大象的5倍，猴子（  ）只。
6.小明有14元钱，小张的钱数比小明少6元，小张有（  ）元。
二．判断（10分）
1.一支铅笔的长度是5米。                                                               （）
2.45+37=72                                                                        （）
3.小明有3元钱，小张的钱数比小明的钱数少4元。                                              （）
4.用1，2，3组合数字，可以组成6个两位数。                                                 （）
5.78-29=49                                                                         （）
三．选择（10分）
1.下面时间中，正确的时间是（）。
A.9：90 B.12:34 C.25:20 D.11:87
2.钝角的度数是（）°
A.34 B.67 C.90 D.123
3.锐角的度数是（）°
A.24 B.91 C.90 D.87
4.小明有3元钱，小黄的钱数是小明的6倍，小黄有（）元。
A.9 B.12 C.18 D.10
5.铅笔的长度是（）厘米。
A.100 B.7 C.42 D.0
四．计算。（25分）
1.直接写得数（10分）
3X4=    5X7=    62+74=    87+98=    9X8=    98-76=    37-29=
87-42=    7X9=    8X8=

2.拖式计算。（15分）
5X7-4          62-37+42         7X9+9       9+9+9       43+28-31




五．操作题。（10分）
1.画一个135°的角。（2分）



2.画一个钟表，然后在你画的钟表中标出22：30。 （4分）



         
3.请你用图表现出3X2=6（4分）
 
六．应用题（25分）
1.小明，爸爸和妈妈一起吃饭，小明，爸爸和妈妈每个人每顿饭都用1双一次性筷子，那么小明一家一天用去多少个一次性筷子？（6分）





2.动物园有大象5只，猴子的只数是大象的3倍多5只，猴子有多少只？（3分）






3.二（1）班有30人，二（2）班的人数比二（1）班人数多4人，一（1）班人数是二（2）班人数的2倍还少4人，一（1）班有多少人？（6分）






4.课桌的长度是50厘米，黑板的长度是课桌的2倍，黑板多少米？（5分）





5.在一次做题比赛中，小明答对了20道题，小任答的题是小明的2倍少10道题，小张答对的题是小任的2倍少15题，小张答对多少道题？（5分）




附加题（20分）
王叔叔砍一棵树，砍下来后将那棵树切了4刀，平均每段长50厘米，那颗树全长多少分米？
                                              

"""
input(a)

b = 0

print('开始答题')

print('注意，出于技术原因，一道小题错了，不管错在哪，不管这道小题对了几个空，一律视作错误，整道小题全部不计分。而且，填完之后不可更改，请三思后行。在答题的过程中，请不要输入空格。')

oneone = input('一.1.请输入答案(第一小小题不用带单位用点分开答案，例如：213.41)：')
if oneone == '100.cm':
    b = b + 4

onetwo = input('一.2.')
if onetwo == '15':
    b = b + 2

onethree = input('一.3.')
if onethree == '小.大.大':
    b = b + 6

onefour = input('一.4.')
if onefour == '9':
    b = b + 2

onefive = input('一.5.')
if onefive == '15':
    b = b + 4

onesix = input('一.6.')
if onesix == '8':
    b = b + 2

print('第二题开始做答（对的填t,错的填f）')

twoone = input('二.1.')
if twoone == 'f':
    b = b + 2

twotwo = input('二.2.')
if twoone == 'f':
    b = b + 2

twothree = input('二.3.')
if twothree == 'f':
    b = b + 2

twofour = input('二.4')
if twofour == 't':
    b = b + 2

twofive = input('二.5.')
if twofive == 't':
    b = b + 2

print('第三题开始作答。（用小写）')

threeone = input('三.1.')
if threeone == 'b':
    b = b + 2

threetwo = input('三.2.')
if threetwo == 'd':
    b = b + 2

threethree = input('三.3.')
if threethree == 'a' or threethree == 'd':
    b = b + 2

threefour = input('三.4.')
if threefour == 'c':
    b = b + 2

threefive = input('三.5.')
if threefive == 'b':
    b = b + 2

print('第四题开始作答(拖式直接得数)')

print('第一题要保证全对，错一个，10分没了，横着写。')

siyi = input('要保证全队哟。四.1.')
if siyi == '12.35.136.185.72.22.8.45.63.64':
    b = b + 10

sitwo = input('要保证全对哟。四.2')
if sitwo == '31.67.72.27.40':
    b = b + 15

print('由于第五题不能在这上面做，系统自动赠予10分。')
b = b + 10

print('第六题开始做答（直接写答案不带单位）')

liuyi = input('六.1.')
if liuyi == '9':
    b = b + 6

liuer = input('六.2')
if liuer == '20':
    b = b + 3

liusan = input('六.3')
if liusan == '64':
    b = b + 6

liusii = input('六.4.')
if liusii == '1':
    b = b + 5

liuwu = input('六.5.')
if liuwu == '30':
    b = b + 5

fujiati = input('附加题')
if fujiati == '25':
    b = b + 20

print('你的分数:',b)

c = (f"""
**绝密·启用前
2019~2020学年度二年级期末考试
    90分钟 满分：100分
         数学

一．填空。（20分）
1.1m=（ ）cm，1张课桌的长度=60（ ）答案:{oneone}
2.小明拿了20元钱，小牛拿的钱数比小明少5元，小牛拿了（ ）元？答案：{onetwo}
3.锐角比直角（ ），钝角比直角（ ），钝角比锐角（ ）。答案：{onethree}
4.小明有3颗糖，小黄的颗数是小明的3倍，小黄有（ ）颗糖。答案：{onefour}
5.大象有3只，猴子的只数是大象的5倍，猴子（  ）只。答案：{onefive}
6.小明有14元钱，小张的钱数比小明少6元，小张有（  ）元。答案：{onesix}
二．判断（10分）
1.一支铅笔的长度是5米。                                                               （{twoone}）
2.45+37=72                                                                        （{twotwo}）
3.小明有3元钱，小张的钱数比小明的钱数少4元。                                              （{twothree}）
4.用1，2，3组合数字，可以组成6个两位数。                                                 （{twofour}）
5.78-29=49                                                                         （{twofive}）
三．选择（10分）
1.下面时间中，正确的时间是（{threeone}）。
A.9：90 B.12:34 C.25:20 D.11:87
2.钝角的度数是（{threetwo}）°
A.34 B.67 C.90 D.123
3.锐角的度数是（{threethree}）°
A.24 B.91 C.90 D.87
4.小明有3元钱，小黄的钱数是小明的6倍，小黄有（{threefour}）元。
A.9 B.12 C.18 D.10
5.铅笔的长度是（{threefive}）厘米。
A.100 B.7 C.42 D.0
四．计算。（25分）
1.直接写得数（10分）
3X4=    5X7=    62+74=    87+98=    9X8=    98-76=    37-29=
87-42=    7X9=    8X8=
答案：{siyi}
2.拖式计算。（15分）
5X7-4          62-37+42         7X9+9       9+9+9       43+28-31
答案：{sitwo}
五．操作题。（10分）
1.画一个135°的角。（2分）



2.画一个钟表，然后在你画的钟表中标出22：30。 （4分）



         
3.请你用图表现出3X2=6（4分）
 
六．应用题（25分）
1.小明，爸爸和妈妈一起吃饭，小明，爸爸和妈妈每个人每顿饭都用1双一次性筷子，那么小明一家一天用去多少个一次性筷子？（6分）

{liuyi}



2.动物园有大象5只，猴子的只数是大象的3倍多5只，猴子有多少只？（3分）

{liuer}




3.二（1）班有30人，二（2）班的人数比二（1）班人数多4人，一（1）班人数是二（2）班人数的2倍还少4人，一（1）班有多少人？（6分）

{liusan}




4.课桌的长度是50厘米，黑板的长度是课桌的2倍，黑板多少米？（5分）

{liusii}



5.在一次做题比赛中，小明答对了20道题，小任答的题是小明的2倍少10道题，小张答对的题是小任的2倍少15题，小张答对多少道题？（5分）

{liuwu}


附加题（20分）
王叔叔砍一棵树，砍下来后将那棵树切了4刀，平均每段长50厘米，那颗树全长多少分米？
{fujiati}
""")

chakanshijuan = input('是否查看您的试卷？查看输入k').strip()

if chakanshijuan == 'k':
    print(c)