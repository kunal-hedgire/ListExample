import threading
import time
import logging
'''
#2018-10-04 10:27:22.094 DEBUG PythonThreading2 - consumer: Consumer thread started ...

#logging.

logging.basicConfig(
    filename='HISTORYlistener.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S%B")

#logging.getLogger().setLevel(20)

def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
        logging.info('Consumer waiting ...')
        cv.wait()
        logging.debug('Consumer consumed the resource')

def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.info('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()
'''

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)

def consume(cv):
    logging.debug('consume started:')

    with cv:
        logging.debug('Waiting for resource:')
        cv.wait()
        logging.debug('consumer consume the resource')

def produce(cv):
    logging.debug('producing resources')
    with cv:
        logging.debug('making resource available')
        logging.debug('Notify to All consumer Thread')
        cv.notifyAll()


if __name__ == '__main__':
    condition = threading.Condition()
    c = threading.Thread(name='consume', target=consume, args=(condition,))
    p = threading.Thread(name='produce', target=produce, args=(condition,))

    c.start()
    time.sleep(2)

    p.start()

