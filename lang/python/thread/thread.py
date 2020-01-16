#!/usr/bin/python3

import threading, time


finish = threading.Event()
stop = threading.Event()
task_list = threading.Lock()


class Rtask:

        def __init__(self, name, timeout):
                self.result = 0
                self.name = name
                self.timeout = timeout
                self.time = time.time()
                self.thread = None

        def start(self):
                self.thread = threading.Thread(None, self.run, None, [])
                self.thread.start()

        def run(self):
                print("Running :", self.name,)
                self.time = time.time() + self.timeout

                global th_list, stop, task_list
                task_list.acquire()
                th_list.append(self)
                stop.set()
                task_list.release()

        def join(self):
                if(self.thread != None):
                        self.thread.join()

        def isAlive(self):
                if(self.thread != None):
                        return self.thread.isAlive()
                return 0


th_list=[Rtask("thread 1", 10), Rtask("  thread 2", 1), Rtask("    thread 3", 2), Rtask(" thread 4", 5)]


class WThread(threading.Thread):

        def __init__(self):
                self.result = 0
                super().__init__(None, None, None, [])

        def run(self):

                global th_list, stop, task_list, finish

                while(True):
                        if(finish.isSet()):
                                break
                        ctime = time.time()
                        task_list.acquire()
                        next_time = None
                        new_list = []
                        for task in th_list:
                                if(task.time <= ctime):
                                        task.start()
                                else:
                                        new_list.append(task)
                                        if(next_time==None or next_time>task.time):
                                                next_time=task.time
                        th_list=new_list
                        task_list.release()
                        if(next_time==None):
                                stop.wait()
                        else:
                                stop.wait(next_time-ctime)

                        stop.clear()



w=WThread()
w.start()

time.sleep(60)
finish.set()

w.join()
for task in th_list:
	task.join()


