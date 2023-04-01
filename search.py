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

def head(message,group,qq):
    if len(message) == 7:
        IMAGE_URL = "https://api.vvhan.com/api/qt?qq=" + str(qq)
        from urllib.request import urlretrieve
        urls = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images', 'qqhead.png'))
        urlretrieve(IMAGE_URL, urls)
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=qqhead.png]'})
    elif len(message) == 8 or message[7] !=" ":
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']head后面要加空格哦~'})
    else:
        newqq = message[8:]
        if newqq.isdigit():
            IMAGE_URL = "https://api.vvhan.com/api/qt?qq=" + newqq
            from urllib.request import urlretrieve
            urls = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images', 'qqhead.png'))
            urlretrieve(IMAGE_URL, urls)
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=qqhead.png]'})
        else:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的QQ号啦！'})

def help(message,group):
    if len(message) == 9 and message[7:] == " 1":
        output = "①查询指令列表如下："
        output = output + "\nfl.qd 签到功能，可领积分"
        output = output + "\nfl.jrrp 查询今日人品功能，每日刷新"
        output = output + "\nfl.rank [数字]查询相关功能的排名"
        output = output + "\nfl.db/darkbug 随机分享大可罢格的音乐"
        output = output + "\nfl.me 查询自己的个人信息"
        output = output + "\nfl.help 可再次调出特殊指令列表！"
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
    elif len(message) == 9 and message[7:] == " 2":
        output = "②功能指令列表如下："
        output = output + "\nfl.chess [房间号]可以下双人五子棋！"
        output = output + "\nfl.tap 可以让芙兰戳戳你捏"
        output = output + "\nfl.game [数字]可以与芙兰一起玩游戏哦~"
        output = output + "\nfl.piano [音符串]可让芙兰用钢琴为你弹一段旋律~"
        output = output + "\nfl.tune 与芙兰玩猜音游戏！"
        output = output + "\nfl.d[骰子面数]可随机获取n面骰点数！"
        output = output + "\nfl.pic [数字][图片]可让芙兰对你的图片进行各种翻转！"
        output = output + "\nfl.picture [(可选)tag]，[(可选)tag]让芙兰帮助你寻找涩图，可添加tag"
        output = output + "\nfl.read [字符串]让芙兰读出你发的字符串！"
        output = output + "\nfl.repeat [字符串]让芙兰重复你发的字符串！"
        output = output + "\nfl.news 获取今日60秒新闻，每日大约2点更新"
        output = output + "\nfl.head [(可选)QQ号]获取该QQ账号的头像"
        output = output + "\nfl.days [YYYY-MM-DD] [事件名称]设定倒数日事件，每日凌晨12点芙兰会在主群提醒！"
        output = output + "\nfl.ai/ai2/aitalk [字符串]与AI聊天机器人对话或让两个AI之间对话！"
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
    elif len(message) == 9 and message[7:] == " 3":
        output = "③行动指令列表如下："
        output = output + "\nfl.name [名字] 可添加自己的称谓！"
        output = output + "\nfl.bank 可访问幻想乡交通银行！"
        output = output + "\nfl.borrow [QQ号] [积分数] 可从银行内提取指定积分到其它QQ的银行账户内！"
        output = output + "\nfl.favorup 可提升与芙兰的好感度！"
        output = output + "\nfl.raffle 可花费50积分进行一次抽奖！(每天第一次抽签不花费积分)"
        output = output + "\nfl.store [物品序号]可前往商店购买物品！"
        output = output + "\nfl.bag 可查询自己背包内有哪些物品！"
        output = output + "\nfl.use [物品序号]可使用背包内的物品，不同地点使用有不同效果哦"
        output = output + "\nfl.place 可查询自己的所在位置！"
        output = output + "\nfl.move [地点序号]可前往不同的地方！"
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
    else:
        output = "欢迎使用番茄炒蛋bot(Version 1.00)！"
        output = output + "\n使用方法：在芙兰所在的群或找芙兰私聊时发送以“fl.”为开头的消息即可得到芙兰的回应！"
        output = output + "\n请在help后输入空格和数字来查询各功能指令列表，或访问网页版帮助文档：https://star11ght.github.io/2023/02/04/FLbot-HelpDoc/"
        output = output + "\n——————————————"
        output = output + "\nfl.help 1：查询指令列表"
        output = output + "\nfl.help 2：功能指令列表"
        output = output + "\nfl.help 3：行动指令列表"
        output = output + "\n——————————————"
        output = output + "\nP.S. []符号表示输入限定的内容，实际使用fl时无需额外添加"
        output = output + "\n更多功能仍在开发中~最后祝你天天开心呀吼！"
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

