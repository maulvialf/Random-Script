from subprocess import check_output
import string
import random
import os
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def parserjs(jscode):
    # make sure create random folder (wanna use /tmp/random, but this script sometimes run on my windows. zzz)
    tmpfile = "random/alfanrandom"+get_random_string(10)
    file = open(tmpfile, "w")
    file.write(jscode)
    file.close()
    print(len(jscode))
    out = check_output("node {}".format(tmpfile)).strip()
    print(out)
    os.remove(tmpfile)
    return out
