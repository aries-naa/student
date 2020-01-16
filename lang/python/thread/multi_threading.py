import threading
import time


def thread_function(name, start_time, process_time):
    time.sleep(start_time)
    print(f"{name} started")
    time.sleep(process_time)
    print(f"{name} finished")
    return


def thread_generating():
    while True:
        print("Waiting...")
        thread_1 = threading.Thread(target=thread_function, args=('thread_1', 15, 1))
        thread_2 = threading.Thread(target=thread_function, args=('thread_2', 1, 0))
        thread_3 = threading.Thread(target=thread_function, args=('thread_3', 1, 0))
        thread_4 = threading.Thread(target=thread_function, args=('thread_4', 1, 0))
        thread_list = [thread_1, thread_2, thread_3, thread_4]
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        print("******Finished!******")


thread_generating()


