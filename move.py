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

def places(group,qq):
    output = '[CQ:at,qq='+str(qq)+']您当前的所在地是：'
    nowplace = place.checkplace(qq)
    if(nowplace == "0"):
        output = output + '\n0 人间之里。真是安详的一天啊！'
    elif(nowplace == "1"):
        output = output + '\n1 雾之湖。湖上也有许多飞来飞去的妖精呢。'
    elif(nowplace == "2" or nowplace == "2-0"):
        output = output + '\n2 红魔馆(入口)。不知道门番是否在打鼾呢！'
    elif(nowplace == "2-1"):
        output = output + '\n2-1 红魔馆地下室。芙兰就在你身边看着你哦~诶嘿！'
    elif(nowplace == "2-2"):
        output = output + '\n2-2 红魔馆图书馆。姆Q今天放下书了吗（不可能，绝对不可能）'
    elif(nowplace == "2-3"):
        output = output + '\n2-3 红魔馆大堂中央。今天的咲夜也在很卖力地打扫卫生呢~'
    elif(nowplace == "2-4"):
        output = output + '\n2-4 红魔馆主殿堂。威严满满的姐姐大人正在威严满满地品着红酒！'
    sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})

def move(message,group,qq,favor):
    if len(message) == 7:
        output = '[CQ:at,qq='+str(qq)+']\n在move之后加空格加数字(地点序号)即可移动到该区域！'
        output = output + '\n0 人间之里'
        output = output + '\n1 雾之湖'
        output = output + '\n2 红魔馆(入口)'
        output = output + '\n(需先到达2)2-1 地下室'
        output = output + '\n(需先到达2)2-2 图书馆'
        output = output + '\n(需先到达2)2-3 大堂中央'
        output = output + '\n(需先到达2)2-4 主殿堂'
        output = output + '\n输入fl.place可以查询自己现在所处的位置哦！'
        sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
    elif message[7] != " " or len(message) == 8:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']move后面要加一个空格才能移动哦~'})
    else:
        newmove = message[8:]
        nowplace = place.checkplace(qq)
        results = random.uniform(0,100)
        if results <= 5:
            money = float(getdata.getsd(qq,5))
            money = money - 20
            change.changes(qq,money,5)
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']当你刚准备出发时，一只粉色的兔子突然出现在你的面前绊了你一脚。疼！你爬起来之后发现自己失去了20积分！？！可恶的兔子。。。'})
            return 0
        if newmove == nowplace or (newmove == "2" and nowplace == "2-0"):
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你原地踏步，然后以光速绕了地球一圈，回到了原来的位置。'})
        elif newmove == "0":
            place.changeplace(qq,newmove)
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你回到了人间之里的家中。啊——又是个安详的一天呢（伸懒腰）'})
        
        elif newmove == "1":
            firstmove = place.changeplace(str(qq),str(newmove))
            if(firstmove == 1):
                output = '[CQ:at,qq='+str(qq)+']你来到了雾之湖！湖面上有一只蓝色的baka，你决定去找她探讨智慧人生……\n………………\n………………\n………………\n………………\n………………\n………………\n………………'
                results = random.uniform(0,100)
                if(results<=29.99):
                    money = float(getdata.getsd(qq,5))
                    money = money + 29.99
                    change.changes(qq,money,5)
                    output = output + '\n探讨结束！baka酱觉得你很有胆识，于是掏出了身上的29.99积分决定送给你。（已获得29.99积分）'
                else:
                    output = output + '\n探讨结束！baka酱想送你积分，她决定先向你借99积分再送给你……真是个baka呢（无慈悲）'
            else:
                output = '[CQ:at,qq='+str(qq)+']你又来到了雾之湖！baka已经不见了踪影，你决定独自思考人生……\n………………\n………………\n………………\n………………\n………………\n………………\n………………'
                output = output + '\n你感觉你的人生上升到了一个新的境界。（所以有用吗）'
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

        elif newmove == "2":
            firstmove = place.changeplace(str(qq),str(newmove))
            if(firstmove == 1):
                output = '[CQ:at,qq='+str(qq)+']你来到了红魔馆大门口！似乎有位红发的华人小姑娘站在门口，你决定上去看看……'
                results = random.uniform(0,100)
                if(favor>=15):
                    output = output + '\n美铃似乎一眼就认出了你，她很欢迎你进入红魔馆去找二妹玩。呀吼！（可以输入fl.move 2-X进入红魔馆内部了）'
                elif(results<=30):
                    place.changeplace(str(qq),"2-0")
                    output = output + '\n这位守门员竟然站着都能睡着！？！你决定趁她不注意偷偷潜入……（可以输入fl.move 2-X进入红魔馆内部了）'
                else:
                    output = output + '\n她一把就拦住了你，捏着拳头摆出招式，叫嚣着“拒绝外人进入”。真拿她没办法……'
            else:
                output = '[CQ:at,qq='+str(qq)+']你又来到了红魔馆大门口！'
                if(favor>=15):
                    output = output + '\n美铃看都不看一眼就认出了你，她很欢迎你进入红魔馆去找二妹玩。呀吼！（可以输入2-X进入红魔馆内部了）'
                else:
                    output = output + '\n美铃还在那儿威风凛凛地站着，看到你立马又捏着拳头摆出招式，叫嚣着“拒绝外人进入”。真拿她没办法……'
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

        elif newmove.find("2-") == 0:
            if nowplace.find("2") != 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']要先前往红魔馆大门口才能进入红魔馆内部啦！'})
            elif favor<15 and nowplace == "2":
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你想偷偷摸摸进入红魔馆，被美铃一拳拦住了。可恶……'})
            else:
                newmove2 = newmove[2:]
                if newmove2 == "1":
                    firstmove = place.changeplace(str(qq),str(newmove))
                    if(firstmove == 1):
                        output = '[CQ:at,qq='+str(qq)+']欢迎你来到地下室！！！快来陪芙兰一起玩吧……（笑）（掏出莱瓦汀）（破坏小熊人偶）（变出三个分身）（互相乱砍）（你成功躲开了四位芙兰的弹幕）（你站在角落静静观望，似乎红魔馆又要爆炸了……）'
                        results = random.uniform(0,100)
                        if(results<=60-favor*2):
                            money = int(getdata.getsd(qq,2))
                            money = money + 1
                            change.changes(qq,money,2)
                            output = output + '\n（经过了四个小时的激烈折腾，你和芙兰的好感度竟然上升了1点……呃……你该不会是M吧（后缩））'
                        elif(results<=60):
                            money = float(getdata.getsd(qq,5))
                            money = money + 100
                            change.changes(qq,money,5)
                            output = output + '\n（你看着芙兰在地下室里飞来飞去，突然发现了角落里藏着100积分。偷偷拿走，嗯！）（已获得100积分）'
                        else:
                            output = output + '\n（之后你又陪芙兰在地下室玩(???)了半个小时，她正准备扯下你的胳膊，你慌忙挣脱躲到了角落里。太可怕了……）'
                    else:
                        output = '[CQ:at,qq='+str(qq)+']呜哇！欢迎再次回来！！！芙兰等你好久啦~继续一起玩耍吧XDXDXD'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif newmove2 == "2":
                    firstmove = place.changeplace(str(qq),str(newmove))
                    if(firstmove == 1):
                        output = '[CQ:at,qq='+str(qq)+']你来到了图书馆。姆Q正在专心读书，没注意到你……'
                        results = random.uniform(0,100)
                    else:
                        output = '[CQ:at,qq='+str(qq)+']你又一次来到了图书馆。姆Q还是在专心读书，可恶是书呆子！'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif newmove2 == "3":
                    firstmove = place.changeplace(str(qq),str(newmove))
                    if(firstmove == 1):
                        output = '[CQ:at,qq='+str(qq)+']你来到了大堂中央，看到红魔馆的女仆长正在努力打扫，似乎没时间理你……'
                        results = random.uniform(0,100)
                    else:
                        output = '[CQ:at,qq='+str(qq)+']你又一次来到了大堂中央，咲夜正坐在椅子上休息，看起来很疲惫的样子。'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif newmove2 == "4":
                    firstmove = place.changeplace(str(qq),str(newmove))
                    if(firstmove == 1):
                        output = '[CQ:at,qq='+str(qq)+']你来到了红魔馆主殿堂，遇到了坐在殿堂中央的蕾米。'
                        results = random.uniform(0,100)
                        if(results <= 25 and favor < 20):
                            money = int(getdata.getsd(qq,2))
                            money = money + 1
                            change.changes(qq,money,2)
                            output = output + "蕾米今天似乎心情不错……她改变了你与芙兰之间的命运。（你与芙兰的好感度上升了1点）"
                        elif(results <= 25 and favor >= 20):
                            money = float(getdata.getsd(qq,5))
                            money = money + 250
                            change.changes(qq,money,5)
                            output = output + "蕾米今天似乎心情不错……她奖励了你250积分。"
                        elif(results <= 50):
                            money = float(getdata.getsd(qq,5))
                            money = money + 50
                            change.changes(qq,money,5)
                            output = output + "她正掂着高脚杯喝红酒，突然看向你……于是你陪她喝了一杯。她似乎很赏识你，奖励给了你50积分。"
                        else:
                            output = output + "她正掂着高脚杯喝红酒，并没有理会你……"
                    else:
                        output = '[CQ:at,qq='+str(qq)+']你又来到了红魔馆主殿堂，蕾米正坐在王座上，威严满满地品着红酒。嗯……很压抑的气氛……'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                else:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你来到了红魔馆的虚空中，这里太可怕了，你在马上要摔下去的那一刻回到了原地。'})
        else:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你想去的地方是个未知的领域呢……真是神秘啊XD'})