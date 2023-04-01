#coding=utf-8

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
import remind
from ffmpy import FFmpeg
from pixivpy3 import *

REFRESH_TOKEN = 'LRZahNpdcEjcULZBPrh3c3kpVx5-3jEEAB9xMPppIJo'

g2total = 0
g2left = 0
g2right = 0
repeat = ""
repeatn = 0
repeating = 0
getpicture = 0
urls=''
trytime = 0
picgroup = ""
picqq = ""
codestart = 0
codemiddle = -1
codeend = 0
newsget = 0
newdays = 0

while 1:
    try:
        date = timecheck.times()
        codestart = (codestart + 1) % 114514
        rev = receive.rev_msg()
        now = datetime.datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        days = now.strftime("%d")
        hours = now.strftime("%H")
        minute = now.strftime("%M")
        if hours == "08" and minute == "30" and newsget == 0:
            IMAGE_URL = "https://v2.alapi.cn/api/zaobao?token=dry6TkU6X7uvtWrn&format=image"
            from urllib.request import urlretrieve
            urls = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images', 'news.png'))
            urlretrieve(IMAGE_URL, urls)
            sendmsg.send_msg({'msg_type':'group','number':'719317473','msg':'[CQ:image,file=news.png]'}) 
            sendmsg.send_msg({'msg_type':'group','number':'719317473','msg':'早上好~这里是今天的新闻，祝大家今日万事顺利！'}) 
            sendmsg.send_msg({'msg_type':'group','number':'1164881074','msg':'[CQ:image,file=news.png]'})
            sendmsg.send_msg({'msg_type':'group','number':'1164881074','msg':'早上好~这里是今天的新闻，祝大家今日万事顺利！'}) 
            newsget = 1
        
        if hours == "00" and newsget == 1:
            newsget = 0

        if hours == "00" and minute == "00" and newdays == 0:
            remind.daysrem(year,month,days)
            newdays = 1

        if hours == "01" and newdays == 1:
            newdays = 0
            
        
        if rev["post_type"] == "message":
            if rev["message_type"] == "group": #以下皆为群聊部分
                
                group = rev['group_id']
                codemiddle = codestart
                qq=rev['sender']['user_id']
                message = rev['raw_message']
                favor = int(getdata.getsd(qq,2))
                if message.find("fl.")<0 and getpicture != 1:
                    if message == repeat:
                        repeatn = repeatn + 1
                        if repeatn == 2 and repeating == 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':repeat})
                            repeating = 1
                    else:
                        repeatn = 0
                        repeat = message
                        repeating = 0
                    
                if message.find("fl.name")<0 and message.find("fl.pic")<0 and message.find("fl.repeat")<0: message = message.lower()
                
                urlsss = os.path.abspath(os.path.join(os.path.dirname(__file__),  'guessnum', str(qq) + '.txt'))
                if message.isdigit() and len(message) == 4 and os.path.exists(urlsss):
                    game1.game1(message,urlsss,group,qq)
                                    
                if message.isdigit() and int(message) >= g2left and int(message) <= g2right and bomb.checkingame(qq) :
                    ans = game2.game2(message,group,qq,g2left,g2right,g2total)
                    if ans != -1:
                        g2total = g2total + 1
                    if ans > 100000:
                        g2right = ans - 100000
                    elif ans > 0 :
                        g2left = ans
                
                checkchessfile = os.path.abspath(os.path.join(os.path.dirname(__file__),  'gochess', str(qq) + '.txt'))
                        
                if os.path.exists(checkchessfile) and len(message) <= 3 and len(message) >= 2:
                    chess.chess(message,group,qq,checkchessfile)
                            
                urlsss = os.path.abspath(os.path.join(os.path.dirname(__file__),  'tune', str(qq) + '.txt'))
                if os.path.exists(urlsss) and len(message) <= 3 and len(message) >= 2:
                    guesstune.guesstune(message,group,qq,urlsss)
                        
                if message == '芙兰酱':
                    if qq == 1119194972:
                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']+老公晚上好~[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
                    else:
                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']唔……你好呀~'})

                elif message == "fl.test1":
                    msg = '{"type":"node","data":{"name": "星光是辣鸡","uin": "1119194972","content":"我是辣鸡"} } '
                    msg2 = '{"type":"node","data":{"name": "星光是辣鸡","uin": "1119194972","content":"我是辣鸡"} } '
                    print(msg)
                    b = requests.post(url='http://127.0.0.1:5700/send_group_forward_msg?group_id={0}&messages={1}'.format(group,msg))
                    print(b.text)
                    

                elif message == "fl.news":
                    IMAGE_URL = "https://v2.alapi.cn/api/zaobao?token=dry6TkU6X7uvtWrn&format=image"
                    from urllib.request import urlretrieve
                    urls = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images', 'news.png'))
                    print(urls)
                    urlretrieve(IMAGE_URL, urls)
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=news.png]'}) 

                elif message.find("fl.aitalk") == 0:
                    aitalk.aitalk(message,group,qq)

                elif message.find("fl.ai2") == 0:
                    aitalk.ai2(message,group,qq)

                elif message.find("fl.ai") == 0:
                    aitalk.ai(message,group,qq)
                        
                elif message.find("fl.head") == 0:
                    search.head(message,group,qq)

                elif message.find("fl.help") == 0:
                    search.help(message,group)

                elif message == 'fl.qd' or  message == 'fl.签到':
                    search.qd(group,qq,date,favor)
                    
                elif message == 'fl.qdhelp':
                    output = '[CQ:at,qq='+str(qq)+']\n关于积分：\n签到可随机获得(8＋(今日最高人品/250)) ~ 50积分，\n并可额外获得签到积分的(好感度*10)％~((连续签到天数-1)/50*100)％，若左边界大于右边界两边界互换。如果您有rp重置卡，芙兰建议您将rp重置到更高的时候再签到哦！\n关于银行利息：\n若银行账户内有存款，将会支付1％~3％的利息。可以在每天签到之前将所有的积分存到银行里获取最多的积分哦！'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif message == 'fl.jrrp':
                    search.jrrpuse(group,qq)

                elif message == 'fl.favorup':
                    favor = search.favorup(group,qq)

                elif message == 'fl.raffle':
                    search.raffle(group,qq,date)
                    
                elif message.find("fl.rank")>=0:
                    search.rank(message,group,qq,date)

                elif message.find("fl.name")>=0:
                    search.name(message,group,qq)

                elif message == 'fl.db' or message == 'fl.darkbug' or message == 'fl.miyaktik':
                    songs = random.randint(0,210)
                    lists = [0 for x in range(0,500)]
                    with open(file="Songs.txt", mode='r', encoding="utf-8") as get:
                        for x in range(211):
                            lists[x]=get.readline()
                            lists[x]=lists[x].strip()
                    songid = lists[songs]
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:music,type=163,id='+songid+']'})
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']已为您随机分享大可罢格的音乐~本曲的网易云曲目id：'+songid})

                elif message == 'fl.me':
                    search.me(group,qq,favor,date)

                elif message == 'fl.tap':
                    search.tap(group,qq) 
         
                elif message.find("fl.chess")>=0:
                    chess.startchess(message,group,qq)

                elif message == 'fl.endchess':
                    chess.endchess(group,qq,checkchessfile)           

                elif message.find("fl.game")>=0:
                    game.gamestart(message,group,qq)

                elif message == 'fl.endgame':
                    game.endgame(group,qq)

                elif message.find("fl.piano")>=0:
                    guesstune.usepiano(message,group,qq)

                elif message == 'fl.tune':
                    guesstune.starttune(group,qq)

                elif message == 'fl.flan':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_db.png]'})

                elif message.find("fl.picture")==0:
                    usepicture.picturefind(message,group,qq)

                elif message.find("fl.pixiv")==0:
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'本功能暂时无法使用啦，抱歉orz'})
                    #usepicture.pixivfind(message,group,qq)

                elif message.find("fl.pic")>=0:
                    usepicture.picmix(message,group,qq)
                                
                elif message.find("fl.repeat")==0:
                    search.repeat(message,group,qq)

                elif message.find("fl.store")==0:
                    store.store(message,group,qq,favor)
                    
                elif message == "fl.bag":
                    store.bag(group,qq)

                elif message.find("fl.use")==0:
                    store.use(message,group,qq,favor,date)

                elif message == "fl.place":
                    move.places(group,qq)

                elif message.find("fl.move")==0:
                    move.move(message,group,qq,favor)

                elif message.find("fl.days")==0:
                    remind.daysadd(message,group,qq)

                elif message.find("fl.bank")==0:
                    usebank.banks(message,group,qq)
                
                elif message.find("fl.borrow")==0:
                    usebank.borrow(message,group,qq)
                
                elif message.find("fl.read")>=0:
                    search.read(message,group,qq)

                elif message == 'fl.test001':
                    r = random.randint(1,2)
                    if r == 1:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file=rua.mp3]'})
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file=cota.mp3]'})

                elif message == 'fl.nsrm':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我是吸血鬼，所以我bsr！'})

                elif message == 'fl.mapledise':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=mapledise.jpg]'})

                elif message == 'fl.goodnight' or message == 'fl.night' or message == 'fl.sleep' or message == 'fl.晚安' or message == 'fl.wa':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']晚安哦~愿你在梦里也能看见红魔馆上空的那道七色彩虹XD'})

                elif message == 'fl.goodmorning' or message == 'fl.morning' or message == 'fl.hello' or message == 'fl.hi':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']泥猴哇！我是芙兰朵露斯卡雷特哒！想问我问题可以对我输入指令help！诶……输入指令是啥玩意'})

                elif message == 'fl.starlight' or message == 'fl.星光' or message == 'fl.暗黑色的星光' or message == 'fl.大可罢格' or message == 'fl.meteoroid':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']听说Meteoroid与Margatroid很像，不过实际上，Starlight与Scarlet也很像哦！（笑）'})
                    
                elif message == 'fl.tdll':
                    if qq == 1119194972:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']确实！而你，我的星光，你是唯一的lj。'})
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']不错的自夸[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
                
                elif message.find("fl.kiss")>=0:
                    if qq == 1119194972 or favor >= 100:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1119194972]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']kisskiss~~~'})
                    elif favor <= 5 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']俺拒绝！orz'})
                    elif favor <= 10 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呱！你想干嘛！！！'})
                    elif favor <= 25 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喂！男女授受不亲啦！等等我并没有我们之间要授受的意思……'})
                    elif favor <= 50 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']啊啦…………不太好吧orz（逃）'})
                    elif favor < 100 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']……也不是不行啦，但是如果要你支付100000积分的话，你愿意嘛！（笑）'})

                elif message == 'fl.emotion':
                    emostr=""
                    for x in range(300):
                        emostr = emostr + '[CQ:face,id='+str(x)+']'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg': emostr})

                elif message == 'fl.isdarkbugswife':
                    choose = random.randint(0,6)
                    if choose == 0:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自某D姓死宅的留言）芙兰瘾发作最严重的一次，躺在床上，拼命念大悲咒，难受的一直抓自己眼睛，以为刷推特没事，看到都在发芙兰的图，眼睛越来越大都要炸开了一样，拼命扇自己眼睛，越扇越用力，扇到自己眼泪流出来，真的不知道该怎么办，我真的想芙兰想得要发疯了。我躺在床上会想芙兰，我洗澡会想芙兰，我出门会想芙兰，我走路会想芙兰，我坐车会想芙兰，我工作会想芙兰，我玩手机会想芙兰，我盯着网上的芙兰看，我盯着朋友圈别人照片里的芙兰看，我每时每刻眼睛都直直地盯着芙兰看，我真的觉得自己像中邪了一样，我对芙兰的念想似乎都是病态的了，我好孤独啊!真的好孤独啊!这世界上那么多芙兰为什么没有一个是属于我的。你知道吗?每到深夜，我的眼睛滚烫滚烫，我发病了我要疯狂看芙兰，我要狠狠看芙兰，我的眼睛受不了了，芙兰，我的芙兰"
                    if choose == 1:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自某大姓死宅的留言）有一天芙兰酱在跑步。我冲上去就把她绊倒了。她站起来继续跑，于是我又把她绊倒了。她掏出莱瓦汀问我“你想干嘛！”我对着她大喊：“我碍你！我碍你啊！！！”"
                    if choose == 2:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自某暗姓死宅的留言）是、是的…♡我想要芙兰酱的视频！我真的要芙兰酱的视频！我…好想要…想要得到芙兰酱的视频……♡呜呜、不行了，我已经变成看不到芙兰酱的视频就不行的笨蛋了……啊啊♡好喜欢♡更多的、可爱的视频…是、哪怕有上次的视频也会觉得不够，什么时候都想要看好多好多的视频，除了看芙兰已经什么都想不了了……"
                    if choose == 3:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自暗黑XXXX的留言）我前段时间为了提升自己的文化素养，给自己报了个书法培训班。因为跟我同期的都是小学生所以大家就有点排挤我，看不上我这么大年纪还在学这个。\n本来也没什么，但小学生的恶意真的超乎我的想象，他们说我老头子半只脚进棺材还来学书法，我听到都气哭了。\n我擦干眼眼泪不管他们继续练字，我发誓我一定要练出一笔好字，不能让钱白花。我凝神静气，在纸上认真写出了一行字：芙兰朵露斯卡雷特，超我。[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]"
                    if choose == 4:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自暗XXXX光的留言）我不发疯我说什么？你以为我像你们一样都读过书？都上过学？都知道字怎么打？我从小自闭症，现在一句完整的话都说不完，看到大家在网上都能打字，我也羡慕，所以只能发疯大家说过的话，证明我也会说话，连发疯你都要有意见？你不如把我杀了好好好，一个个的欺负我年纪小，没你们吃的盐多是吧，好啊，那我接下来每一天一罐盐,夠死我自己，看到时候会不会把你们心疼死。可是啊，人和人的体质是不能一概而论的啊，我曾在极度想见芙兰朵露斯卡雷特的情况下流了上百吨眼泪，你们可能不知道，太平洋曾经是沙漠，现在变成了海洋并且孕育出那么多生命，靠的是我一次又一次的发疯的痴狂。 "
                    if choose == 5:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自1119194972的留言）\n今天我们物理开始讲磁力了，物理老师说钢、铁、镍一类的东西都能被磁化，我听完就悟了，大彻大悟。\n课后我问老师：“老师，是不是钢和镍都可以被磁化？”\n老师笑了笑，说：“是的。怎么了？”\n我赶忙追问：“那我对芙兰的爱是不是也可以被磁化？\n老师疑惑了，问为什么？\n我笑着，红了眼眶：“因为我对芙兰的爱就像钢铁打造的拖拉机一样，轰轰烈烈哐哐锵锵。”"
                    if choose == 6:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自-../.-/.-./-.-/-.../..-/--.）\n昨天我到医院看医生，因为最近总是突然心脏痛。\n吃饭的时候，看电影的时候，走在大街上的时候，总是没来由的突然抽痛一下。医生说我这可能是熬夜太多，没啥大问题，但以防万一，还是建议我做一个详细检查。这一做检查就查出病了。\n检查显示我心脏里有异物，我一看片子都差点吓晕——一个金属块，一直藏在我心脏里。医生问我是不是以前受过枪伤，因为那个异物看着像是一枚子弹。我一脸懵逼，说没有啊，我就一普通学生，怎么可能！医生仔细检查了我的胸口，但是怎么也找不到伤口。\n医生也觉得奇怪，说从医这么多年没见过这种情况，如果是吞下去的子弹，不可能会到心脏里；这么粗的子弹也不可能是通过血管进入心脏的。但是有一点是确定的——如果不尽快取出来，我就会有生命危险。\n手术后，我摸摸自己的左胸，那里还缠着绷带——\n医生的技术很好，伤口开得不大，但还是会留下无法消除的疤痕。\n护士端来一个托盘，里面盛着一枚子弹，上面还带着我的血。我把子弹洗干净带回家，做成了吊坠。\n到家后，我打开了芙兰的视频，我突然感觉心脏被狠狠击中。\n我这才想起来，那不是子弹。\n是我第一次见到芙兰时，她明媚的笑容。"
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif message.find("fl.")>=0:
                    newdice = message[4:]
                    if message.find("fl.d")>=0 and newdice.isdigit():
                        search.dice(message,group,qq,newdice)

                    else:
                        if message[0:3] == "fl.":
                            search.defaults(message,group,qq)

                if "[CQ:at,qq=2090027600]" in rev["raw_message"]:
                    continue
            else:
                continue
        else:  # rev["post_type"]=="meta_event":
            continue
    except:
        if codestart == codemiddle:
            sendmsg.send_msg({'msg_type':'private','number':1119194972,'msg':'芙兰在' + str(group) + "群出了故障，快去看看！"})