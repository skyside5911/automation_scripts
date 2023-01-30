from threading import *
import threading
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
class MyThread(Thread):
    def fun(self):
        for i in range(10):
            print("class_thread {}".format(i))
ob=MyThread()
tt=Thread(target=ob.fun)
tt.start()
for i in range(10):
    print("main_thread_1")
print(threading.current_thread().getName())
now = datetime.now()

