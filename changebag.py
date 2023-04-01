import os

def changebags(qq,thing,choose):
    check = os.getcwd()
    location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bag', str(qq) + '.txt'))
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write("-1\n")
            data.close()
    
    things = [0 for i in range(100)]

    with open(file=location, mode='r', encoding="utf-8") as data:
        while(1):
            x = int(data.readline())
            if x == -1 :
                break
            things[x] = int(data.readline())

    things[int(choose)] = int(thing)

    with open(file=location, mode='w', encoding="utf-8") as data:
        for i in range(1,30):
            if things[i] != 0 :
                data.write(str(i) + "\n")
                data.write(str(things[i]) + "\n")
        data.write("-1\n")
        data.close()
