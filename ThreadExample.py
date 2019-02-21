import threading
import time
import logging
import random
'''
#passing argumetns or parameters in threading
def run(id):
    print("thread Function %s"%(id))
    return

if __name__ == '__main__':
    for i in range(3):
        t=threading.Thread(target=run,args=(i,))
        t.start()
'''
'''
#Identifying Threads with print

def f1():
    print(threading.currentThread().getName(),'starting')
    time.sleep(1)
    print(threading.currentThread().getName(), 'Exiting')

def f2():
    print(threading.currentThread().getName(), 'starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def f3():
    print(threading.currentThread().getName(), 'starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

if __name__ == '__main__':
    t1=threading.Thread(name='f1',target=f1)
    t2 = threading.Thread(name='f2', target=f2)
    t3 = threading.Thread(name='f3', target=f3)

    t1.start()
    t2.start()
    t3.start()
'''
'''
#Threading with logging without file

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-9s) %(message)s')

def f1():
    logging.debug('starting')
    time.sleep(1)
    logging.debug('Exiting')

def f2():
    logging.debug('starting')
    time.sleep(2)
    logging.debug('Exiting')


def f3():
    logging.debug('starting')
    time.sleep(3)
    logging.debug('Exiting')

if __name__ == '__main__':

    t1=threading.Thread(target=f1,name='f1')
    t2=threading.Thread(name='f2',target=f2)
    t3=threading.Thread(name='f3',target=f3)

    t1.start()
    t2.start()
    t3.start()
'''
'''
#daemon thread-->only for background process and its not blocking a main thread form exiting
#Using daemon threads is useful for services where there may not be an easy way to interrupt the thread or
# where letting the thread die in the middle of its work without losing or corrupting data.

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-9s) %(message)s')

def f():
    logging.debug('starting')
    logging.debug('Exit')

def d():
    logging.debug('starting')
    time.sleep(5)
    logging.debug('Exiting')

if __name__ == '__main__':

    t1=threading.Thread(name='f',target=f)
    t2=threading.Thread(name='d',target=d)
    t2.setDaemon(True)

    t1.start()
    t2.start()
'''
'''
#join()
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-9s) %(message)s')
def f():
    logging.debug('starting')
    logging.debug('Exit')

def d():
    logging.debug('starting')
    time.sleep(5)
    logging.debug('Exiting')

if __name__ == '__main__':

    t=threading.Thread(name='non-daemon',target=f)

    t1=threading.Thread(name='daemon',target=d)
    t1.setDaemon(True)

    t1.start()
    t.start()

    t1.join(7.0)
    print('t1.isAlive',t1.is_alive())
    t.join()
'''
'''
#enumerate

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

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
#own thread 
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)


class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')
        return

if __name__ == '__main__':

    for i in range(3):
        t=MyThread()
        t.start()
'''
'''
#passing args and kwargs

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)

class MyThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None,args=(), kwargs=None):
        super(MyThread,self).__init__(group=group, target=target,name=name,)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return
if __name__ == '__main__':
    for i in range(3):
        t = MyThread(args=(i,), kwargs={'a': 1, 'b': 2})
        t.start()
'''
'''
#timer object

def run():
    print('hello timer')
    return

if __name__ == '__main__':
    t1=threading.Timer(3.0,run)
    t1.start()
'''
'''
#wait and set method of event method
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other things')


if __name__ == '__main__':
    e = threading.Event()
    t1 = threading.Thread(name='blocking',target=wait_for_event,args=(e,))
    t1.start()

    t2 = threading.Thread(name='non-blocking',target=wait_for_event_timeout,args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('Event is set')
'''
'''
#Lock object - Acquire and Realease


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired a lock')
            self.value = self.value + 1
        finally:
            logging.debug('Released a lock')
            self.lock.release()


def worker(c):
    for i in range(2):
        r = random.random()
        logging.debug('Sleeping %0.02f', r)
        time.sleep(r)
        c.increment()
    logging.debug('Done')


if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()

    logging.debug('Waiting for worker threads')
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Counter: %d', counter.value)
'''
'''
#using lock with statement.

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s', )



def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_not_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    w = threading.Thread(target=worker_with, args=(lock,))
    nw = threading.Thread(target=worker_not_with, args=(lock,))

    w.start()
    nw.start()
'''
#Produce and consume



















