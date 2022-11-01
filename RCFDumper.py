#!/usr/bin/env python3
import requests
from pprint import pprint as pp
import os
from urllib.parse import unquote

from os import sys
if len(sys.argv) < 2:
    print("need argument")
    print("example: ")
    print("RCTFDumper.py '{}'".format('https://wreckctf.com/login?token=ABCDEF))
    exit(0)

param = sys.argv[1]


domain = param.split("://")[1].split("/")[0]
method = param.split("://")[0]
url = method + "://" + domain 



firsttoken = param.split("token=")[1]
# auth token
firsttoken = unquote(firsttoken)

session = requests.session()
burp0_url = "{}/api/v1/auth/login".format(url)
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "{}".format(url), "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": "Bearer null", "Referer": param, "Te": "trailers"}
burp0_json={"teamToken": firsttoken}
r = session.post(burp0_url, headers=burp0_headers, json=burp0_json)
data = r.json()
pp(data)
token = data['data']['authToken']

# access soal

session = requests.session()

burp0_url = "{}/api/v1/challs".format(url)
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "{}/challs".format(url), "Authorization": "Bearer {}".format(token), "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
r = session.get(burp0_url, headers=burp0_headers)
datas = r.json()
template = """\
title: {}
value: {}
description: {}"""


for data in datas['data']:
    filepath = "{}/{}/{}".format(domain, data['category'], data['name'])
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    
    readme = "{}/{}".format(filepath, "README.md")

    readme_value = template.format(data['name'], data['points'], data['description'])
    with open(os.path.join(filepath, 'README.md'), 'w+') as f:
        f.write(str(readme_value))

    for file in data['files']:
        res = session.get(url + file['url'], headers=burp0_headers, stream=True)
        filename = file['name']
        print("[+] Downloading {}".format(os.path.join(filepath, filename)))
        print(url + file['url'])
        with open(os.path.join(filepath, filename), 'wb+') as f:
            f.write(res.content)