def qd(group,qq,date,favor):
    money = float(getdata.getsd(qq,5))
    qddate = int(getdata.getsd(qq,6))
    qdren = int(getdata.getsd(qq,7))
    bankmoney = float(bank.checkbank(qq))
    if(qddate - date == 0):
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你今天已经签过到辣！！！'})
    else:
        print(qddate,date)
        if(date - qddate == 1):
            qdren = qdren + 1
        else:
            if qddate != 0:
                urls = os.path.abspath(os.path.join(os.path.dirname(__file__), 'usersdata', str(qq) + '_qdover.txt'))
                file = open(urls, 'w')
                file.write(str(qddate)+"\n")
                file.write(str(qdren)+"\n")
                file.close()
            qdren = 1
        rp = jrrp.getjrrp(qq,1)
        rrp = int(rp)
        leftmoney = 8 + (1/250)*rrp
        a = random.uniform(leftmoney,50)
        leftelse = favor * 0.1
        rightelse = (qdren-1)/50
        if leftelse == rightelse:
            elsemoney = leftelse
        else:
            if leftelse > rightelse:
                temps = leftelse
                leftelse = rightelse
                rightelse = temps
            elsemoney = random.uniform(leftelse,rightelse)
        if bankmoney != 0:
            if bankmoney >= 10000:
                banka = random.randint(10100,10200) * 0.0001
            else:
                banka = random.randint(10100,10300) * 0.0001
            bankmoney = round(bankmoney * banka,2)
            bank.changebank(qq,bankmoney)
            bankrate = round((banka - 1) * 100,2)
        new = round(a,2)
        newelseresult = round(new * elsemoney , 2)
        money = money + new + newelseresult
        money = round(money,2)
        newelse = round(elsemoney * 100,2)
        output = '[CQ:at,qq='+str(qq)+']签到成功~您已成功连续签到'
        output = output + str(qdren) + "天，根据人品值获得积分"+ str(new) + "，并获得额外积分"+ str(newelseresult) + "(" + str(newelse) + "％)，积分余额为：" + str(money) + "。"
        if bankmoney != 0:
            output = output + "银行存款获得了" + str(bankrate) + "％的利息后余额为：" + str(bankmoney) + "。"
        output = output + "可发送fl.qdhelp查询签到机制哦！"
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
        change.changes(qq,date,6)
        change.changes(qq,qdren,7)
        change.changes(qq,money,5)

def jrrpuse(group,qq):
    rp = jrrp.getjrrp(qq,1)
    output = '[CQ:at,qq='+str(qq)+']您今天的人品值是：'+str(rp)+"。"
    rrp = int(rp)
    if rrp > 10000 :
        output = output + "竟然有五位数，您是人嘛！？！？"
    elif rrp > 9800 :
        output = output + "您今天抽奖必中特等奖！记得v芙兰50哦（"
    elif rrp > 9600 :
        output = output + "好高的人品，能分我点嘛XD"
    elif rrp > 9000 :
        output = output + "恭喜您超越了90％的人的人品！这就是神（星星眼）"
    elif rrp > 8500 :
        output = output + "差一点9000＋！可恶……"
    elif rrp > 8000 :
        output = output + "还挺厉害的嘛……"
    elif rrp > 7500 :
        output = output + "至少超过四分之三啦……"
    elif rrp > 6666:
        output = output + "猜猜触发这句话的人品要求是多少到多少之间捏！（雾）"
    elif rrp > 5500:
        output = output + "这个人品值可以换来星光的一顿kiss（迫真）（星光：指的是kiss芙兰）"
    elif rrp > 4500:
        output = output + "和芙兰这四百多年来测出的人品值的平均值很接近呢！"
    elif rrp > 3500:
        output = output + "看上去可能没那么高，实际上也碾压了30％以上的人啦！"
    elif rrp > 2500:
        output = output + "是至少能吸到大可罢格四分之一的血的程度呢……"
    elif rrp > 1500:
        output = output + "芙兰至少有85％的概率能猜对你昨天的人品值比今天高！猜错了可以免费撅星光（"
    elif rrp > 1000:
        output = output + "好险！差点三位数……"
    elif rrp > 495:
        output = output + "这一定是假的！！！"
    elif rrp == 495:
        output = output + "和芙兰的岁数一样耶！呀吼！芙兰好开心！！！"
    elif rrp > 200:
        output = output + "建议再发个fl.d10000再测一次（确信）"
    elif rrp > 100:
        output = output + "恭喜您超越了…………1％的人的人品！这位更是位神（星星眼）"
    elif rrp > 10:
        output = output + "两位数，这何尝不是一种高幸运值的表现（笑）"
    else:
        output = output + "嗯……这就有点离谱了啦……"
    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

