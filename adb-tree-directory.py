#!/usr/bin/env python3
import datetime
from adb_shell.adb_device import AdbDeviceTcp
from pprint import pprint as pp
import time as time
import signal


device = AdbDeviceTcp("adbaby.sstf.site", 6666, default_transport_timeout_s=10)
device.connect()
#Close session
def handler(signum, frame):
    print(1)
    raise Exception('Action took too much time')


signal.signal(signal.SIGALRM, handler)
signal.alarm(3) #Set the parameter to the amount of seconds you want to wait


def explore(path):
	fs = device.list(path)
	output = fs
	if output:
		headers = ('Name', 'Mode', 'Size', 'Modification Time')
		# param  =  oct(output[0][1])
		# pp(param)

		signal.signal(signal.SIGALRM, handler)
		signal.alarm(3) #Set the parameter to the amount of seconds you want to wait
		try:


			data = list()
		except:
			return 0
		signal.alarm(3) #Resets the alarm to 10 new seconds
		signal.alarm(0) #Disables the alarm 
		for entry in sorted(output):
			# timestamp = datetime.datetime.fromtimestamp(entry[3])
			timestamp = entry[3]
			data.append((entry[0].decode(), oct(entry[1])[2:], str(entry[2]), timestamp))
		# pp(data)
		# print_table(f"Directory fs", headers, *data)
		return data
	else:
		return 0

# pp(explore("."))
kotak = []
sudah = []
data = explore("/dev")
for i in data:
	if(i[0] == "." or i[0] == ".."):
		continue
	kotak.append(i[0])

sudah.append(".")
while True:
	if(kotak == []):
		break
	cari = kotak.pop()
	print (cari)
	data = explore(cari)
	if(data == 0):
		continue
	for i in data:
		if(i[0] == "." or i[0] == ".."):
			continue
		kotak.append(cari+"/"+i[0])
