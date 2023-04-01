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

def banks(message,group,qq):
    if message.find("fl.bank 1 ") == 0 and len(message) >= 11:
        moneyminus = message[10:]
        money = float(getdata.getsd(qq,5))
        if moneyminus == "all":
            moneyminus = str(money)
        try:
            moneym = float(moneyminus)
        except:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的积分哦~'})
            return 0
        if moneyminus.find("-")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']存 钱 罐 吐 钱 事 件'})
        elif moneym > money:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你身上的积分没有那么多呢~要不要芙兰借给你一点呀！（笑）'})
        elif moneym == 0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果需要存空气的话，（害羞）芙兰也不是不能帮你存一口啦（对手指）'})
        else :
            moneym = round(moneym,2)
            bankmoney = float(bank.checkbank(qq))
            bankmoney = bankmoney + round(moneym*0.985,2)
            money = money - moneym
            bankmoney = round(bankmoney,2)
            money = round(money,2)
            change.changes(qq,money,5)
            bank.changebank(qq,bankmoney) 
            output = '[CQ:at,qq='+str(qq)+']向您收取了1.5％的服务费，已成功往银行内存款' + str(round(moneym*0.985,2)) + '积分，当前您身上持有' + str(money) + '积分，银行内存有' + str(bankmoney) + '积分。'
            sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})


    elif message.find("fl.bank 2 ") == 0 and len(message) >= 11:
        moneyminus = message[10:]
        bankmoney = float(bank.checkbank(qq))
        if moneyminus == "all":
            moneyminus = str(bankmoney)
        try:
            moneym = float(moneyminus)
        except:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的积分哦~'})
            return 0
        if moneyminus.find("-")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']吐 钞 机 吞 钱 事 件'})
        elif moneym > bankmoney:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你银行内的积分存款没有那么多呢~要不要芙兰借给你一点呀！（笑）'})
        elif moneym == 0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果需要取空气的话，（害羞）芙兰也不是不能帮你喘气啦（对手指）'})
        else :
            moneym = round(moneym,2)
            money = float(getdata.getsd(qq,5))
            bankmoney = bankmoney - moneym
            money = money + round(moneym*0.985,2)
            bankmoney = round(bankmoney,2)
            money = round(money,2)
            change.changes(qq,money,5)
            bank.changebank(qq,bankmoney)
            output = '[CQ:at,qq='+str(qq)+']向您收取了1.5％的服务费,已成功从银行内取款' + str(round(moneym*0.985,2)) + '积分，当前您身上持有' + str(money) + '积分，银行内存有' + str(bankmoney) + '积分。'
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
    else:
        bankmoney = float(bank.checkbank(qq))
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']欢迎您光临幻想乡交通银行！\n您当前的银行账户余额为：' + str(bankmoney) + '\n输入fl.bank 1 [数字]即可往您的银行账户里存款\n输入fl.bank 2 [数字]即可往您的银行账户里取款\n注意：每次成功使用存款/取款功能需支付1.5％的服务费！每天签到时银行会根据您的银行余额支付利息哦~多存点我喜欢！！！（抢走灵梦的话筒）'})

def borrow(message,group,qq):
    if len(message) >= 11:
        if message[9] != " ":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']borrow后面要加空格哦~'})
        else:
            qqmoney = message[10:]
            space = qqmoney.find(" ")
            if space <= 0 :
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式输入错啦，再输一次试试看！'})
            else:
                borrowqq = qqmoney[0:space]
                borrowmoney = qqmoney[space + 1:]
                if not borrowqq.isdigit:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式输入错啦，再输一次试试看！'})
                elif int(borrowqq) == int(qq):
                    name = getdata.getsd(borrowqq,1).strip()
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已成功向' + name + '转账1145141919810积分！等等你说你没那么多钱……？没事您又收到了' + name + '的1145141919810积分转账！这下有钱啦!诶嘿~'})
                else:
                    try:
                        moneym = float(borrowmoney)
                    except:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的积分哦~'})
                        return 0
                    bankmoney = float(bank.checkbank(qq))
                    if borrowmoney.find("-")>=0:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']讹钱可不是什么好行为哦~（笑）'})
                    elif moneym > bankmoney:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你银行内的积分存款没有那么多呢~要不要芙兰借给你一点呀！（笑）'})
                    elif moneym == 0:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果需要转账空气的话，（害羞）芙兰也不是不能帮你喘气啦（对手指）'})
                    else :
                        location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bank', str(borrowqq) + '.txt'))
                        if not os.path.exists(location):
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您所转账的QQ号暂未开通银行账户哦~让他使用一次fl.bank功能就能向他转账啦！'})
                        else:
                            moneym = round(moneym,2)
                            bankmoney2 = float(bank.checkbank(borrowqq)) + moneym
                            bankmoney = bankmoney - moneym
                            bank.changebank(qq,bankmoney)
                            bank.changebank(borrowqq,bankmoney2)
                            name = getdata.getsd(borrowqq,1).strip()
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已成功向' + name + '转账' + str(moneym) + '积分！您当前的银行余额为：' + str(bankmoney) + '，对方的银行账户余额为：' + str(bankmoney2)})
    else:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']输入fl.borrow [QQ号] [积分数/all]就能从自己的银行账户内提取指定积分到其它QQ的银行账户上啦！富哥V50！'})