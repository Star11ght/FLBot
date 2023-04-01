import receive
import json
import getbag
import changebag
import sendmsg
import jrrp
import random
import change
import getdata
import guessnum
import os
import time
import timecheck
import math
import bomb
import time
import getimages
import shutil
import piano
import requests
import uuid
import picrev
import place
import bank
import datetime
import game1
from ffmpy import FFmpeg
from pixivpy3 import *

def store(message,group,qq,favor):
    if len(message) == 8:
        output = '[CQ:at,qq='+str(qq)+']\n欢迎来到商店！输入fl.store＋空格＋数字即可购买东西XD\n'
        output = output + "——————————————\n"
        output = output + '1 补签卡(断签时可补签，两次断签以上仅补签最近的一次断签区间) - 800积分\n'
        output = output + '2 rp重置卡(可重新测jrrp，rp取今日最高的一次，购买需好感度>=10) - 500积分\n'
        output = output + '3 获得随机零食/饮料 - 100积分\n'
        output = output + '4 钓鱼竿，可前往有大量水资源的地方钓鱼 - 1000积分'
        sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
    elif message[8] != " " or len(message) == 9:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']store后面要加一个空格才能购买东西哦~'})
    else:
        newstore = message[9:]
        money = float(getdata.getsd(qq,5))
        if newstore == '1':
            if(money >= 800):
                money = money - 800
                tnum = getbag.getbags(qq,1) + 1
                changebag.changebags(qq,tnum,1)
                change.changes(qq,money,5)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已购买一张补签卡，包内现有' + str(tnum) + '张。输入fl.use 1即可使用哦~'})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的积分不足，还不能买哦！'})
        elif newstore == '2':
            if(favor >= 10):
                if(money >= 500):
                    money = money - 500
                    tnum = getbag.getbags(qq,2) + 1
                    changebag.changebags(qq,tnum,2)
                    change.changes(qq,money,5)
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已购买一张rp重置卡，包内现有' + str(tnum) + '张。输入fl.use 2可直接使用哦~'})
                else:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的积分不足，还不能买哦！'})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的好感度不够，芙兰还不能卖给你……qwq'})
        elif newstore == '3':
            if(money >= 100):
                money = money - 100
                food = random.randint(3,7)
                tnum = getbag.getbags(qq,food) + 1
                changebag.changebags(qq,tnum,food)
                change.changes(qq,money,5)
                output = '[CQ:at,qq='+str(qq)+']'
                if food == 3:
                    output = output + "您买到了一份⑨转大肠，包内共有" + str(tnum) + "份。嘶……这真的能吃嘛……(可输入fl.use 3使用)"
                elif food == 4:
                    output = output + "您买到了一份草莓蛋糕，包内共有" + str(tnum) + "份。甜甜的草莓加上甜甜的蛋糕，甜蜜程度平方啦——(可输入fl.use 4使用)"
                elif food == 5:
                    output = output + "您买到了一个红苹果，包内共有" + str(tnum) + "个。快给芙兰芙兰想吃！！！(可输入fl.use 5使用)"
                elif food == 6:
                    output = output + "您买到了一杯红茶玛奇朵，包内共有" + str(tnum) + "杯。奶油的味道好香！(可输入fl.use 6使用)"
                elif food == 7:
                    output = output + "您买到了一块冰糖雪糕，包内共有" + str(tnum) + "块。你和冰糖雪梨是什么关系.jpg(可输入fl.use 7使用)"
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的积分不足，还不能买哦！'})
        elif newstore == '4':
            tnum = getbag.getbags(qq,21)
            if(tnum==1):
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的身上已经有一根钓鱼竿辣！！！再买的话恋恋会找你的（捂嘴）'})
            elif(money >= 1000):
                money = money - 1000
                tnum = tnum + 1
                changebag.changebags(qq,tnum,21)
                change.changes(qq,money,5)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已购买一根鱼竿~输入fl.use 21即可在有湖水的地方使用啦！'})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的积分不足，还不能买哦！'})

def bag(group,qq):
    output = '[CQ:at,qq='+str(qq)+']\n当前您的背包里有：'
    empty = 1
    for i in range (1,30):
        n = getbag.getbags(qq,i)
        if n != 0:
            if i == 1:
                output = output + "\n1 补签卡×" + str(n)
            elif i == 2:
                output = output + "\n2 rp重置卡×" + str(n)
            elif i == 3:
                output = output + "\n3 ⑨转大肠×" + str(n)
            elif i == 4:
                output = output + "\n4 草莓蛋糕×" + str(n)
            elif i == 5:
                output = output + "\n5 红苹果×" + str(n)
            elif i == 6:
                output = output + "\n6 红茶玛奇朵×" + str(n)
            elif i == 7:
                output = output + "\n7 冰糖雪糕×" + str(n)
            elif i == 8:
                output = output + "\n8 黑松露炒饭×" + str(n)
            elif i == 9:
                output = output + "\n⑨ 琪露诺冰块×" + str(n)
            elif i == 10:
                output = output + "\n10 冰冻的鱼×" + str(n)
            elif i == 11:
                output = output + "\n11 草莓奶油×" + str(n)
            elif i == 12:
                output = output + "\n12 苹果草莓派×" + str(n)
            elif i == 13:
                output = output + "\n13 雾之矿泉水×" + str(n)
            elif i == 21:
                output = output + "\n21 一根普通的鱼竿"
            elif i == 22:
                output = output + "\n22 烧烤机"
            elif i == 23:
                output = output + "\n23 木棍×" + str(n)
            empty = 0
    if empty == 1:
        output = output + "一片死寂的空气……"
    else:
        output = output + "\n可输入fl.use [物品前的数字]使用哦！"
    sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})

