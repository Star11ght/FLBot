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

def gamestart(message,group,qq):
    if message[0:7] == "fl.game":
        newgame = message[8:]
        if len(message) == 7:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']在game后键入空格与数字1可玩1A2B猜数字\n在game后键入空格与数字2可玩寻找炸弹人偶\n输入fl.endgame可与芙兰停止游戏\n其它游戏仍在开发中！啊确实是芙兰自己闲着无聊开发的啦才不是什么大可罢格写的（确信）'})
        
        elif message[7] != " ":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']game后面要加空格哦~'})

        elif newgame == "1":
            print("检查游戏进程")
            if bomb.checkingame(qq):
                print("游戏2正在进行中\n")
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你还在进行别的游戏哦~玩好这把游戏或者输入fl.endgame后再来玩这个吧！'})
            elif os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'guessnum', str(qq) + '.txt'))):
                print("游戏1正在进行中\n")
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喂这局游戏还没玩好咧！！！'})
            else:
                print("游戏可启动\n")
                guessnum.numberguess(qq)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n开始了哦！我已经想好了四个互不相同的数字，接下来你只需要直接打出这四个数字芙兰就能知道你猜的是什么啦！\n然后芙兰就会告诉你，你所猜的这四个数字与我想的数字中有几个数字是位置和数都符合（用A表示），有几个数只有数字符合（用B表示）！\n一共8次机会哦！那就开始吧~\nPS：输入fl.game 114514可查看本游戏案例'})
                

        elif newgame == "2":
            print("检查游戏进程",bomb.checkingame(qq))
            if os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'guessnum', str(qq) + '.txt'))):
                print("游戏1正在进行中\n")
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你还在进行别的游戏哦~玩好这把游戏或者输入fl.endgame后再来玩这个吧！'})
            elif bomb.checkingame(qq):
                print("游戏2正在进行中\n")
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喂这局游戏还没玩好咧！！！'})
            else:
                print("游戏可启动\n")
                bnum = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bomb', 'num.txt'))
                with open(file=bnum, mode='r', encoding="utf-8") as data:
                    bombnumber = int(data.readline())    
                bomb.joingame(qq)
                if bombnumber == 0:
                    g2left = 1
                    g2right = 100000
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您已启动新一轮的找炸弹游戏！\n芙兰将自己的一只炸弹人偶藏进了1-100000号红魔馆房间中，接下来你只需要每打出一个在规定范围内的房间号，芙兰就会告诉你一个新的房间范围，如此往复~\n多人游戏中第一个找到炸弹人偶的人可以获得积分奖励哦！那就，开始吧！(*^▽^*)'})
                else:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您已加入本轮找炸弹游戏！\n芙兰将自己的一只炸弹人偶藏进了1-100000号红魔馆房间中，接下来你只需要每打出一个在规定范围内的房间号，芙兰就会告诉你一个新的房间范围，如此往复~\n多人游戏中第一个找到炸弹人偶的人可以获得积分奖励哦！那就，开始吧！(*^▽^*)'})
            

        elif newgame == "114514":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n例如：答案为1234\n案例输入1：5678 案例回答1：0A0B（无相符数字）\n案例输入2：4325 案例回答2：0A3B（有3个相符数字，但位置对不上）\n案例输入3：1238 案例回答3：3A0B（有3个相符数字且位置全对上了）'})
                        
        else :
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']在game后键入空格与数字1可玩1A2B猜数字\n在game后键入空格与数字2可玩寻找炸弹人偶\n输入fl.endgame可与芙兰停止游戏\n其它游戏仍在开发中！啊确实是芙兰自己闲着无聊开发的啦才不是什么大可罢格写的（确信）'})

def endgame(group,qq):
    if os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'guessnum', str(qq) + '.txt'))):
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呜呜呜好可惜……下次还要再来找我玩哦！(已结束1A2B猜数字）'})
        guessnum.gameend(qq)
        
    elif bomb.checkingame(qq):
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呜呜呜好可惜……下次还要再来找我玩哦！（已结束寻找炸弹人偶）'})
        bomb.exitgame(qq)
        
    else:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']蛤？我们在……在玩游戏嘛！我怎么不知道orz憋骗我啊喂！！！'})