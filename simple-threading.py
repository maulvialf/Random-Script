#!/usr/bin/env python3

import sys
from threading import Thread
from queue import Queue
from subprocess import check_output
passwords = Queue()

# generate list
for i in range(0, 100):
    passwords.put(i)

def worker(y):
    # make sure all thread work until all generated list enqueed
    while not passwords.empty():
        password = passwords.get()
        # execute command. just example
        pload = check_output(["gdb", "--batch", "-ex", "py arg0={};".format(password), "-x", "template.py"]).decode('utf8')
        
        # success behaviour
        if("success" in pload):
            print(pload)
            with passwords.mutex:
                passwords.queue.clear()
            return
        # fail beheaviour, print trial
        else:
            print(password, "failed")
            continue
    pass

threads = []
# threads 32
for i in range(1, 32):
    thread = Thread(target=worker, args=(i, ), daemon=True)
    thread.start()
    threads.append(thread)

# wait all thread to completed
for thread in threads:
    thread.join()