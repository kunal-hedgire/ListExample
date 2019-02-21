import threading
import time
import logging
import random
#Example 1

'''
def run():
    print("thread")
    return

if __name__ == '__main__':
    for i in range(3):
        t1=threading.Thread(target=run)
        t1.start()
'''
'''
#Example2 passing variable to thread

def run(id):
    print("Thread %s" %id)
    return
if __name__ == '__main__':
    for i in range(4):
        t1 = threading.Thread(target=run,args=(i,))
        t1.start()
'''
'''
#Example 3 naming to thread

def f1():
    print(threading.current_thread().getName(),'Starting')
    time.sleep(1)
    print(threading.current_thread().getName(), 'Ending')

t1=threading.Thread(target=f1)

t1.start()
'''
'''
#Example 4 join and daemon thread

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)
def n():
    logging.debug("n starting")
    logging.debug("n Existing")

def f():
    logging.debug("f Started")
    time.sleep(2)
    logging.debug("f Exit")


if __name__ == '__main__':
    t1=threading.Thread(name="Non Daemon",target=n)
    t2=threading.Thread(name="Daemon",target=f)
    t1.setDaemon(True)

    t1.start()
    t2.start()

    t1.join()
    print(t1.is_alive())
    t2.join()
'''
'''
#Example 5 enumurate

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)
def f():
    t = threading.currentThread()
    r = random.randint(1,10)
    logging.debug('sleeping %s', r)
    time.sleep(r)
    logging.debug('ending')
    return
if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
	    if t is main_thread:
		    continue
    logging.debug('joining %s', t.getName())
    t.join()
'''
'''
#Example 6 run()method and isAlive() method


class MyThread(threading.Thread):
    def run(self):
        time.sleep(2)
        return


if __name__ == '__main__':
    for i in range(3):
        t=MyThread()
        t.start()
        print("Active:",t.is_alive())
        t.join()
        print("Active:", t.is_alive())
'''
"""
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)

class MyThread(threading.Thread):
    def run(self):
        logging.debug("Running")
        return


if __name__ == '__main__':
    for i in range(3):
        t=MyThread()
        print("before start",t.is_alive())
        t.start()
        print("After start", t.is_alive())
"""
'''
class MyThread(threading.Thread):
    def run(self):
        logging.debug("Running")
        for i in range(1, 10):
            print(i)
            time.sleep(2)
        time.sleep(2)
        return
for i in range(20,30):
     print(i)



if __name__ == '__main__':
    t1=MyThread()
    t1.start()

    t1.join()

for i in range(40,50):
    print(i)
'''












