#!/usr/bin/python3

import threading, time


finish = threading.Event()
stop = threading.Event()
task_list = threading.Lock()


# Список потоков, ожидающих выполнения.
th_list = []

class Rtask():

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
                # Выполняем работу ...
                print("Running :", self.name, " at ", int(time.time()))
                self.time = time.time() + self.timeout

                # Вернули поток в список ожидания.
                task_list.acquire()
                th_list.append(self)
                task_list.release()

                # Сигнао об окончании работы потока.
                stop.set()

        def join(self):
                if(self.thread != None):
                        self.thread.join()



th_list.extend([
        Rtask("thread 1    ", 10),
        Rtask("  thread 2  ", 1),
        Rtask("    thread 3", 2),
        Rtask(" thread 4   ", 5)
])


#class WThread(threading.Thread):
#
#        def __init__(self):
#                self.result = 0
#                super().__init__(None, None, None, [])
#
#        def run(self):
#
#                global th_list, stop, task_list, finish
#
#                while(True):
#                        if(finish.isSet()):
#                                break
#                        ctime = time.time()
#                        task_list.acquire()
#                        next_time = None
#                        new_list = []
#                        for task in th_list:
#                                if(task.time <= ctime):
#                                        task.start()
#                                else:
#                                        new_list.append(task)
#                                        if(next_time==None or next_time>task.time):
#                                                next_time=task.time
#                        th_list=new_list
#                        task_list.release()
#                        if(next_time==None):
#                                stop.wait()
#                        else:
#                                stop.wait(next_time-ctime)
#
#                        stop.clear()
#
#
#
#w=WThread()
#w.start()
#
#time.sleep(60)
#finish.set()
#
#w.join()
#for task in th_list:
#	task.join()


while(True):

        ctime = time.time()

        # блокируем список задач для запуска.
        task_list.acquire()
        next_time = None
        new_list = []

        for task in th_list:
                # Пришло время запуска
                if(task.time <= ctime):
                        task.start()
                # Ещё не время - выясняем сколько осталось.
                else:
                        new_list.append(task)
                        if(next_time == None or next_time > task.time):
                                next_time = task.time

        # Новый список задач.
        th_list = new_list
        task_list.release()

        # Ждём, когда закончит работу какой либо поток или
        # подойдёт время запуска потока.
        if(next_time == None):
                stop.wait()
        else:
                stop.wait(next_time-ctime)
        stop.clear()
