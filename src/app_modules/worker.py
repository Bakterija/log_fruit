from kivy.event import EventDispatcher
from kivy.logger import Logger
from threading import Thread
from time import time, sleep
import subprocess
try:
    from queue import Queue, Empty
except:
    from Queue import Queue, Empty
    

class wlock():
    def __enter__(self):
        global worker
        worker.active = False
    def __exit__(self, type, value, traceback):
        worker.active = True


class Worker(EventDispatcher):
    active = False
    added_msg = 0
    queue = []

    def start(self, *args):
        self.active = True
        self._tr = Thread(target=self.logfruit_work)
        self._tr.daemon = True
        self._tr.start()

    def read_queue(self, *args):
        with wlock():
            nlist = list(self.queue)
            self.queue = []
            return nlist

    def logfruit_work(self):
        Logger.info('Worker: logfruit_work()')
        def execute(cmd):
            popen = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                stderr=subprocess.PIPE, universal_newlines=False)
            self.proc = popen
            for stdout_line in iter(popen.stdout.readline, ""):
                yield stdout_line
            popen.stdout.close()
            popen.stdin.close()
            return_code = popen.wait()
            if return_code:
                if return_code != -2:
                    raise subprocess.CalledProcessError(return_code, cmd)

        for text in execute(["adb", "logcat"]):
            while not self.active:
                sleep(0.01)
            try:
                text = text.decode('utf-8')
                self.queue.append(
                    {'time': time(), 'text': text, 'text0': text})
                self.added_msg += 1
            except:
                pass

    def stop(self):
        self.proc.send_signal(subprocess.signal.SIGINT)
        # self._tr.join()

worker = Worker()
