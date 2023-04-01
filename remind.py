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
import game2
import chess
import guesstune
import aitalk
import search
import store
import move
import usebank
import game
import usepicture
from datetime import datetime
from ffmpy import FFmpeg
from pixivpy3 import *

def daysadd(message,group,qq):
    if message[0:7] == "fl.days":
        userlist = ["" for x in range(500)]
        dayslist = ["" for x in range(500)]
        eventslist = ["" for x in range(500)]
        urls = os.path.abspath(os.path.join(os.path.dirname(__file__), 'days', 'users.txt'))
        exists = -1
        with open(file=urls, mode='r', encoding="utf-8") as data:
            users = data.readline().strip()
            days = ""
            events = ""
            total = 0
            while(users!="-1"):
                userlist[total] = users
                if(int(users)==int(qq)):
                    exists = total
                days = data.readline().strip()
                dayslist[total] = days
                events = data.readline().strip()
                eventslist[total] = events
                total = total + 1
                users = data.readline().strip()

        if len(message) == 7:
            if(exists==-1):
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你还没有添加过倒数日事件哦！请按照格式“fl.days YYYY-MM-DD 事件名称”来添加倒数日事件！（位数不够前面补0，days、日期、事件之间需带空格）'})
            else:
                days = dayslist[exists]
                date = datetime.strptime(days, "%Y-%m-%d").date()
                events = eventslist[exists]
                today = datetime.now().date()
                delta = (today - date).days
                output = "您设下的事件为于" + str(days) + "这一天发生的“" + str(events) + "”，"
                if(delta==0):
                    output = output + "今天就是该事件发生的日子啦！祝您有一个特殊的一天~~~"
                elif(delta>0):
                    output = output + "距离该事件发生已经过去了" + str(delta) + "天。真是怀旧呢XD"
                else:
                    output = output + "距离该事件发生还剩下" + str(-delta) + "天。或许需要芙兰的鼓励……？！干巴爹！"
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + output})
            return 0
        
        try:
            msgget = message.split()
            date = msgget[1]
            if date == "del":
                if exists == -1:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你还没有添加倒数日事件，删不了啦！'})
                    return 0
                print(exists,total)
                total = total - 1
                for x in range(exists,total):
                    userlist[x] = userlist[x+1]
                    dayslist[x] = dayslist[x+1]
                    eventslist[x] = eventslist[x+1]
                
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已成功删除自己的倒数日事件~'})

            else:
                if exists != -1:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已经添加过倒数日事件啦，若想替换请输入fl.days del删除原有的事件再添加哦！'})
                    return 0
                events = msgget[2]
                date = datetime.strptime(date, "%Y-%m-%d").date()
                today = datetime.now().date()
                delta = (today - date).days
                userlist[total] = qq
                dayslist[total] = date
                eventslist[total] = events
                total = total + 1
            
            with open(file=urls, mode='w', encoding="utf-8") as data:
                for x in range(total):
                    data.write(str(userlist[x])+"\n")
                    data.write(str(dayslist[x])+"\n")
                    data.write(str(eventslist[x])+"\n")
                data.write("-1")

            if date != "del":
                output = "添加成功！"
                if(delta==0):
                    output = output + "今天就是" + events + "的日子啦！在今天设置了这样的日子一定有什么深意吧（笑）"
                elif(delta>0):
                    output = output + "距离" + events + "已经过去了" + str(delta) + "天。真是怀旧呢XD"
                else:
                    output = output + "距离" + events + "还剩下" + str(-delta) + "天。或许需要芙兰的鼓励……？！干巴爹！"
                output = output + "（以后每日凌晨12点芙兰都会在主群里放送各位设下的倒数日哦）"
                print(output)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + output})

        except:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式输入错啦，再输一次试试看！（日期：YYYY-MM-DD，位数不够前面补0，日期与事件之间需带空格）'}) 
            return 0

def daysrem(nyear,nmonth,ndays):

    urls = os.path.abspath(os.path.join(os.path.dirname(__file__), 'days', 'users.txt'))

    output = '晚上好~新的一天开始啦！今天是' + nyear + "年" + nmonth + "月" + ndays + "日，以下是各位的倒数日事件：\n" 
    with open(file=urls, mode='r', encoding="utf-8") as data:
        users = data.readline().strip()
        days = ""
        events = ""
        total = 0
        while(users!="-1"):
            nowname = getdata.getsd(users,1)
            if nowname == "iamnameless\n":
                nowname = "*******" + users[-4:]
            else:
                nowname = nowname.strip() + "(" + users[-4:] + ")"

            days = data.readline().strip()
            events = data.readline().strip()
            output = output + nowname + "：\n"
            date = datetime.strptime(days, "%Y-%m-%d").date()
            today = datetime.now().date()
            delta = (today - date).days
            if(delta==0):
                output = output + "今天就是" + events + "的日子"
            elif(delta>0):
                output = output + "距离" + events + "已经过去了" + str(delta) + "天"
            else:
                output = output + "距离" + events + "还剩下" + str(-delta) + "天"
            users = data.readline().strip()
            output = output + "(" + days + ")\n"
        output = output + "\n您也可以输入fl.days设置或修改自己的倒数日事件哦！最后祝大家今夜好梦~"
    sendmsg.send_msg({'msg_type':'group','number':'719317473','msg':output}) 