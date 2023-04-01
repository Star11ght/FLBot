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

def guesstune(message,group,qq,urlsss):
    tunef = urlsss
    if message == "end":
        with open(file=tunef, mode='r', encoding="utf-8") as data:
            key = data.readline()
        os.remove(tunef)
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶！竟然不猜了嘛！答案是'+key+'哦！'})
        return 0
    elif len(message) == 3 :
        tune = message[0:2]
        height = message[2]
    elif len(message) == 2 :
        tune = message[0]
        height = message[1]
    if height.isdigit():
        heighta = int(height)
        with open(file=tunef, mode='r', encoding="utf-8") as data:
            key = data.readline()
            if len(key) == 3 :
                tunek = key[0:2]
                heightk = int(key[2])
            elif len(key) == 2 :
                tunek = key[0]
                heightk = int(key[1])
            tunek = tunek.lower()
        if tune == "c#":
            tune = 'db'
        elif tune == "d#":
            tune = 'eb'
        elif tune == "f#":
            tune = 'gb'
        elif tune == "g#":
            tune = 'ab'
        elif tune == "a#":
            tune = 'bb'
        if tune == tunek and heighta == heightk:
            money = float(getdata.getsd(qq,5))
            add = 5
            money = money + add
            change.changes(qq,money,5)
            os.remove(tunef)
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']猜对辣！快去教星光编曲（推）（已获得积分：5）'})
        else :
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']戳啦，再猜猜看吧！XD'})

def starttune(group,qq):
    if os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'gochess', str(qq) + '.txt'))):
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']有没有一种可能，当你下五子棋的时候，五子棋的坐标也能成为一种音高呢！'})
    elif os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'tune', str(qq) + '.txt'))):
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']先把我出的这个音猜完呗！或者输入end可以直接结束哦！'})
    else:
        tunefile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tune', str(qq) + '.txt'))
        tuneno = random.randint(9,96)
        height = int(tuneno/12)+1
        tuneno = tuneno + 1
        if tuneno%12 == 10:
            tune = "A"
        elif tuneno%12 == 11:
            tune = "Bb"
        elif tuneno%12 == 0:
            tune = "B"
        elif tuneno%12 == 1:
            tune = "C"
        elif tuneno%12 == 2:
            tune = "Db"
        elif tuneno%12 == 3:
            tune = "D"
        elif tuneno%12 == 4:
            tune = "Eb"
        elif tuneno%12 == 5:
            tune = "E"
        elif tuneno%12 == 6:
            tune = "F"
        elif tuneno%12 == 7:
            tune = "Gb"
        elif tuneno%12 == 8:
            tune = "G"
        elif tuneno%12 == 9:
            tune = "Ab"
        tune = tune + str(height)
        with open(file=tunefile, mode='w', encoding="utf-8") as data:
            data.write(tune)
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']来猜猜这是什么音！(字母加数字，升号#，降号b，加在字母后面，规定C5为中央音)(输入end可结束猜音)'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file='+tune+'.mp3]'})

def usepiano(message,group,qq):
    if message[0:8] == "fl.piano":
        melody = message[9:]
        if len(message) == 8:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n钢琴功能输入顺序：\n①（可选）左括号\"(\"降一个八度，右括号\")\"反之，默认下为小字一组，最多可使用三个括号\n②（必选）输入音符0~7，可用合法的升降号#或b，0为空拍无升降号\n③（可选）加号\"＋\"速度加快一倍，减号\"－\"速度放慢一倍，默认下为8分音符，范围为全音符~32分音符'})    
        elif message[8] != " ":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']piano后面要加空格哦~'})
        else:
            timedo = 0
            timedo = len(melody)/4
            timedo = round(timedo,2)
            if timedo !=0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰大约需要' + str(timedo) + '秒钟的时间弹奏！等等喵……'})
            get = piano.musicmake(melody)
            print(get)
            if get == None or get == -1:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n输入的音符串不合法！\n输入顺序：\n①（可选）左括号\"(\"降一个八度，右括号\")\"反之，默认下为小字一组，最多可使用三个括号\n②（必选）输入音符0~7，可用合法的升降号#或b，0为空拍无升降号\n③（可选）加号\"＋\"速度加快一倍，减号\"－\"速度放慢一倍，默认下为8分音符，范围为全音符~32分音符'})
            else:
                pianodocu = str(get) + ".mp3"
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file=' + pianodocu + ']'})