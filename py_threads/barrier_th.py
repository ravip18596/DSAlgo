import sys
from threading import Thread
from threading import Barrier, BrokenBarrierError


# target function to prepare some work
def task(barrier, number, value):
    print(f'Thread {number} done, got: {value}')
    try:
        barrier.wait()
    except BrokenBarrierError:
        pass


# create a barrier
barrier = Barrier(5)
# create the worker threads
for i in range(5):
    # start a new thread to perform some work
    worker = Thread(target=task, args=(barrier, i, i*i))
    worker.start()



try:
    barrier.wait()
    print('All threads have their result')
except Exception as e:
    print(f'Exception: {str(e)}')

print("doing next")
sys.exit(0)
