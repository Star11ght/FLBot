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

def chess(message,group,qq,checkchessfile):
    x = message[0]
    x0 = message[0]
    y = message[1:]
    y0 = message[1:]
    if ord(x)>=97 and ord(x) <= 111 and y.isdigit() :
        y = int(y)
        if y >= 1 and y <= 15:
            with open(file=checkchessfile, mode='r', encoding="utf-8") as data:
                lastnx = data.readline()
                lasty = int(data.readline())
                lastnx = lastnx.strip()
                if lastnx != "0":
                    lastx = int(ord(lastnx)-97)
                room = data.readline()
                room = room.strip()
                
            checkroomfile = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(room) + '.txt'))
            
            with open(file=checkroomfile, mode='r', encoding="utf-8") as data:
                people = int(data.readline())
                rounds = int(data.readline())
                bqq = int(data.readline())
                wqq = int(data.readline())
                if (rounds % 2 == 0 and qq == bqq) or (rounds % 2 == 1 and qq == wqq):
                    chboard = [[0 for x in range (15)] for x in range (15)]
                    chbint = [[0 for x in range (15)] for x in range (15)]
                    for x in range(0,15):
                        chboard[x] = data.readline()
                        for y in range(0,15):
                            chbint[x][y] = int(chboard[x][y])
                
            if (rounds % 2 == 0 and qq == bqq) or (rounds % 2 == 1 and qq == wqq) :
                if chbint[ord(message[0])-97][int(message[1:])-1] != 0:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']这个位置上已经有棋子啦！换个位置试试看吧~'})
                else :
                    rounds = rounds + 1
                    if qq == bqq:
                        n = 1
                        qq2 = wqq
                    if qq == wqq:
                        n = 2
                        qq2 = bqq
                        
                    getimages.writein(message,n,rounds,room)
                    
                    x = ord(message[0])-97
                    y = int(message[1:])-1
                    chbint[x][y] = n
                    print(x,y)
                    if x < 4 :
                        topx = 0
                    else:
                        topx = x - 4
                        
                    if x > 10 :
                        bottomx = 14
                    else:
                        bottomx = x + 4
                        
                    if y < 4 :
                        lefty = 0
                    else:
                        lefty = y - 4
                        
                    if y > 10 :
                        righty = 14
                    else:
                        righty = y + 4
                        
                    count1 = 0
                    for i in range(topx,bottomx+1):
                        if chbint[i][y] == n:
                            count1 = count1 + 1
                            print(i,y,count1)
                            if count1 == 5:
                                break
                        else :
                            count1 = 0
                    
                    count2 = 0
                    for i in range(lefty,righty+1):
                        if chbint[x][i] == n:
                            count2 = count2 + 1
                            print(x,i,count2)
                            if count2 == 5:
                                break
                        else :
                            count2 = 0

                    count3 = 0
                    topxc = x
                    leftyc = y
                    bottomxc = x
                    rightyc = y
                    time = 4
                    while topxc != 0 and leftyc != 0 and time != 0:
                        topxc = topxc - 1
                        leftyc = leftyc - 1
                        time = time - 1
                    time = 4
                    while bottomxc != 14 and rightyc != 14 and time != 0:
                        bottomxc = bottomxc + 1
                        rightyc = rightyc + 1
                        time = time - 1
                    ix = topxc
                    iy = leftyc
                    while(ix<=bottomxc and iy <= rightyc):
                        if chbint[ix][iy] == n:
                            count3 = count3 + 1
                            print(ix,iy,count3)
                            if count3 == 5:
                                break
                        else :
                            count3 = 0
                        ix = ix + 1
                        iy = iy + 1
                    
                    count4 = 0
                    topxc = x
                    leftyc = y
                    bottomxc = x
                    rightyc = y
                    time = 4
                    while topxc != 0 and rightyc != 14 and time != 0:
                        topxc = topxc - 1
                        rightyc = rightyc + 1
                        time = time - 1
                    time = 4
                    while bottomxc != 14 and leftyc != 0 and time != 0:
                        bottomxc = bottomxc + 1
                        leftyc = leftyc - 1
                        time = time - 1
                    ix = topxc
                    iy = rightyc
                    while(ix<=bottomxc and iy >= leftyc):
                        if chbint[ix][iy] == n:
                            count4 = count4 + 1
                            print(ix,iy,count4)
                            if count4 == 5:
                                break
                        else :
                            count4 = 0
                        ix = ix + 1
                        iy = iy - 1
                    print(count1,count2,count3,count4)
                    if count1 ==5 or count2 ==5 or count3 ==5 or count4 ==5:
                        add = float(getimages.getadd(rounds))
                        money = float(getdata.getsd(qq,5))
                        money = money + add
                        change.changes(qq,money,5)
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n恭喜你赢得了这场五子棋比赛！\n作为奖品，芙兰也想喂你五 亿 颗 弹 幕 哦 ~！！！（惊悚的笑声）\n本轮进行回合数：' + str(rounds) +'\n已获得积分：'+str(add)+'[CQ:image,file=' + str(room) +'_'+ str(rounds) +'.png]'})
                        location1 = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(qq) + '.txt'))
                        os.remove(location1)
                        location2 = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(qq2) + '.txt'))
                        os.remove(location2)
                        location3 = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(room) + '.txt'))
                        os.remove(location3)
                        location4 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images', str(room)))
                        shutil.rmtree(location4)
                        
                    else :
                        if rounds == 225:
                            add = float(getimages.getadd(rounds))
                            money = float(getdata.getsd(qq,5))
                            money = money + add
                            money2 = float(getdata.getsd(qq2,5))
                            money2 = money2 + add
                            change.changes(qq,money,5)
                            change.changes(qq2,money2,5)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n什么！你们……竟然下满了整个棋盘！？！实在是tdllwsl……\n作为奖品，芙兰要喂你们俩1145141919810 亿 颗 弹 幕 了 哦 ~~~~~~！！！（极度惊悚的笑声）\n本轮进行回合数：' + str(rounds) +'\n两人均获得积分：'+str(add)+'[CQ:image,file=' + str(room) +'_'+ str(rounds) +'.png]'})
                            location1 = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(qq) + '.txt'))
                            os.remove(location1)
                            location2 = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(qq2) + '.txt'))
                            os.remove(location2)
                            location3 = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(room) + '.txt'))
                            os.remove(location3)
                            location4 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images', str(room)))
                            shutil.rmtree(location4)
                        else:
                            message = message.upper()
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n房间号：'+str(room)+"\n回合数："+str(rounds)+"\n您下在了"+ message + '这个位置上。\n现在是[CQ:at,qq='+str(qq2)+']的回合啦！\n[CQ:image,file=' + str(room) +'_'+ str(rounds) +'.png]'})
                            with open(file=checkroomfile, mode='w', encoding="utf-8") as data:
                                data.write(str(people)+"\n")
                                data.write(str(rounds)+"\n")
                                data.write(str(bqq)+"\n") 
                                data.write(str(wqq)+"\n")
                                for x in range(0,15):
                                    for y in range(0,15):
                                        data.write(str(chbint[x][y]))
                                    data.write("\n")
                            
                            with open(file=checkchessfile, mode='w', encoding="utf-8") as data:
                                data.write(x0+"\n")
                                data.write(y0+"\n")
                                data.write(str(room)+"\n")