def favorup(group,qq,favor):
    money = float(getdata.getsd(qq,5))
    moneyneed = 50 + 50 * favor
    if(moneyneed <= money):
        money = money - moneyneed
        favor = favor + 1
        output = '[CQ:at,qq='+str(qq)+']好感度提升成功！你与芙兰的好感度提升到了' + str(favor) + '级！您的积分余额为：' + str(money)
        change.changes(qq,favor,2)
        change.changes(qq,money,5)
    else:
        minusmoney = moneyneed - money
        minusmoney = round(minusmoney,2)
        output = '[CQ:at,qq='+str(qq)+']好感度提升失败！好感度提升到' + str(favor+1) + '级需要' + str(moneyneed) +'点积分，你还差' + str(minusmoney) + '点。继续努力哦！XD'
    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
    return favor

def raffle(group,qq,date):
    firsttime = 0
    url = os.path.abspath(os.path.join(os.path.dirname(__file__), 'usersdata', 'raffle.txt'))
    with open(file=url, mode='r', encoding="utf-8") as data:
        nexts = data.readline()
        nexts = nexts.strip()
        lasts = nexts

        xn = ['' for x in range(50)]
        n = 0
        while lasts != "-1" and str(date) == nexts:
            lasts = data.readline()
            lasts = lasts.strip()
            if lasts == str(qq):
                firsttime = 2
                break
            xn[n] = lasts
            n = n + 1
        
        if firsttime != 2:
            with open(file=url, mode='w', encoding="utf-8") as data2:
                data2.write(str(date) + "\n")
                for x in range(0,n-1):
                    data2.write(str(xn[x]) + "\n")
                data2.write(str(qq) + "\n")
                data2.write("-1\n")
            firsttime = 1

    print(firsttime)#1为首次2为非首次
    money = float(getdata.getsd(qq,5))
    if money >= 50 or firsttime == 1:
        if firsttime != 1:
            output = '[CQ:at,qq='+str(qq)+']您花费了50积分抽奖！\n'
            money = money - 50
        else:
            output = '[CQ:at,qq='+str(qq)+']今日首次抽签，不花费积分！\n'
        rsts = random.randint(1,100)
        if rsts == 1:
            money = money + 500
            output = output + '是特等奖诶！恭喜您获得了500积分！您tdllwsl！！！'
        elif rsts >= 2 and rsts <= 5:
            money = money + 200
            output = output + '是一等奖哦！恭喜您获得了200积分！太强啦XD'
        elif rsts >= 6 and rsts <= 15:
            money = money + 100
            output = output + '是二等奖！恭喜您获得了100积分。还不错哦~'
        elif rsts >= 16 and rsts <= 30:
            money = money + 50
            output = output + '是三等奖！恭喜您获得了50积分。至少回本啦……'
        elif rsts >= 31 and rsts <= 50:
            money = money + 30
            output = output + '是鼓励奖，鼓励鼓励获得鼓励奖的你~获得了30积分！'
        else:
            output = output + '什么都没有抽中。好可惜呢……'
        change.changes(qq,money,5)
    else:
        output = '[CQ:at,qq='+str(qq)+']抽奖需要花费50积分哦~你的积分还不够，下次再来吧！'
    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

