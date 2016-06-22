import time
import os
for x in range(0,120):
    t=time.localtime()
    hour=t[3]
    minute=t[4]
    second=t[5]
    print("H: "+str(hour))
    print("M: "+str(minute))
    print("S: "+str(second))
    time.sleep(1)
    os.system('cls')


