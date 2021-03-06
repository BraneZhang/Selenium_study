#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing
import time, os


# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)


# output worker
def outputQ(queue, lock):
    info = queue.get()
    lock.acquire()
    print(str(os.getpid()) + '(get):' + info)
    lock.release()


# Main
record1 = []  # store input processes
record2 = []  # store output processes

lock = multiprocessing.Lock()  # 加锁，为防止散乱的打印
queue = multiprocessing.Queue(3)

# input processes
for i in range(10):
    process = multiprocessing.Process(target=inputQ, args=(queue,))
    process.start()
    record1.append(process)

# output processes
for i in range(10):
    process = multiprocessing.Process(target=outputQ, args=(queue, lock))
    process.start()
    record2.append(process)

for p in record1:
    p.join()

queue.close()  # 没有更多的对象进来，关闭 queue

for p in record2:
    p.join()