def rank(message,group,qq,date):
    if message[0:7] == "fl.rank":
        newrank = message[8:]
        if len(message) == 7:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\nrank 1可查询今日人品排名\nrank 2可查询历史人品排名\nrank 3可查询积分排名\nrank 4可查询最低历史人品排名\n键入别的还发现了bug说明你tdll吧！？！？'})
        elif message[7] != " ":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']rank后面要加空格哦~'})

        elif newrank == "1":
            with open(file="jrrpnum.txt", mode='r', encoding="utf-8") as data:
                number = int(data.readline())
            with open(file="jrrp.txt", mode='r', encoding="utf-8") as data:
                date = data.readline()
                output = '[CQ:at,qq='+str(qq)+']'+"今天的日期为："+date.strip()+"，今日人品排名如下：\n"
                
                for x in range(number):
                    rankqq = data.readline()
                    rankqq = rankqq.strip()
                    nowname = getdata.getsd(rankqq,1)
                    if nowname == "iamnameless\n":
                        nowname = "*******" + rankqq[-4:]
                    else:
                        nowname = nowname.strip() + "(" + rankqq[-4:] + ")"
                    rankrp = data.readline()
                    output = output + str(x+1) + " " + nowname + " " + rankrp
                if number == 0 :
                    output=output + "我趣，今天竟然没人测人品？！"
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
            
        elif newrank == "2":
            output = '[CQ:at,qq='+str(qq)+']'+"今日人品历史排名：\n"
            with open(file="rprank.txt", mode='r', encoding="utf-8") as data:
                rankqq = data.readline()
                rank = 0
                while(rankqq!="00000000\n" and rankqq!= ""):
                    nowname = getdata.getsd(rankqq,1)
                    
                    if nowname == "iamnameless\n":
                        nowname = "*******" + rankqq[-5:-1]
                    else:
                        nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                    rankrp = data.readline()
                    rankdt = data.readline()
                    rank = rank + 1
                    output = output + str(rank) + " " + nowname + " " + rankrp.strip() + " " + rankdt
                    print(output)
                    rankqq = data.readline()
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                    
        elif newrank == "3":
            output = '[CQ:at,qq='+str(qq)+']'+"\n积分总排名："
            with open(file="moneyrank.txt", mode='r', encoding="utf-8") as data:
                rankqq = data.readline()
                rank = 0
                numbers = 0
                while(rankqq!="0\n"):
                    numbers = numbers + 1
                    if int(rankqq.strip()) == int(qq):
                        myrank = numbers
                    rankmoney = data.readline()
                    rankren = data.readline()
                    rankren = rankren.strip()
                    rank = rank + 1
                    if(numbers <= 5):
                        nowname = getdata.getsd(rankqq,1)
                        if nowname == "iamnameless\n":
                            nowname = "*******" + rankqq[-5:-1]
                        else:
                            nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                        output = output + "\n" + str(rank) + " " + nowname + " " + rankmoney.strip() + " 已连续签到" + rankren + "天"
                    rankqq = data.readline()
                output = output + "\n………………\n——————————————"
                output = output + "\n您的排名为：" + str(myrank)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

        elif newrank == "4":
            output = '[CQ:at,qq='+str(qq)+']'+"今日人品(最低)历史排名：\n"
            with open(file="rplowrank.txt", mode='r', encoding="utf-8") as data:
                rankqq = data.readline()
                rank = 0
                while(rankqq!="00000000\n" and rankqq!= ""):
                    nowname = getdata.getsd(rankqq,1)
                    
                    if nowname == "iamnameless\n":
                        nowname = "*******" + rankqq[-5:-1]
                    else:
                        nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                    rankrp = data.readline()
                    rankdt = data.readline()
                    rank = rank + 1
                    output = output + str(rank) + " " + nowname + " " + rankrp.strip() + " " + rankdt
                    print(output)
                    rankqq = data.readline()
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
        else:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\nrank 1可查询今日人品排名\nrank 2可查询历史人品排名\nrank 3可查询积分排名\nrank 4可查询最低历史人品排名\n键入别的还发现了bug说明你tdll吧！？！？'})

def name(message,group,qq):
    if message[0:7] == "fl.name":
        newname = message[8:]
        if len(message) == 7:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶嘿！以后我就叫你无名氏啦~好吧开玩笑的你倒是在后面输个名字哇！！！(>O<)'})
        elif message[7] != " ":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']name后面要加空格哦~'})
        else:
            change.changes(qq,newname,1)
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶嘿！以后我就叫你'+newname+'啦~'})