def endchess(group,qq,checkchessfile):
    if os.path.exists(checkchessfile):
        with open(file=checkchessfile, mode='r', encoding="utf-8") as data:
            checking = data.readline()
            checking = checking.strip()
            if not checking.isdigit():
                checking2 = data.readline()
                room = data.readline()
                room = room.strip()
                checkroomfile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', room + '.txt'))
                with open(file=checkroomfile, mode='r', encoding="utf-8") as dat:
                    num = dat.readline()
                    rounds = dat.readline()
                    bqq = int(dat.readline())
                    wqq = int(dat.readline())
                    if(bqq == qq):
                        qq2 = wqq
                    else:
                        qq2 = bqq
                    dat.close()
                data.close()
                os.remove(checkchessfile)
                location2 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', str(qq2) + '.txt'))
                os.remove(location2)
                os.remove(checkroomfile)
                location4 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images', room))
                shutil.rmtree(location4)
                add = float(getimages.getadd(rounds))
                money = float(getdata.getsd(qq2,5))
                money = money + add
                change.changes(qq2,money,5)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您中途退出了对局！您的对手[CQ:at,qq='+str(qq2)+']获得积分：' + str(add)})
            else:
                data.close()
                room = checking.strip()
                roomfile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', room + '.txt')) 
                os.remove(checkchessfile)
                os.remove(roomfile)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您已关闭房间' + room + '~'})
    else:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶……难不成你在和芙兰下棋嘛！芙兰可没有答应哦~'}) 

