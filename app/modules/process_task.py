import multiprocessing
from multiprocessing import Process, Pool, Queue
import time
print(multiprocessing.cpu_count(), ' cores .')


def worker(start: int, end: int, q: Queue): 
    total = 0
    for i in range(start, end + 1):
        total += i
    q.put(total)


def calculator() -> int:
    q = Queue()
    processes = []
    for i in range(10):
        start = i * 100 + 1
        end = (i + 1) * 100
        p = Process(target=worker, args=(start, end, q))
        p.start()
        processes.append(p)

    total = 0
    for _ in range(10):
        total += q.get()

    for p in processes:
        p.join()

    print("=====================Total:",  total)
    return total
