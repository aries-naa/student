#!/usr/bin/python3

import threading, time


# сигнал завершения работы потока.
stop = threading.Event()

# блокировка доступа к списку потоков.
task_list = threading.Lock()

# Список потоков, ожидающих выполнения.
th_list = []


class Rtask(threading.Thread):

        def __init__(self, name, timeout):
                super().__init__(None, self.run, None, [])
                self.name = name
                self.timeout = timeout
                self.time = time.time()


        def run(self):
                # Выполняем работу ...
                print("Running :", self.name, " at ", int(time.time()))
                self.time = time.time() + self.timeout

                # Вернули поток в список ожидания.
                task_list.acquire()
                next_task = Rtask(self.name, self.timeout)
                next_task.time = self.time
                th_list.append(next_task)
                task_list.release()

                # Сигнао об окончании работы потока.
                stop.set()


th_list.extend([
        Rtask("thread 1    ", 10),
        Rtask("  thread 2  ", 1),
        Rtask("    thread 3", 2),
        Rtask(" thread 4   ", 5)
])


try:
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

except KeyboardInterrupt:
        print("---")

print("!!!!!!!!!!!")