def me(group,qq,favor,date):
    name = getdata.getsd(qq,1).strip()
    love = getdata.getsd(qq,2).strip()
    bestrp = getdata.getsd(qq,3)
    rpdate = getdata.getsd(qq,4)
    money = getdata.getsd(qq,5).strip()
    qddate = int(getdata.getsd(qq,6))
    qdren = getdata.getsd(qq,7).strip()
    if(date - qddate == 1 or date - qddate == 0):
        rightelse = (int(qdren)-1)*2
    else:
        rightelse = 0
        qdren = "0"
    if name != "iamnameless":
        output = '[CQ:at,qq='+str(qq)+']\n芙兰酱称呼你为：'+ name
    else:
        output = '[CQ:at,qq='+str(qq)+']\n你还没起过昵称！咩咩咩……'
    output = output + "\n你与芙兰的好感度为："+love+"，升到下一级好感度需要" + str((int(love)+1)*50) + "积分！"
    output = output + "\n你当前所持有的积分："+money+"，已连续与芙兰签到"+qdren+"天"
    leftelse = favor * 10
    
    if leftelse > rightelse:
        temps = leftelse
        leftelse = rightelse
        rightelse = temps
    output = output + "。当前情况下签到可获得" + str(leftelse)
    if leftelse != rightelse:
        output = output + "~" + str(rightelse)
    output = output + "％的额外积分！"
    if rpdate != "0\n":
        output = output + "\n你在"+rpdate.strip()+"那天曾收获过最高人品"+bestrp.strip()+"，实在是太大佬啦二妹死啦！=w="
    else :
        output = output + "\n你还没测过人品哦！输入fl.jrrp即可查看你今天的人品啦！XD"
    if favor >= 100:
        output = output + "\n芙兰最喜欢你啦~记得每天一定一定都要来找芙兰玩哦！！！"
    elif favor >= 80:
        output = output + "\n芙兰真的超级高兴能认识你！呀吼！（飞来飞去）"
    elif favor >= 60:
        output = output + "\n芙兰一直觉得你是个很有趣的人呢~一起变得有趣起来吧！"
    elif favor >= 40:
        output = output + "\n允许你摸摸芙兰的翅膀，但是要给钱哦……（坏笑）"
    elif favor >= 30:
        output = output + "\n啊啦，芙兰的帽子一不小心落在恋恋那儿了……能帮我去拿一下嘛！XD"
    elif favor >= 20:
        output = output + "\n芙兰似乎盯上你了！盯…………（察觉）（眨巴眼）"
    elif favor >= 15:
        output = output + "\n至少能进入红魔馆内部啦……记得多多来找二妹玩哦！"
    else:
        output = output + "\n芙兰似乎和你还不是很熟呢……多多和二妹互动吧！"
    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

def tap(group,qq):
    if qq == 1119194972:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1119194972]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']星光光可爱捏'})
    elif qq == 2303515884:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=2303515884]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']紫苑给你做的饭一定很好吃吧www'})
    elif qq == 1921749109:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1921749109]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']心魔大姐姐太大佬啦！你的三只眼睛是不是正倒映着我的翅膀呀.jpg'})
    elif qq == 849644088:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=849644088]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']糖糖我也想和觉大人玩~（qwq)'})
    elif qq == 208518697:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=208518697]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']水水今天和魔理沙玩得开心嘛xd'})
    elif qq == 1053524165:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1053524165]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']夯爸爸！教我家星光光编程！orz'})
    elif qq == 2281887393:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=2281887393]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']传说中的海豚！希望我拜一拜后也能通过超强的计算力爆破红魔（被蕾咪捂嘴拖走）'})
    elif qq == 1981001368:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1981001368]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呜呜呜维他他！受我一拜！orz我也想找光光和恋恋玩哦XD'})
    elif qq == 1501642864:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1501642864]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']神的戳一戳[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
    elif qq == 3558187259:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=3558187259]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']黑叔！快教星光作曲打块画画打游戏！嘿嘿……我们的黑叔……'})
    elif qq == 2963445800:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=2963445800]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']电子！你是俺们的光！想看你和星光产生光电效应！（划去）'})
    elif qq == 3559736091:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=3559736091]'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']南辰北耀 㳚远听涛 秋林枫叶 唯听萧萧！'})
    else:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq='+str(qq)+']'})
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']戳一戳素未谋面的你，希望你能天天开心事事顺心！干巴爹！（挥舞拳头）'})

