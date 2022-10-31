from pprint import pprint as pp
import sys
from threading import Thread
from queue import Queue
import os 
import requests

session = requests.session()
ROOT = "asis2022"
MAINURL = "https://asisctf.com:443"
USERNAME = "blabla@gmail.com"
PASSWORD = "blabla"
THREAD_COUNT = 6
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}

def login(session, username, password):
    s = session.get(MAINURL, headers=burp0_headers)
    resp = session.get(f"{MAINURL}/login", headers=burp0_headers).text
    csrftoken = resp.split('name="csrf-token" content="')[1].split('"')[0]
    burp0_data = {"_token": csrftoken, "email": username, "password": password}
    resp = session.post(f"{MAINURL}/login", headers=burp0_headers, data=burp0_data)

def generate_tags(blob):
    tags = ""
    for i in range(len(blob)):
        tags += blob[i]['name'] + "_"
    return tags

def parsing(desc):
    links = []
    hrefs = desc.split('href="/tasks')
    for i in hrefs[1:]:
        link = "/tasks"+i.split('"')[0]
        links.append(link)

    return links


def worker(y):
    while not files.empty():
        try:
            file = files.get()
            urls      = file[1]
            filepath = file[0]
            filename = file[1].split("/")[2]
            print(filename)
            print(f"Downloading ")
            res = session.get(f"{MAINURL}/{urls}", headers=burp0_headers, stream=True)
            with open( f"{filepath}/{filename}", 'wb+') as f:
                f.write(res.content)

            with passwords.mutex:
                passwords.queue.clear()
            return
        except:
            pass

login(session, USERNAME, PASSWORD)
resp = session.get(f"{MAINURL}/challenges/list", headers=burp0_headers)
challs = resp.json()
files = Queue()

for chall in challs:
    challname = chall['name']
    point  = chall['dynamic_points']
    tags = generate_tags(chall['categories'])
    description = chall['description']
    foldername = f"{ROOT}/{tags}{challname}"
    links = parsing(description)
    for link in links:
        files.put((foldername,link))

    readme = f"""\
title: {challname}
tags: {tags}
value: {point}
description: {description}"""
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    with open(os.path.join(foldername, 'README.md'), 'w+') as f:
        f.write(str(readme))

threads = []

for i in range(1, THREAD_COUNT):
    thread = Thread(target=worker, args=(i,), daemon=True)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Download Complete")