def startchess(message,group,qq):
    if message[0:8] == "fl.chess":
        newchess = message[9:]
        if not newchess.isdigit():
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']chess后面加空格再加任意数字就能创建五子棋房间了哦！'})
        else:
            if message[8] != " ":
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']chess后面要加个空格！'})
            
            elif os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', str(qq) + '.txt'))):
                print("五子棋正在进行中\n")
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']先把这盘棋下完再来下新的一局吧~'})
                
            elif os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'tune', str(qq) + '.txt'))):
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']有没有一种可能，当你猜音的时候，音高也能成为一种五子棋的坐标呢！'})
            
            else :
                room = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', newchess + '.txt'))
                if os.path.exists(room):
                    with open(file=room, mode='r', encoding="utf-8") as data:
                        people = int(data.readline())
                        if people == 2:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']当前房间人已经满啦，换一个房间代号吧！或者……来陪芙兰玩玩？XD'})
                        else:
                            qq2 = data.readline()
                            if int(qq2) == qq:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']自己和自己下棋的话，到底是谁输谁赢捏……反正我拒绝你这么做！'})
                            else :
                                qqcolor = random.randint(1,2)
                                if qqcolor == 1:
                                    qq2color = 2
                                    bqq = qq
                                    wqq = qq2
                                    black = getdata.getsd(qq,1)
                                    white = getdata.getsd(qq2,1)
                                else :
                                    qq2color = 1
                                    bqq = qq2
                                    wqq = qq
                                    black = getdata.getsd(qq2,1)
                                    white = getdata.getsd(qq,1)

                                output = '[CQ:at,qq='+str(qq)+']\n您已加入[CQ:at,qq='+str(qq2)+']的房间！\n对局开始啦！输入棋盘边缘标注的字母与数字坐标即可下棋！'
                                output = output + "\n黑方：" + black + "白方：" + white + '[CQ:image,file=Board.jpg]'
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                                
                                data1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', str(bqq) + '.txt'))
                                data2 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', str(wqq) + '.txt'))
                                
                                with open(file=room, mode='w', encoding="utf-8") as dat:
                                    dat.write("2\n"+"0\n"+str(bqq)+"\n"+str(wqq)+"\n")
                                    for x in range (15):
                                        dat.write("000000000000000\n")
                                    
                                with open(file=data1, mode='w', encoding="utf-8") as dat:
                                    dat.write("Z\n0\n"+str(newchess)+"\n")

                                with open(file=data2, mode='w', encoding="utf-8") as dat:
                                    dat.write("Z\n0\n"+str(newchess)+"\n")
                                getimages.start(newchess)
                else:
                    qqdata = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', str(qq) + '.txt'))
                    with open(file=room, mode='w', encoding="utf-8") as data:
                        data.write("1\n"+str(qq))
                        output = '[CQ:at,qq='+str(qq)+']您已创建一个新的五子棋房间~第二个人输入与你相同的房间号就可以开始下五子棋啦！'
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                        
                    with open(file=qqdata, mode='w', encoding="utf-8") as data:
                        data.write(str(newchess)+"\n")