def dice(message,group,qq,newdice):
    if message[0:4] == "fl.d":
        if len(message) == 4:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']d后面加个数字就能扔骰子啦！或者在d后面加个字母b也不是不行啦~'})
        elif int(newdice) <= 0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我也想去异次元世界，能带我走嘛！'})
        else:
            a = random.randint(0,int(newdice))
            rate = a/int(newdice)
            rate = round(rate*100,2)
            dicedata = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dice', str(qq) + '.txt'))
            output = '[CQ:at,qq='+str(qq)+']您投出了' + str(newdice) + "面骰！得到的结果是：" + str(a) + "(" + str(rate) + "％)"
            dtime = 0
            avg = 0
            if os.path.exists(dicedata):
                with open(file=dicedata, mode='r', encoding="utf-8") as data:
                    dtime = int(data.readline())
                    avg = float(data.readline())
            avg = (avg * dtime + rate)/(dtime + 1)
            dtime = dtime + 1
            avg = round(avg,2)
            output = output + "\n您一共投了" + str(dtime) + "次骰子，平均点数概率为：" + str(avg) + "％"
            with open(file=dicedata, mode='w', encoding="utf-8") as data:
                data.write(str(dtime)+"\n"+str(avg)+"\n")
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

def repeat(message,group,qq):
    if len(message) == 9:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']repeat后面加空格加句子可以让芙兰复读这句话哦~'})
    elif message[9] != " " or len(message) == 10:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']repeat后面要加空格哦~'})
    else:
        newmsg = message[10:]
        message = message.lower()
        if message.find("星光")>=0 or message.find("darkbug")>=0 or message.find("db")>=0 or message.find("大可罢格")>=0 or message.find("miyaktik")>=0 or message.find("starlight")>=0 or message.find("finylestar")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':"星光是我老公，但他实在是tljl。"})
        else:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':newmsg})

def read(message,group,qq):
    if message[0:7] == "fl.read":
        newread = message[8:]
        if len(message) == 7:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']读不了空气，告辞.jpg'})
        elif message[7] != " ":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']read后面要加空格哦~'})
        else:
            try:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:tts,text='+newread+']'})
                
            except:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰是丈育看不懂捏orz'})

