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

REFRESH_TOKEN = 'LRZahNpdcEjcULZBPrh3c3kpVx5-3jEEAB9xMPppIJo'

def picturefind(message,group,qq):
    trytime = 0
    urls = 'https://api.lolicon.app/setu/v2?size=small'
    getpicture = 1
    if len(message) >= 10:
        tag = message[11:]
        while len(tag)>0:
            loca = tag.find("，")
            if(loca<0):
                gettag = tag
                if gettag == "18rated":
                    urls = urls + '&r18=1'
                else:
                    urls = urls + '&tag=' + gettag
                break
            else:
                gettag = tag[0:loca]
                urls = urls + '&tag=' + gettag
                tag = tag[loca+1:]
    print(urls)
    picgroup = group
    picqq = qq
    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰正在寻找图片中，请稍后……\n（picture后什么都不加为随机，加tag需由中文逗号隔开）'})

    try:
        r = requests.get(urls).content.decode('UTF-8')
        start = r.find("https")
        end = r.find("}}]}")
        
        imglo = r.find("img-master")
        print(start,end)
        if start == -1 or end == -1:
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + r']芙兰没有找到规定的图片！换个tag试试吧orz（tag之间要用中文逗号隔开哦！）'))
            trytime = 0
            return 0
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

        mas = r.find("master")
        originalpic = "https://i.pixiv.re/" + r[imglo:mas] + "master1200."

        if r[end - 3:end] == "jpg":
                originalpic =  originalpic + "jpg"
        else:
                originalpic =  originalpic + "png"
        print(r[start:end])
        websites = "https://pixiv.re/" + msg_pid
        msg_p = str(int(msg_p) + 1)
        if(msg_p!="1"):
            websites = websites + "-" + msg_p
        if r[end - 3:end] == "jpg":
            websites = websites + ".jpg"
        else:
            websites = websites + ".png"
        
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + r'][CQ:image,' r'file=' + str(r[start:end]) + r']'))
        trytime = 0
        
    except:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + r']出现错误，请再试一次！果咩纳塞orz'))
        print("Failed."+str(trytime))
        time.sleep(0.2)
        return 0

    requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + ']已找到图片！若长时间未收到可能被tx吞了或是原图网址404了，请再试一次！\n标题：' + msg_title + '\n作者：' + msg_author +'\nid：' + msg_pid + ' 第' + msg_p + 'P\n作者id：' + msg_uid + '\n图片网址：\n'+ websites))
    return 0

def pixivfind(message,group,qq):
    if len(message) == 8:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\npixiv后面加pid数字就能获取p站图片啦！已过滤R-18标签，请放心食用~'})
    elif message[8] != " " or len(message) == 9:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']pixiv后面要加空格哦~'})
    else:
        newmsg = message[9:]
        if not newmsg.isdigit():
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']要输入数字才有效啦！！！'})
            return 0
        aapi = AppPixivAPI()
        aapi.auth(refresh_token=REFRESH_TOKEN)
        json_result = aapi.illust_detail(newmsg)
        illusts = json_result.illust
        if illusts == None:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']该图片不存在，请检查输入是否有误！'})
            return 0
        title = "标题：" + illusts.title + "\n"
        author = "作者：" + illusts.user.name + "\n"
        id = "图片id：" + str(illusts.id) + "\n"
        times = illusts.create_date.replace("T"," ")
        times = times[:-6]
        times = "时间：" + times + "\n"
        urls = "https://pixiv.re/" + str(illusts.id) + ".jpg"
        websites = "原图：" + urls + "\n"

        tagnum = len(illusts.tags)
        tags = illusts.tags[0].name
        if tags == "R-18":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']本图为R-18图片，已阻止发送！'})
            return 0
        for x in range(1,tagnum):
            tags = tags + "," + illusts.tags[x].name
        print(tags)
        tagout = "标签：" + tags + "\n"
        captions = "简介：\n" + illusts.caption.replace("<br />","\n")
        output = title + author + id + times + websites + tagout + captions
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']已找到图片，即将发送，请稍后……'})
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(group),r'[CQ:at,qq='+ str(qq) + r'][CQ:image,' r'file=' + urls + r']'))
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']图片信息：\n' + output})

def picmix(message,group,qq):
    if message[0:6] == "fl.pic":
        if len(message) <= 7:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\npic加空格加数字1~5可选择图片翻转类型\n1为水平翻转左边拼在右边\n2为水平翻转右边拼在左边\n3为垂直翻转上边拼在下边\n4为垂直翻转下边拼在上边\n5为翻转图片颜色\n之后还要跟着一张图片哦！'})
            return 0
        choose = message[7]
        if choose.isdigit():
            cse = int(choose)
        if message[6] != " ":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']pic后面要加空格哦~'})
        elif not choose.isdigit() or cse > 5 or cse == 0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\npic加空格加数字1~5可选择图片翻转类型\n1为水平翻转左边拼在右边\n2为水平翻转右边拼在左边\n3为垂直翻转上边拼在下边\n4为垂直翻转下边拼在上边\n5为翻转图片颜色\n之后还要跟着一张图片哦！'})
        
        else:   
            locate = message.find("url")
            if(locate > 0):
                picurl = message[locate+4:]
                print(picurl)
                numbe = picrev.picrev(picurl,cse)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=picrev_' + str(numbe) + '.png]'})
            else:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰没收到您发过来的图片耶……要不要再试一次？！'})