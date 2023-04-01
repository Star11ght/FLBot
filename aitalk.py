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

def aitalk(message,group,qq):
    if len(message) == 9:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']aitalk后面加空格加随便什么东西可以让两个ai相互对话哦~'})
    elif len(message) == 10 or message[9] !=" ":
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']aitalk后面要加空格哦~'})
    else:
        newqq = message[10:]
        url = "https://api.ownthink.com/bot?spoken=" + newqq
        response = requests.get(url)
        data = response.text
        answer = json.loads(data)
        text1 = answer['data']['info']['text']
        output = '[CQ:at,qq='+str(qq)+']\n你：' + newqq + '\nai2：' + text1

        url = "http://api.qingyunke.com/api.php?key=free&msg=" + text1
        response = requests.request("GET", url)
        data = response.text
        start = data.find("content") + 10
        ends = data.find("}")
        end = 0
        while ends >= 0:
            end = end + ends + 1
            newdata = data[end:]
            ends = newdata.find("}")
            if ends < 0:
                end = end - 1
        end = end - 1
        answer = data[start:end]
        text2 = answer.replace("{br}","\n")
        output = output + '\nai：' + text2
        
        url = "https://api.ownthink.com/bot?spoken=" + text2
        response = requests.get(url)
        data = response.text
        answer = json.loads(data)
        text3 = answer['data']['info']['text']
        output = output + '\nai2：' + text3

        url = "http://api.qingyunke.com/api.php?key=free&msg=" + text3
        response = requests.request("GET", url)
        data = response.text
        start = data.find("content") + 10
        ends = data.find("}")
        end = 0
        while ends >= 0:
            end = end + ends + 1
            newdata = data[end:]
            ends = newdata.find("}")
            if ends < 0:
                end = end - 1
        end = end - 1
        answer = data[start:end]
        text4 = answer.replace("{br}","\n")
        output = output + '\nai：' + text4

        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

def ai2(message,group,qq):
    if len(message) == 6:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai2后面加空格加随便什么东西可以和ai2对话哦~对话内容和芙兰无关不是我说的话！！！'})
    elif len(message) == 7 or message[6] !=" ":
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai2后面要加空格哦~'})
    else:
        newqq = message[7:]
        url = "https://api.ownthink.com/bot?spoken=" + newqq
        response = requests.get(url)
        data = response.text
        answer = json.loads(data)
        text = answer['data']['info']['text']
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + text})

def ai(message,group,qq):
    if len(message) == 5:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai后面加空格加随便什么东西可以和ai对话哦~对话内容和芙兰无关不是我说的话！！！'})
    elif len(message) == 6 or message[5] !=" ":
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai后面要加空格哦~'})
    else:
        newqq = message[6:]
        url = "http://api.qingyunke.com/api.php?key=free&msg=" + newqq
        response = requests.request("GET", url)
        data = response.text
        start = data.find("content") + 10
        ends = data.find("}")
        end = 0
        while ends >= 0:
            end = end + ends + 1
            newdata = data[end:]
            ends = newdata.find("}")
            if ends < 0:
                end = end - 1
        end = end - 1
        answer = data[start:end]
        answer2 = "\n" + answer.replace("{br}","\n")
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + answer2})