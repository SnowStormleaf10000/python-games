import time

count = 0

def Count():
    global count
    time.sleep(1)
    count += 1
    print(count)
    Count()

Count()
