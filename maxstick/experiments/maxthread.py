import os
import time
import threading

import MaxPlus
MaxPlus.Core.EvalMAXScript("print \"active!\"")


class MaxInteractionThread(threading.Thread):

    def __init__(self):
        super(MaxInteractionThread, self).__init__()
        self.counter = 0
        self.maximum = 10
        self.alive = True

    def run(self):
        MaxPlus.Core.EvalMAXScript("print \"" + str(self.alive) + "\"")
        while self.alive:
            time.sleep(0.25)

            pth = os.path.join(r"C:\Users\Public\Desktop\temp", str(time.time()))
            print pth
            with open(pth, "w") as f:
                f.write("")

            # mxs = "print localtime"
            # MaxPlus.Core.EvalMAXScript(mxs)

            self.counter += 1
            if self.counter >= self.maximum:
                self.alive = False
        print("Thread is dying.")


thread = MaxInteractionThread()
thread.start()
# thread.join()


"""

python.executeFile @"C:\Users\Buelter\Google Drive\dev\maxstick\maxstick\maxthread.py"

"""