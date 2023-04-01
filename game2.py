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

def game2(message,group,qq,g2left,g2right,g2total):
    g2l = g2left
    g2r = g2right
    print(int(message),g2left,g2right)
    print("符合输入要求")
    answer = int(message)
    location = os.path.abspath(os.path.join(os.path.dirname(__file__),  'bomb', 'player.txt'))
    with open(file=location, mode='r', encoding="utf-8") as data:
        key = int(data.readline())
    if answer > key :
        g2right = answer
        g2total = g2total + 1
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你缩小了炸弹人偶的范围！在' + str(g2left) + "-" + str(g2right) + "之间再猜猜看吧~"})
    elif answer < key :
        g2left = answer
        g2total = g2total + 1
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你缩小了炸弹人偶的范围！在' + str(g2left) + "-" + str(g2right) + "之间再猜猜看吧~"})
    elif answer == key :
        num = os.path.abspath(os.path.join(os.path.dirname(__file__),  'bomb', 'num.txt'))
        with open(file=num, mode='r', encoding="utf-8") as data:
            people = int(data.readline())
        money = float(getdata.getsd(qq,5))
        add = 5 * (people - 1)
        money = money + add
        change.changes(qq,money,5)
        output = '[CQ:at,qq='+str(qq)+']恭喜你找到炸弹人偶啦！你tdllwsl！那么这个炸弹人偶就——（红 魔 馆 爆 破 不 可 避）（'
        if people == 1:
            output = output + "单人游戏下不获得积分）"
        else :
            output = output + str(people) + "人游戏下您已获得积分" + str(add) + ")"
        output = output + "（本次一共用了" + str(g2total) + "次尝试机会找到该人偶)"
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output })
        g2total = 0
        bomb.gameend()
    if g2l != g2left:
        return g2left
    elif g2r != g2right:
        return g2right+100000
    else:
        return -1