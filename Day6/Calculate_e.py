import threading
import multiprocessing
from queue import Queue
import time
from decimal import Decimal, getcontext
from math import factorial


def e_serie_part(start, end, que=None):
    getcontext().prec = 100  # Set precision for Decimal calculations
    partial_sum = Decimal(0)
    
    for n in range(start, end):
        partial_sum += Decimal(1) / Decimal(factorial(n))
    
    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum


qres = Queue()

N = 100  # Number of terms to calculate in total
threads_count = 8  # Number of threads to use

# Calculate chunk size
chunk_size = N // threads_count

num_cores = multiprocessing.cpu_count()
print(f"Number of cores: {num_cores}")

start_time = time.time()

# Launch threads
thread_list = []
for i in range(threads_count):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < threads_count - 1 else N
    t = threading.Thread(target=e_serie_part, args=(start, end, qres))
    thread_list.append(t)
    t.start()

# Wait for all threads to finish
for t in thread_list:
    t.join()

end_time = time.time()

print(f"Threads finished. Elapsed time: {end_time - start_time:.2f} seconds. {qres.qsize()} elements in queue.")

# Aggregate results from the queue
e_approx = Decimal(0)
while not qres.empty():
    e_approx += qres.get()

print(f"Approximation of e: {e_approx}")
