import os
from pprint import pprint as pp
import shutil
from PIL import Image
import pytesseract as pyt

from threading import Thread
from queue import Queue
from subprocess import check_output

listfiles = os.listdir('EXP')

def identified(filename):
    text = pyt.image_to_string(filename)
    if('Host' in text or 'Accept' in text or 'POST /' in text or 'GET /' in text or 'Agent ' in text or '/json ' in text):
        return True
    else:
        return False

try:
    os.mkdir("BURP")
    os.mkdir("NONBURP")
except:
    pass

passwords = Queue()
for filename in listfiles:
    passwords.put(filename)


def worker(filename):
    while not passwords.empty():
        filename = passwords.get()
        if(identified('EXP/'+filename) == True):
            shutil.copyfile('EXP/'+filename, 'BURP/'+filename)
            print(passwords.qsize(), filename, ' ', 'BURP')
        else:
            shutil.copyfile('EXP/'+filename, 'NONBURP/'+filename)
            print(passwords.qsize(), filename, ' ', 'Non BURP')


threads = []
# threads 32
for i in range(1, 32):
    thread = Thread(target=worker, args=(i, ), daemon=True)
    thread.start()
    threads.append(thread)

# wait all thread to completed
for thread in threads:
    thread.join()
