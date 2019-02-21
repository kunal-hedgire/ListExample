import threading


class PrintNumbers(threading.Thread):
    def __init__(self, start_number, end_number, step, set_event, clear_event):
        threading.Thread.__init__(self)
        self.start_number = start_number
        self.end_number = end_number
        self.step = step
        self.set_event = set_event
        self.clear_event = clear_event



    def run(self):
        for i in range(self.start_number, self.end_number, self.step):
            print("Active thread:", threading.current_thread().getName())
            print(i)
            self.set_event.set()
            self.clear_event.clear()
            self.clear_event.wait()
        self.set_event.set()

t = threading.Event()
tr1 = threading.Event()


#threading.current_thread()
t1 = PrintNumbers(0, 51, 2, t, tr1)
t2 = PrintNumbers(1, 50, 2, tr1, t)


t1.start()
t2.start()

t1.join()
t2.join()