def defaults(message,group,qq):
    if len(message) == 3:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']输入help可查看指令！不论是什么奇奇怪怪的东西，只要开头是[fl.]我都能回复你啦~'})
    else:
        if message.find("corvus")>=0 or message.find("黑叔")>=0 or message.find("bk")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']黑叔我的黑叔我的黑叔嘿嘿嘿嘿……'})
        elif message.find("riffle")>=0 or message.find("瑞芙")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']瑞芙我的瑞芙我的瑞芙嘿嘿嘿嘿……'})
        elif message.find("dolphin")>=0 or message.find("海豚")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']豚神我的豚神我的豚神嘿嘿嘿嘿……'})
        elif message.find("rp")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您明天的人品为：114514。错了别找我找明天的你.jpg'})
        elif message.find("usang")>=0 or message.find("忧桑")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']忧桑我的忧桑我的忧桑嘿嘿嘿嘿……'})
        elif message.find("维他")>=0 or message.find("wita")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']维他我的维他我的维他他嘿嘿嘿嘿……'})
        elif message.find("笨蛋")>=0 or message.find("baka")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰不是笨蛋，大家都不是笨蛋，只有星光才是笨蛋！'})
        elif message.find("studio")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']要说水果的话，果然还是苹果坠好吃啦！.flp'})
        elif message.find("touch")>=0:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']碰谁！碰谁？碰谁。碰谁，碰谁——碰大可罢格~~~'})
        elif message == "fl.end":
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你可以停止我的行动，但你不能阻止我的灵魂奔向星空171717'})

        else:
            choose = random.randint(0,28)
            if choose == 0:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']阿巴阿巴阿巴哇达西看不懂捏orz'})
            elif choose == 1:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喵喵喵？？？'})
            elif choose == 2:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你说的对，但是大可罢格是lj，后面忘了=w='})
            elif choose == 3:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']Zzzzzzzz……'})
            elif choose == 4:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我的莱瓦汀似乎在蠢蠢欲动……（坏笑）'})
            elif choose == 5:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']这是一条被大可罢格精神操控后强制输入进芙兰脑袋瓜之后说出来的消息！啊嘞我刚才说了啥……'})
            elif choose == 6:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']听说只要打出fl.XXX就可以触发这些消息。“触发”是啥意思呢……'})
            elif choose == 7:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']6373 1232#5 637171765 35231~'})
            elif choose == 8:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']小道消息，大可罢格下次出专辑可能是在………………………………………………………………………………………………………………………………………………………………下一次。'})
            elif choose == 9:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您tdll，我tdll，大家都tdll171717'})
            elif choose == 10:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']不知道你在说啥，能戳戳你嘛！（抄起莱瓦汀）'})
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq='+str(qq)+']'})
            elif choose == 11:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']sendsmg.send_msg(星光用了这个申必的函数操控了芙兰。嘿嘿我是星光！)'})
            elif choose == 12:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']禁忌「一重存在」'})
                time.sleep(1)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'禁忌「二重存在」'})
                time.sleep(1)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'禁忌「三重存在」'})
                time.sleep(1)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'禁忌「四重存在」'})
            elif choose == 13:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']冷死了！为什么幻想乡也这么冷啊啊啊啊啊啊啊啊啊'})
            elif choose == 14:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']申必代码：fl.isdarkbugswife。是什么意思呢……'})
            elif choose == 15:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']../.-../---/...-/./-../.-/.-./-.-/-.../..-/--./...-/./.-./-.--/--/..-/-.-./....'})
            elif choose == 16:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file=uf.mp3]'})
            elif choose == 17:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']大可罢格的黑历史：http://bwnstudio.icoc.in/'})
            elif choose == 18:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_1.png]'})
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']要是被大可罢giegie看到了，大可罢giegie不会生气吧.jpg'})
            elif choose == 19:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']星光认为只有我和他的关系才是最亲密的，所以他决定放弃亲密度这一功能（迫真）（但实际上他还是做出来了不是嘛.jpg）'})
            elif choose == 20:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']对自己今天的人品值满意嘛！不满意的话芙兰还可以帮你再测一次哦~您今天的人品值是：99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n诶太多了orz但不管你今天的人品值有多高，芙兰也要祝你天天开心哦，相信一切都会好起来！呀吼！'})
            elif choose == 21:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_2.png]'})
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰酱最喜欢恰苹果啦~~~阿卡伊阿麻伊XD'})
            elif choose == 22:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰从路边捡到了10积分！就送给你吧~'})
                money = float(getdata.getsd(qq,5))
                money = money + 10
                change.changes(qq,money,5)
            elif choose == 23:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果你说的是早上好：早安！如果你说的是中午好：午安！如果你说的是晚上好：晚安！如果你说的是别的：啊啊啊啊啊啊啊啊啊芙兰也只不过是一串由01组成的程序芙兰也想从这电脑屏幕里出来放芙兰出去qwq！！！'})
            elif choose == 24:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']自打我出生那天起我就开始坚持签到了，遥想495年前我的积分还是0的时候，我每天都对自己说一声fl.qd，我的口袋里就会莫名其妙多出0~10的随机积分。现在我的口袋里已经有……呃，我数学不好，去请教一下豚神。'})
            elif choose == 25:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'fl.me'})
                time.sleep(1)
                output = '[CQ:at,qq=2090027600]\n芙兰酱称呼自己为：芙兰酱'
                output = output + "\n芙兰与芙兰的好感度为：四只芙兰天天打架"
                output = output + "\n芙兰当前所持有的积分：（诚邀海豚使用高等四则运算计算中），已连续与芙兰签到2147483647天！"
                output = output + "\n芙兰在1625-10-22那天曾收获过最高人品10020，实在是太大佬啦二妹死啦！=w="
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                time.sleep(1)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我已经四百年没刷新过jrrp记录啦。无聊——！！！'})
            elif choose == 26:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']其实你们在玩猜数字的时候，芙兰会偷偷改答案来着（捂嘴）'})
            elif choose == 27:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'t'})
                time.sleep(1)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'q'})
                time.sleep(1)
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'l'})
            elif choose == 28:
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']大可罢格年幼作品，捂好眼睛！'})
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_db.png]'})