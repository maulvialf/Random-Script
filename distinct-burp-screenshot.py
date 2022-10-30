"""
split burp screenshot from other png images
"""
import os
from pprint import pprint as pp
import shutil
from PIL import Image
import pytesseract as pyt

listfiles = os.listdir('EXP')

def identified(filename):
    text = pyt.image_to_string(filename)
    if('Host' in text or 'Accept' in text or 'POST /' in text or 'GET /' in text or 'Agent ' in text or '/json ' in text):
        return True
    else:
        return False

i = 0
for filename in listfiles:
    if(identified('EXP/'+filename) == True):
        shutil.copyfile('EXP/'+filename, 'BURP/'+filename)
        print(i, filename, ' ', 'BURP')
    else:
        shutil.copyfile('EXP/'+filename, 'NONBURP/'+filename)
        print(i, filename, ' ', 'Non BURP')
    i += 1