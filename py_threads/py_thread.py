from threading import Thread


class thread(Thread):
    def __init__(self, thread_ID):
        Thread.__init__(self)
        self.thread_ID = thread_ID

    def run(self):
        print(f"ThreadID = {self.thread_ID}")


thread1 = thread(100)
thread2 = thread(101)
thread3 = thread(102)