def use(message,group,qq,favor,date):
    if len(message) == 6:
        output = '[CQ:at,qq='+str(qq)+']\n在use之后加空格加数字(物品序号)即可使用该物品！可以发送fl.bag查询物品序号哦~'
        sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
    elif message[6] != " " or len(message) == 7:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']use后面要加一个空格才能使用东西哦~'})
    else:
        newuse = message[7:]
        if newuse == "1":
            tnum = getbag.getbags(qq,1)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                qddate = int(getdata.getsd(qq,6))
                location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'usersdata', str(qq) + '_qdover.txt'))
                if (qddate - date != 0):
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']先去签个到再来使用这个东西吧！'})
                elif not os.path.exists(location):
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你貌似不需要补签的样子！暂时用不了哦~'})
                else:
                    with open(file=location, mode='r', encoding="utf-8") as data:
                        lastqddate = int(data.readline())
                        lastqdren = int(data.readline())
                    qdren = int(getdata.getsd(qq,7)) + 1
                    datemin = qddate - lastqddate
                    reqdtimes = datemin - qdren
                    longestren = lastqdren+datemin
                    if reqdtimes == 0:
                        change.changes(qq,longestren,7)
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']补签成功，您已连续签到' + str(longestren) + '天，已无需再次补签啦~'})
                        os.remove(location)
                    else:
                        change.changes(qq,qdren,7)
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']补签成功，您已连续签到' + str(qdren) + '天，再使用' + str(reqdtimes) + '张补签卡就能连续签到' + str(longestren) + '天了哦！'})
                    tnum = tnum - 1
                changebag.changebags(qq,tnum,1)

                    
        
        elif newuse == "2":
            tnum = getbag.getbags(qq,2)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                orirp = int(jrrp.getjrrp(qq,1))
                newrp = int(jrrp.getjrrp(qq,2))
                if orirp > newrp:
                    output = '[CQ:at,qq='+str(qq)+']你原本的人品值为' + str(orirp) + '，使用rp重置卡后得到的新rp值为' + str(newrp) +'。没有原来的高，将保留原rp。可惜……'
                elif orirp < newrp:
                    output = '[CQ:at,qq='+str(qq)+']你原本的人品值为' + str(orirp) + '，使用rp重置卡后得到的新rp值为' + str(newrp) +'。恭喜刷新今日最高！'
                else:
                    output = '[CQ:at,qq='+str(qq)+']你原本的人品值为' + str(orirp) + '，使用rp重置卡后得到的新rp值为' + str(newrp) +'。这都能一模一样………这得比达到理论最高人品还难了吧orz'
                changebag.changebags(qq,tnum,2)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
        elif newuse == "3":
            tnum = getbag.getbags(qq,3)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                
                if(nowplace == "0"):
                    output = output + '你吃下了⑨转大肠……呃嗯……感觉自己的大肠正在疯狂⑨转中……'
                elif(nowplace == "1"):
                    output = output + '你让⑨吃下了⑨转大肠，⑨的脸部凝聚成了一块……随后逃跑了……然后又回来了。'
                    results = random.uniform(0,100)
                    if results <= 50:
                        money = float(getdata.getsd(qq,5))
                        money = money + 199.99
                        change.changes(qq,money,5)
                        output = output + '\n俗话说得好，baka的记忆只有9秒。她看到你给她的东西里名字带⑨，竟然决定奖励你199.99积分！？！'
                elif(nowplace == "2"):
                    if(favor<15):
                        place.changeplace(str(qq),"2-0")
                        output = output + '你将⑨转大肠送到了美铃的面前。美铃闻了一下之后一边骂着国粹一边到处跑开然后昏倒了……！？是个潜入红魔馆的好机会！（可以输入fl.move 2-X进入红魔馆内部了）'
                    else:
                        output = output + '你将⑨转大肠送到了美铃的面前，美铃闻了一下之后立刻扔掉了。看来谁都不喜欢这道菜捏……'
                elif(nowplace == "2-0"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 250
                    change.changes(qq,money,5)
                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了⑨转大肠。然后你把她熏醒了……？？？她似乎很感谢你在大小姐发现她之前叫醒她，然后给了你150积分……'
                elif(nowplace == "2-1"):
                    money = float(getdata.getsd(qq,5))
                    money = money - 100
                    change.changes(qq,money,5)
                    output = output + '喂！！！你这是拿了个什么东西出来啊喵！！！快点给我扔掉啊啊啊啊啊（掏出莱瓦汀）（乱挥）（……你失去了100积分）'
                elif(nowplace == "2-2"):
                    output = output + '你拿出了⑨转大肠。姆Q貌似对这道菜还挺感兴趣……！？她决定拿另一道菜和你交换。（已获得：'
                    food = random.randint(6,8)
                    tnum2 = getbag.getbags(qq,food) + 1
                    changebag.changebags(qq,tnum2,food)
                    if food == 6:
                        output = output + "6 红茶玛奇朵）"
                    elif food == 7:
                        output = output + "7 冰糖雪糕）"
                    elif food == 8:
                        output = output + "8 黑松露炒饭）"

                elif(nowplace == "2-3"):
                    place.changeplace(str(qq),"2")
                    output = output + '你拿出了⑨转大肠。在你刚拿出的那一刻，女仆长立刻把你送到了红魔馆门口。似乎打扰到她打扫卫生了……'
                    tnum = tnum + 1

                elif(nowplace == "2-4"):
                    place.changeplace(str(qq),"2")
                    output = output + '你拿出了⑨转大肠。在你刚拿出的那一刻，蕾米突然大吼一声“咲夜”。你被赶出去了……'
                    tnum = tnum + 1
                
                changebag.changebags(qq,tnum,3)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "4":
            tnum = getbag.getbags(qq,4)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    output = output + '你吃下了草莓蛋糕。甜甜的，确实好吃！'
                elif(nowplace == "1"):
                    results = random.uniform(0,100)
                    if results <= 50:
                        money = float(getdata.getsd(qq,5))
                        money = money + 199.99
                        change.changes(qq,money,5)
                        output = output + '你让⑨吃下了草莓蛋糕，她很开心，随后丢给了你199.99积分！好耶！'
                    else:
                        output = output + '你让⑨吃下了草莓蛋糕，她很开心，不断吼着“我还要我还要”。看来是没完没了了……'
                elif(nowplace == "2"):
                    if(favor<15):
                        output = output + '你想给美铃吃草莓蛋糕，但显然这种东西还是贿赂不了她啦……'
                    else:
                        output = output + '你想给美铃吃草莓蛋糕，但她拒绝了你的好意。'
                    tnum = tnum + 1
                elif(nowplace == "2-0"):
                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了草莓蛋糕。填饱肚子再进去捏（吐舌头）'
                elif(nowplace == "2-1"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 150
                    change.changes(qq,money,5)
                    output = output + '哦哦哦！草莓蛋糕！！！芙兰最最喜欢吃啦XD（大吃一通）（……你偷偷拿走了150积分）'
                elif(nowplace == "2-2"):
                    output = output + '你拿出了草莓蛋糕。姆Q似乎不感兴趣……！但她还是收下了你的心意。'
                elif(nowplace == "2-3"):
                    results = random.uniform(0,100)
                    if results <= 75:
                        money = float(getdata.getsd(qq,5))
                        money = money + 123
                        change.changes(qq,money,5)
                        output = output + '你拿出了草莓蛋糕。咲夜说她这里正好缺蛋糕……随后拿走了你的蛋糕并给了你123积分。跑腿费才这么点真小气……'
                    else:
                        place.changeplace(str(qq),"2")
                        output = output + '你拿出了草莓蛋糕。在你刚拿出的那一刻，女仆长立刻把你送到了红魔馆门口并没收了你的蛋糕。似乎打扰到她打扫卫生了……怎么不付钱的啊！！！'
                elif(nowplace == "2-4"):
                    results = random.uniform(0,100)
                    if results <= 50:
                        money = float(getdata.getsd(qq,5))
                        money = money + 222
                        change.changes(qq,money,5)
                        output = output + '你拿出了草莓蛋糕。蕾米突然跑了下来一把塞进了嘴里。嘶……她可真急……你得到了222积分。'
                    else:
                        output = output + '你拿出了草莓蛋糕。蕾米突然跑了下来一把塞进了嘴里，但她吃得太快呛着了……真是威严满满啊（便乘）'
                
                changebag.changebags(qq,tnum,4)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "5":
            tnum = getbag.getbags(qq,5)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    output = output + '你吃下了红苹果。一天一苹果，永琳远离我（大雾）'
                    results = random.uniform(0,100)
                    if results <= 75:
                        money = float(getdata.getsd(qq,5))
                        money = money + 150
                        change.changes(qq,money,5)
                        output = output + '\n吃完苹果后，你突然感觉到身上充满了破坏一切的力量，转瞬即逝……随后获得了150积分！？'
                elif(nowplace == "1"):
                    output = output + '你让⑨吃下了苹果，她似乎不是很喜欢吃水果，真是个挑食的孩子XD'
                elif(nowplace == "2"):
                    if(favor<15):
                        output = output + '你想给美铃吃红苹果，但显然这种东西还是贿赂不了她啦……'
                    else:
                        output = output + '你想给美铃吃草莓蛋糕，但她拒绝了你的好意，说芙兰最喜欢吃这个了，可以去带给她吃！嗯嗯嗯她说的对（飞来飞去）'
                    tnum = tnum + 1
                elif(nowplace == "2-0"):
                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了红苹果。水果果然还是填饱不了肚子啦！'
                elif(nowplace == "2-1"):
                    output = output + '芙兰最喜欢吃苹果啦！阿卡伊阿麻伊！（大口大口咀嚼）'
                    results = random.uniform(0,100)
                    if results <= 50 - favor * 2:
                        money = int(getdata.getsd(qq,2))
                        money = money + 1
                        change.changes(qq,money,2)
                        output = output + '\n芙兰吃得好开心！谢谢你！！！（试图扑向你的怀中）（你躲开了…………并增加了1点好感值）'
                    elif favor >= 25 and results <= 10:
                        money = float(getdata.getsd(qq,5))
                        money = money + 500
                        change.changes(qq,money,5)
                        output = output + '\n芙兰吃得好开心！谢谢你！！！（你得到了500积分）'
                    
                elif(nowplace == "2-2"):
                    output = output + '你拿出了红苹果，姆Q的建议是拿给芙兰吃，因此你收了回去。'
                    tnum = tnum + 1
                elif(nowplace == "2-3"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 111
                    change.changes(qq,money,5)
                    output = output + '你拿出了红苹果，咲夜似乎想收下这个苹果。她感谢你并给了你111积分。'
                elif(nowplace == "2-4"):
                    results = random.uniform(0,100)
                    if results <= 40 - favor * 2:
                        money = int(getdata.getsd(qq,2))
                        money = money + 1
                        change.changes(qq,money,2)
                        output = output + '你拿出了红苹果。蕾米好像也很喜欢吃！不愧是姐妹俩……但她拒绝和你培养好感度，所以她通过改变命运的力量将你和芙兰的好感度提升了1点。什么鬼！'
                    elif favor >= 20 and results <= 25:
                        money = float(getdata.getsd(qq,5))
                        money = money + 150
                        change.changes(qq,money,5)
                        output = output + '你拿出了红苹果。蕾米收下了，似乎想拿给妹妹吃……向你支付了150P。小赚！'
                    else:
                        money = float(getdata.getsd(qq,5))
                        money = money + 50
                        change.changes(qq,money,5)
                        output = output + '你拿出了红苹果。蕾米收下了，似乎想拿给妹妹吃……向你支付了50P。红魔馆里头物价这么低的吗（恼）'

                changebag.changebags(qq,tnum,5)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "6":
            tnum = getbag.getbags(qq,6)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    output = output + '你喝下了红茶玛奇朵。一杯喝下去整天都有好心情~'
                elif(nowplace == "1"):
                    output = output + '你让⑨喝下了红茶玛奇朵。烫死啦！！！她噗的一声就吐了出来……真浪费喵'
                elif(nowplace == "2"):
                    if(favor<15):
                        output = output + '你想让美铃喝红茶玛奇朵，她喝了下去，精神状态爆发！！！等等你这样不就更难潜入了……'
                    else:
                        place.changeplace(str(qq),"2-0")
                        output = output + '你让美铃喝下了红茶玛奇朵。什么！这竟然是昏睡红茶！？她昏倒了……希望别被大小姐发现'
                elif(nowplace == "2-0"):
                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己喝下了红茶玛奇朵。这种东西要让她喝才怪咧！！！'
                elif(nowplace == "2-1"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 50
                    change.changes(qq,money,5)
                    output = output + '哦哦哦！是红茶！谢谢你给我带了红茶！！！（飞奔上去喝）（已获得50积分）'
                    results = random.uniform(0,100)
                    if (results <= 30 - favor * 2) or (favor >= 15 and results <= 2):
                        money = int(getdata.getsd(qq,2))
                        money = money + 1
                        change.changes(qq,money,2)
                        output = output + '\n芙兰喝得好开心！谢谢你！！！（试图扑向你的怀中）（你被推倒了……？！星光震怒……并增加了1点好感值）'
                elif(nowplace == "2-2"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 100
                    change.changes(qq,money,5)
                    output = output + '你拿出了红茶玛奇朵，姆q似乎很喜欢喝，并向你支付了100积分。等等这不带跑路费的嘛！！！'
                elif(nowplace == "2-3"):
                    money = float(getdata.getsd(qq,5))
                    output = output + '你拿出了红茶玛奇朵，咲夜喝了一口，神清气爽！'
                    results = random.uniform(0,100)
                    if results <= 50:
                        money = money + 50
                        output = output + '但好像影响到了她打扫卫生……她只给了你50积分。'
                    else:
                        money = money + 150
                        output = output + '她似乎非常感谢你，给了你150积分。'
                    change.changes(qq,money,5)

                elif(nowplace == "2-4"):
                    results = random.uniform(0,100)
                    output = output + '你拿出了红茶玛奇朵，但蕾米好像正在喝红酒！你收回去了。'
                    tnum = tnum + 1
                
                changebag.changebags(qq,tnum,6)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "7":
            tnum = getbag.getbags(qq,7)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    output = output + '你吃下了冰糖雪糕。冰冰的甜甜的，有一种吃⑨的感觉捏（雾）'
                elif(nowplace == "1"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 149.99
                    change.changes(qq,money,5)
                    output = output + '你让⑨吃下了冰糖雪糕，⑨高兴地跳了起来，大吼着想给你一百万亿积分。于是你借给了她一百万亿，然后她给了你一百万亿＋149.99积分。嗯……多此一举'
                elif(nowplace == "2"):
                    if(favor<15):
                        output = output + '你想让美铃吃冰糖雪糕，但她好像并不是很喜欢⑨的样子……还回来了。'
                    else:
                        output = output + '你想让美铃吃冰糖雪糕，她拒绝了你的好意……还回来了。'
                    tnum = tnum + 1
                elif(nowplace == "2-0"):
                    results = random.uniform(0,100)
                    if results <= 40:
                        money = float(getdata.getsd(qq,5))
                        money = money + 250
                        change.changes(qq,money,5)
                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你吃下了冰糖雪糕。你边吃边看着美铃，什么！她裙子旁边竟然夹着250积分！？嗯……反正她睡着了就直接拿走罢（心虚）'
                    else:
                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你吃下了冰糖雪糕。你边吃边看着美铃。嗯……真凉快！'
                elif(nowplace == "2-1"):
                    output = output + '唔……芙兰并不是很喜欢吃雪糕呢……但谢谢你的好意啦！XD'
                elif(nowplace == "2-2"):
                    output = output + '你拿出了冰糖雪糕，姆q一把夺过，并指责你不能在图书馆里吃零食。呃……怎么别的食物就可以在图书馆里吃呢……'
                elif(nowplace == "2-3"):
                    output = output + '你拿出了冰糖雪糕，咲夜看了一眼，建议你在外面自己吃掉。看来并没有收下……'
                    tnum = tnum + 1
                elif(nowplace == "2-4"):
                    results = random.uniform(0,100)
                    if results <= 50:
                        money = float(getdata.getsd(qq,5))
                        money = money + 229.99
                        change.changes(qq,money,5)
                        output = output + '你拿出了冰糖雪糕。蕾米似乎心生一计，拿229.99积分换下了雪糕。(吸血)鬼知道她在想什么！'
                    else:
                        output = output + '你拿出了冰糖雪糕。蕾米不喜欢吃，但她还是吃下去了……'

                changebag.changebags(qq,tnum,7)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "8":
            tnum = getbag.getbags(qq,8)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 200
                    change.changes(qq,money,5)
                    output = output + '你吃下了黑松露炒饭。太好吃辣！！！你直奔出家门在人间之里大吼大叫跑了一圈，别人以为你是抢积分的妖怪，直接给你扔了200积分……喵？'
                elif(nowplace == "1"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 199.99
                    change.changes(qq,money,5)
                    output = output + '你让⑨吃下了黑松露炒饭，⑨不喜欢吃热的东西。但是！她竟然朝你丢了笨蛋积分！（已获得199.99积分）'
                elif(nowplace == "2"):
                    if(favor<15):
                        output = output + '你想让美铃吃黑松露炒饭，她好像吃腻了的样子……还回来了。'
                    else:
                        output = output + '你想让美铃吃黑松露炒饭，她拒绝了你的好意……还回来了。'
                    tnum = tnum + 1
                elif(nowplace == "2-0"):
                    results = random.uniform(0,100)
                    if results <= 50:
                        money = float(getdata.getsd(qq,5))
                        money = money + 300
                        change.changes(qq,money,5)
                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了黑松露炒饭。香气扑鼻啊！立刻引来了一帮妖怪想吃你的东西，随后丢下钱走了。还好没吵醒美铃……（已获得积分：300）'
                    else:
                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了黑松露炒饭。香气扑鼻啊！'
                elif(nowplace == "2-1"):
                    output = output + '是黑松露炒饭诶！虽然并没有特别喜欢松露，但是加上了炒饭真的好香！（大口大口咀嚼）'
                    results = random.uniform(0,100)
                    if (results <= 60 - favor * 2) or (favor>=30 and results <= 1):
                        money = int(getdata.getsd(qq,2))
                        money = money + 2
                        change.changes(qq,money,2)
                        output = output + '\n芙兰吃得好开心！谢谢你！！！（试图扑向你的怀中）（你接住了，增加了2点好感值）'
                    elif results <= 60:
                        money = float(getdata.getsd(qq,5))
                        money = money + 200
                        change.changes(qq,money,5)
                        output = output + '\n芙兰吃得好开心！谢谢你！作为回礼，芙兰奖励你一些积分吧！（已获得200积分）'
                elif(nowplace == "2-2"):
                    output = output + '你拿出了黑松露炒饭，姆q表示自己这里有一大堆实验品，你决定收回……啥？实验品？？？'
                    tnum = tnum + 1
                elif(nowplace == "2-3"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 220
                    change.changes(qq,money,5)
                    output = output + '你拿出了黑松露炒饭，咲夜好像很饿，她吃了下去，然后给了你220P……等等她为什么自己不做一份呢'
                elif(nowplace == "2-4"):
                    output = output + '你拿出了黑松露炒饭，蕾米说她家女仆天天给她做这个，建议还是拿给她妹妹吃。'
                    tnum = tnum + 1

                changebag.changebags(qq,tnum,8)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "9" or newuse == "⑨":
            tnum = getbag.getbags(qq,9)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    output = output + '你将琪露诺冰块含在嘴里。冰冰凉凉的，还带一丝甜味……心情愉悦！'
                elif(nowplace == "1"):
                    output = output + '你将⑨丢给了⑨，⑨看到了自己的分身，很开心！然后⑨把⑨丢进了雾之湖里……蛤？'
                elif(nowplace == "2"):
                    output = output + '你把冰块丢给了美铃，美铃觉得碍事，一脚踢走了……你捡了回来。'
                    tnum = tnum + 1
                elif(nowplace == "2-0"):
                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你含住了冰块。解渴！'
                elif(nowplace == "2-1"):
                    output = output + '竟然是冰块！一定是从湖边那只冰妖精中拿来的吧……（笑）真有趣！（接过之后捂在胸口）（没过一会儿融化了……）'
                elif(nowplace == "2-2"):
                    output = output + '你拿出了冰块向姆Q展示。见怪不怪！她说道。于是你收了回去……'
                    tnum = tnum + 1
                elif(nowplace == "2-3"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 100
                    change.changes(qq,money,5)
                    output = output + '你向女仆长展示了冰块，女仆似乎正缺一些冰块，她向你道谢后并给了你100积分。'
                elif(nowplace == "2-4"):
                    output = output + '你拿出了冰块，试图向蕾米展现溜冰技术。蕾米展开了翅膀，试图向你展示飞行技术。冰块融化了……'
                changebag.changebags(qq,tnum,9)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "10":
            tnum = getbag.getbags(qq,10)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    output = output + '你拿出了冰冻的鱼仔细欣赏，它似乎在冰块里朝你眨眼……好吓人！'
                    tnum = tnum + 1
                elif(nowplace == "1"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 100
                    change.changes(qq,money,5)
                    output = output + '你将冰冻的鱼丢给了⑨，它突然变成了若鹭姬！！！于是⑨和若鹭姬开心地玩耍了起来………你获得了100积分。'
                elif(nowplace == "2"):
                    output = output + '你将冰冻的鱼拿给美铃看，美铃建议你烤熟后再吃不然会喷射。'
                    tnum = tnum + 1
                elif(nowplace == "2-0"):
                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你抱着冰冻的鱼睡着了。欧亚斯密！'
                    tnum = tnum + 1
                elif(nowplace == "2-1"):
                    output = output + '哇哦！竟然是条冰冻的鱼！芙兰好想吃…………但它竟然是生的！orz'
                    tnum = tnum + 1
                elif(nowplace == "2-2"):
                    output = output + '你拿出了冰冻的鱼向姆Q展示。好臭的鱼腥味！她将你的鱼没收了……'
                elif(nowplace == "2-3"):
                    results = random.uniform(0,100)
                    if results <= 50:
                        money = float(getdata.getsd(qq,5))
                        money = money + 200
                        change.changes(qq,money,5)
                        output = output + '你向女仆长展示了冰冻的鱼，女仆今晚似乎正想给蕾米做鱼肉吃，她向你道谢后并给了你200积分。'
                    else:
                        output = output + '你向女仆长展示了冰冻的鱼，女仆认为你打扰了她打扫卫生，于是将鱼收走了……'
                elif(nowplace == "2-4"):
                    output = output + '你拿出了冰冻的鱼，想和蕾米一起分享。蕾米只对你身上的血感兴趣。危！（流口水）'
                    tnum = tnum + 1
                changebag.changebags(qq,tnum,10)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
        elif newuse == "11":
            tnum = getbag.getbags(qq,11)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                tnum = tnum - 1
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                if(nowplace == "0"):
                    output = output + '你生吞下了草莓奶油。嗯……很好喝……但这也太腻了吧！？'
                elif(nowplace == "1"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 220
                    change.changes(qq,money,5)
                    output = output + '你将草莓奶油递给了baka，baka最喜欢这种甜甜的东西啦！你从她身上拿到了220积分。'
                elif(nowplace == "2"):
                    output = output + '你将草莓奶油拿给美铃看，美铃建议你将草莓奶油和别的东西混合做成新食物吃。'
                    tnum = tnum + 1
                elif(nowplace == "2-0"):
                    place.changeplace(str(qq),"2")
                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你试图用奶油泼醒她。真的泼醒了草！'
                elif(nowplace == "2-1"):
                    output = output + '哇哦！是草莓奶油耶！要是能和别的食物混在一起吃一定很好吃吧………'
                    tnum = tnum + 1
                elif(nowplace == "2-2"):
                    money = float(getdata.getsd(qq,5))
                    money = money + 220
                    change.changes(qq,money,5)
                    output = output + '你拿出了草莓奶油。姆Q似乎想研究研究，于是她向你支付了220积分收下了这瓶奶油。'
                elif(nowplace == "2-3"):
                    results = random.uniform(0,100)
                    if results <= 30:
                        money = float(getdata.getsd(qq,5))
                        money = money + 300
                        change.changes(qq,money,5)
                        output = output + '你向女仆长展示了草莓奶油，红魔馆似乎正缺奶油……她向你道谢后并给了你300积分。'
                    else:
                        money = float(getdata.getsd(qq,5))
                        money = money + 50
                        change.changes(qq,money,5)
                        output = output + '你向女仆长展示了草莓奶油。女仆表示自己这里还有很多，但感谢你的帮助……给了你50积分。'
                elif(nowplace == "2-4"):
                    output = output + '你拿出了草莓奶油。蕾米好像对原料不感兴趣……'
                    tnum = tnum + 1
                changebag.changebags(qq,tnum,11)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})

        elif newuse == "12":
            tnum = getbag.getbags(qq,12)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']当你刚想拿出苹果草莓派时，突然钻出一只暗黑色的星光吃掉了你手上的草莓派。感谢你对他加快完成代码速度作出的巨大贡献！作为回报，他送给了你一个苹果草莓派。'})

        elif newuse == "13":
            tnum = getbag.getbags(qq,13)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你竟然知道星光口渴了，阿里嘎多矿泉水桑！（一口喝下）（被呛到）（一口吐出来）（归还）还是等我写完代码再用罢（咳嗽）'})

        elif newuse == "23":
            tnum = getbag.getbags(qq,23)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']为什么要在这里用木棍，你是不是有什么非分之想！建议对星光使用（发热吐舌头）'})
        elif newuse == "21":
            tnum = getbag.getbags(qq,21)
            
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                nowplace = place.checkplace(qq)
                output = '[CQ:at,qq='+str(qq)+']'
                
                if(nowplace == "0"):
                    output = output + '你在家里练习着挥舞鱼竿。嗯，很有感觉！似乎钓上东西的概率成功了不少……（心理作用罢了.jpg）'

                elif(nowplace == "1"):
                    url = os.path.abspath(os.path.join(os.path.dirname(__file__), 'usersdata', str(qq)+'_angle.txt'))
                    if not os.path.exists(url):
                        with open(file=url, mode='w', encoding="utf-8") as data:
                            data.write(str(date)+'\n')
                            data.write("0\n")
                            data.close()
                    
                    with open(file=url, mode='r', encoding="utf-8") as data:
                        dateangle = data.readline()
                        if int(date) != int(dateangle):
                            dateangle = str(date)
                            times = 0
                        else:
                            times = int(data.readline())
                        
                    needmoney = (times-4)*200
                    money = float(getdata.getsd(qq,5))
                    if money >= needmoney:
                        if times >= 5:
                            output = output + '花费了' + str(needmoney) + '积分进行第' + str(times+1) + '次钓鱼，下一次需要花费' + str(needmoney+200) + '积分……\n'
                            money = money - needmoney
                            change.changes(qq,money,5)
                        else:
                            output = output + '今日第' + str(times+1) + '次钓鱼，第6次开始收费200积分……\n'
                        times = times + 1

                        with open(file=url, mode='w', encoding="utf-8") as data:
                            data.write(str(date)+'\n')
                            data.write(str(times)+"\n")
                            data.close()

                        output = output + '你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……'
                        output = output + '\n突然感觉到钩子有动静！你使劲往上一拉——'
                        results = random.uniform(0,55)
                        if results <= 22:
                            output = output + '\n恭喜你钓到了一根钓鱼竿！你认为这个钓鱼竿很适合你，于是把你原本的钓鱼竿丢掉了……'
                        elif results <= 24:
                            tnum2 = getbag.getbags(qq,2) + 1
                            changebag.changebags(qq,tnum2,2)
                            output = output + '\n恭喜你钓到了一张rp重置卡！输入fl.use 2即可使用啦！等等谁会把这种东西丢进去啊喂！'
                        elif results > 24 and results <= 49:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                            if results <= 25:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=芙兰朵露'
                            elif results <= 26:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=琪露诺'
                            elif results <= 27:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=博丽灵梦'
                            elif results <= 28:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=雾雨魔理沙'
                            elif results <= 29:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=爱丽丝&tag=东方'
                            elif results <= 30:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=蕾米莉亚'
                            elif results <= 31:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=古明地恋'
                            elif results <= 32:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=古明地觉'
                            elif results <= 33:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=幽幽子'
                            elif results <= 34:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=魂魄妖梦'
                            elif results <= 35:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=射命丸文'
                            elif results <= 36:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=十六夜咲夜'
                            elif results <= 37:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=帕秋莉'
                            elif results <= 38:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=东风谷早苗'
                            elif results <= 39:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=河城荷取'
                            elif results <= 40:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=露米娅'
                            elif results <= 41:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=八云紫'
                            elif results <= 42:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=八云蓝'
                            elif results <= 43:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=橙&tag=东方'
                            elif results <= 44:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=上白泽慧音'
                            elif results <= 45:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=蓬莱山辉夜'
                            elif results <= 46:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=多多良小伞'
                            elif results <= 47:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=键山雏'
                            elif results <= 48:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=火焰猫燐'
                            elif results <= 49:
                                urls = 'https://api.lolicon.app/setu/v2?size=thumb&tag=灵乌路空'
                            
                            r = requests.get(urls).content.decode('UTF-8')
                            start = r.find("https")
                            end = r.find("}}]}")
                            imglo = r.find("img-master")
                            end = end - 1
                            pid_start = r.find("pid") + 5
                            p_start = r.find("\"p\"") + 4
                            uid_start = r.find("uid") + 5
                            title_start = r.find("title") + 8
                            author_start = r.find("author") + 9
                            author_end = r.find("r18") - 3
                            msg_pid = r[pid_start:p_start-5]
                            msg_p = r[p_start:uid_start-7]
                            msg_uid = r[uid_start:title_start-10]
                            msg_title = r[title_start:author_start-12]
                            msg_author = r[author_start:author_end]
                            print(msg_pid + msg_p + msg_uid + msg_title + msg_author)
                            mas = r.find("square")
                            originalpic = "https://i.pixiv.re/" + r[imglo:mas] + "square1200."
                            if r[end - 3:end] == "jpg":
                                originalpic =  originalpic + "jpg"
                            else:
                                originalpic =  originalpic + "png"
                            print(r[start:end])
                            if results <= 25:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n恭喜你钓到了一只可爱的芙兰酱~说起来为什么芙兰会在湖里游泳来着（疑惑）\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 26:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n恭喜你钓到了一只baka！唔……这是不是意味着你救了她一命……\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 27:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你竟然钓到了一只差点淹死的乐园的巫女……灵梦！这是异变啊！！！\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 28:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只普通的魔法使！或许她原本就在这里游泳来着被你给钓上来了……？？？\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 29:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只七色的人偶师！她好像本来就在这儿和她的人偶游泳……是在测试防水性嘛！（惑）\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 30:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了恶魔姐姐！嗯……她不在2-4在这儿干嘛……\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 31:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只恋恋！你竟然能看到她……她这样想着，想着，无意识地消失了……\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 32:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只小五！她看到了你钓到了正在对你读心的她……\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 33:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只幽幽子！或许她想吃鱼所以跳到湖里去了？？？\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 34:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只妖梦！她似乎在水中练习着什么神奇的剑术……\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 35:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只文文！她在练习波纹气功。等等练习什么？？？\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 36:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只pad！没等你反应过来，她大喊一声砸瓦鲁多，飞回了2-3。\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 37:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只姆Q！她在水中犯了哮喘病，还好你救了她一命……但她并不想给你什么回报，因为星光这个懒比懒得写代码哈哈！\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 38:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只早喵！或许这就是奇迹的力量罢（确信）\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 39:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只河童！等等这只河童竟然不会游泳…………真怪！\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 40:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只⑩！她看起来想吃人。是~这样吗~！\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 41:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你竟然钓到了八云紫！17岁的妙龄少女，失足跌入雾之湖，迷茫地望着你…………然后突然透过隙间消失了。\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 42:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只八云蓝！九尾狐的尾巴防水嘛……（惑）\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 43:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只橙喵！还好你把她救上来了不然她真的会淹死！！！\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 44:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只慧音老师！为什么老师会在湖里呢……（疑惑）\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 45:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只辉夜！辉夜大小姐打算在湖里向我…………求救\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 46:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只小伞！她试图吓你一跳，但没啥作用……于是她本来想给你一把伞作为报答，但是星光懒得写代码。\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 47:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只转转！她在水里转来转去，形成了强大的水卷风……？\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 48:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只阿燐！她在水中推着小推车，是想清洗尸体吗……等等猫猫竟然不怕水！\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            elif results <= 49:
                                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + ']你决定在雾之湖旁钓鱼。你坐在湖边，往下缓缓放钩子……\n突然感觉到钩子有动静！你使劲往上一拉——\n你钓到了一只阿空！你将她钓起来之后她立马飞走了……嗯……这就是所谓的核辐射安全距离控制吗……\n[CQ:image,' r'file=' + str(r[start:end]) + r']'))
                            return 0
                        elif results <= 55:
                            tnum2 = getbag.getbags(qq,22)
                            if tnum2 == 0:
                                tnum2 = tnum2 + 1
                                changebag.changebags(qq,tnum2,22)
                                output = output + '\n你钓到了一个烧烤机！似乎使用时再在后面输入想要烧烤的东西编号就能进行烧烤啦……等等这玩意掉水里竟然还能用嘛！（已获得：22 烧烤机）'
                            else:
                                money = float(getdata.getsd(qq,5))
                                money = money + 150
                                change.changes(qq,money,5)
                                output = output + '\n你钓到了150积分！竟然有人把积分扔进湖里，真是浪费……'

                    else:
                        output = output + '你今天的钓鱼次数用光啦，或者攒够' + str(needmoney) + '积分即可再次钓鱼！'
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                        return 0
                    
                elif(nowplace == "2"):
                    output = output + '你在美铃面前挥舞着鱼竿，她一脸看baka的表情看着你……被当成baka了呜呜！'
                elif(nowplace == "2-0"):
                    output = output + '你在美铃面前挥舞着鱼竿，但她睡得很死，完全没有任何反应。'
                elif(nowplace == "2-1"):
                    place.changeplace(str(qq),"2")
                    output = output + '呃呃呃你！你在干嘛！地下室可不是钓鱼的地方啦！还是说……你想和芙兰玩捆绑pl……（话音刚落你就被咲夜丢出了大门口……可恶）'
                elif(nowplace == "2-2"):
                    output = output + '你决定在图书馆钓书。你坐在某个书柜的顶端往下缓缓放钩子……'
                    output = output + '\n恭喜你钓到了大可罢格！他突然揪着你的衣领，告诉你其实这段原本是别的稀有物品，你本来赚大了，但他代码还没写完哈哈。KUSO！'
                elif(nowplace == "2-3"):
                    output = output + '你在咲夜面前挥舞着钓鱼竿。咲夜甚至没看你一眼……所以你在干嘛'
                elif(nowplace == "2-4"):
                    output = output + '你在蕾米面前拿出了钓鱼竿，试图向吸血鬼展现钓鱼技术。竟然！好像没啥用！'
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
            
        elif newuse.find("22")==0:
            tnum = getbag.getbags(qq,22)
            if tnum <= 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
            else:
                if len(message) == 9:
                    output = '[CQ:at,qq='+str(qq)+']\n你将烧烤机摆在地板上，准备开始烧烤……22后面加空格加物品序号就可以烧烤东西啦！可以发送fl.bag查询物品序号哦~'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                elif message[9] != " " or len(message) == 10:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']22后面还要加一个空格再加物品序号才能使用烧烤机烤东西哦~'})
                else:
                    newburn = message[10:]
                    if newburn == "1":
                        tnum2 = getbag.getbags(qq,1)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,1)
                            results = random.uniform(0,100)
                            if results <= 50:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将补签卡放在烧烤机上碳烤，没过多久就被烧成了碳……你失去了一张补签卡'})
                            else:
                                tnum3 = getbag.getbags(qq,2) + 1
                                changebag.changebags(qq,tnum3,2)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将补签卡放在烧烤机上碳烤，经过神奇的回炉重造，补签卡竟然变成了rp重置卡！'})
                    elif newburn == "2":
                        tnum2 = getbag.getbags(qq,2)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,2)
                            results = random.uniform(0,100)
                            if results <= 50:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将rp重置卡放在烧烤机上碳烤，没过多久就被烧成了碳……你失去了一张rp重置卡'})
                            else:
                                tnum3 = getbag.getbags(qq,1) + 1
                                changebag.changebags(qq,tnum3,1)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将rp重置卡放在烧烤机上碳烤，经过神奇的回炉重造，rp重置卡竟然变成了补签卡！'})
                    elif newburn == "3":
                        tnum2 = getbag.getbags(qq,3)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将⑨转大肠放在烧烤机上碳烤，似乎除了变热以外并没有别的变化……'})
                    elif newburn == "4":
                        tnum2 = getbag.getbags(qq,4)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,4)
                            tnum3 = getbag.getbags(qq,11) + 1
                            changebag.changebags(qq,tnum3,11)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将草莓蛋糕放在烧烤机上碳烤，蛋糕逐渐变形，变成了一滩草莓奶油……你将其装在了瓶子里。（已获得：11 草莓奶油）'})
                    elif newburn == "5":
                        tnum2 = getbag.getbags(qq,5)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,5)
                            tnum4 = getbag.getbags(qq,11)
                            if tnum4 > 0:
                                tnum4 = tnum4 - 1
                                changebag.changebags(qq,tnum4,11)
                                tnum3 = getbag.getbags(qq,12) + 1
                                changebag.changebags(qq,tnum3,12)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将苹果放在烧烤机上碳烤，并加上了草莓奶油。香喷喷的苹果草莓派诞生啦！（已获得：12 苹果草莓派）'})
                            else:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将苹果放在烧烤机上碳烤，苹果被烤烂了………似乎包里如果有别的什么东西再烤的话会得到新的食物？！'})
                    elif newburn == "6":
                        tnum2 = getbag.getbags(qq,6)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将红茶玛奇朵放在烧烤机上加热，好像变得更好喝了！你拿走了红茶玛奇朵。它马上又变冷了……'})
                    elif newburn == "7":
                        tnum2 = getbag.getbags(qq,7)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,7)
                            tnum3 = getbag.getbags(qq,23) + 1
                            changebag.changebags(qq,tnum3,23)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将冰糖雪糕放在烧烤机上加热，马上融化了……啊这。你得到了一根剩下的木棍。（已获得：23 木棍）'})
                    elif newburn == "8":
                        tnum2 = getbag.getbags(qq,8)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将黑松露炒饭放在烧烤机上加热，除了变热以外好像没啥变化……'})
                    elif newburn == "9" or newburn == "⑨":
                        tnum2 = getbag.getbags(qq,9)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,9)
                            tnum3 = getbag.getbags(qq,13) + 1
                            changebag.changebags(qq,tnum3,13)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将琪露诺冰块放在烧烤机上加热，冰块马上融化了。但似乎融化的水有一股神奇的气味！你拿出瓶子，接了一瓶……(已获得：13 雾之矿泉水)'})
                    elif newburn == "10":
                        tnum2 = getbag.getbags(qq,10)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,10)
                            money = float(getdata.getsd(qq,5))
                            money = money + 250
                            change.changes(qq,money,5)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将冰冻的鱼放在烧烤机上加热，冰块马上融化了……什么！里面竟然蹦出了一只若鹭姬！你赶忙跑到雾之湖湖边将她放生了……她很感谢你救了她一命，于是给了你250积分。'})
                    elif newburn == "11":
                        tnum2 = getbag.getbags(qq,11)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,11)
                            money = float(getdata.getsd(qq,5))
                            money = money + 50
                            change.changes(qq,money,5)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将草莓奶油放在烧烤机上加热，奶油融化了……你从中找到了50积分。好奇怪为什么会有积分啦！'})
                    elif newburn == "12":
                        tnum2 = getbag.getbags(qq,12)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将苹果草莓派放在烧烤机上加热，除了变热以外好像没啥变化……'})
                    elif newburn == "13":
                        tnum2 = getbag.getbags(qq,13)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将雾之矿泉水放在烧烤机上加热，水开了……多喝热水捏！你拿走了矿泉水，结果它马上又变冷了……'})
                    elif newburn == "21":
                        tnum2 = getbag.getbags(qq,21)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,21)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将鱼竿放在烧烤机上烧，但鱼竿是木制的，马上开始着火了……你失去了一根普通的鱼竿（悲）'})
                    elif newburn == "22":
                        tnum2 = getbag.getbags(qq,22)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你建造了一个传送门，将自己的烧烤机放在烧烤机上烧烤。烧烤机开始着火……但由于烧烤机着火了烧烤功能紧急关闭所以烧烤机停止了工作，你的烧烤机保住了……'})
                    elif newburn == "23":
                        tnum2 = getbag.getbags(qq,23)
                        if tnum2 <= 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，暂时不能烧烤！'})
                        else:
                            tnum2 = tnum2 - 1
                            changebag.changebags(qq,tnum2,23)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你将木棍放在烧烤机上烧，马上开始着火了……你就这么失去了木棍。'})
        else:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
