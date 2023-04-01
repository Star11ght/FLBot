import sendmsg
import guessnum
import change
import getdata

def game1(message,urlsss,group,qq):
    location = urlsss
    answer = [0 for x in range(0,5)]
    key = [0 for x in range(0,5)]
    history = ["" for x in range(0,10)]
    hisans = ["" for x in range(0,10)]
    samecheck = 0
    numlocate = 0
    numsame = 0
    for x in range (4):
        answer[x] = int(message[x])
    for x in range (0,4):
        for y in range (x+1,4):
            print(answer[x],answer[y])
            if answer[x] == answer[y]:
                samecheck = samecheck + 1
    if samecheck != 0:
        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']不可以输入相同的数字啦！这次就不算你机会吧orz'})
    else :
        with open(file=location, mode='r', encoding="utf-8") as data:
            for x in range (4):
                key[x] = int(data.readline())
                if key[x] == answer[x]:
                    numlocate = numlocate + 1
            chance = int(data.readline())
            if numlocate != 4:
                for x in range (8-chance):
                    history[x] = history[x] + data.readline()
                    hisans[x] = hisans[x] + data.readline()
            
        if numlocate == 4:
            money = float(getdata.getsd(qq,5))
            add = float(chance) * 5
            money = money + add
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']恭喜你猜中啦！你tdllwsl！想玩还可以再找芙兰玩哦~（已获得积分' + str(add) + ")"})
            change.changes(qq,money,5)
            guessnum.gameend(qq)

        else:
            if chance == 1 :
                output = '[CQ:at,qq='+str(qq)+']呜呜呜好可惜，机会用完啦！正确的答案是'
                for x in range (4):
                    output = output + str(key[x])
                output = output + '，下次再来试试吧！XD'
                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                guessnum.gameend(qq)

            else:
                for x in range (4):
                    for y in range (4):
                        if key[x] == answer[y]:
                            numsame = numsame + 1
                numsame = numsame - numlocate
                chance = chance - 1
                output = '[CQ:at,qq='+str(qq)+']\n你本次的猜测的结果为：'+ str(numlocate) + "A"+ str(numsame) + "B。\n你还剩下" + str(chance) + "次机会，再试试看喵~\n历史猜测记录："
                for y in range (8 - chance - 1):
                    history[y] = history[y].strip()
                    hisans[y] = hisans[y].strip()
                    output =  output + "\n" + history[y] + " " + hisans[y]
                output =  output + "\n" + message + " " + str(numlocate) + "A"+ str(numsame) + "B"
                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                with open(file=location, mode='w', encoding="utf-8") as data:
                    for x in range (4):
                        data.write(str(key[x])+"\n")
                    data.write(str(chance)+"\n")
                    for x in range ( 8 - chance - 1):
                        data.write(str(history[x])+"\n")
                        data.write(str(hisans[x])+"\n")
                    data.write(message + "\n")
                    data.write(str(numlocate) + "A"+ str(numsame) + "B\n")
                    data.close