#!/usr/bin/env python3

import requests
import json
import time

usernamepw = requests.auth.HTTPBasicAuth('admin', 'wifll')

url = 'http://192.168.123.35/cgi-bin/ptz.cgi?action=getStatus&channel=0'
urlStart ='http://192.168.123.35/cgi-bin/ptz.cgi?action=start&channel=0&code=Up&arg1=0&arg2=1&arg3=0'
urlStop ='http://192.168.123.35/cgi-bin/ptz.cgi?action=stop&channel=0&code=Up&arg1=0&arg2=1&arg3=0'

myResponse = requests.get(urlStart, auth=usernamepw)
print(myResponse.content)
time.sleep(0.1)
myResponse = requests.get(urlStop, auth=usernamepw)
print(myResponse.content)

# 
# if (myResponse.ok):
#     jData = myResponse.json()
#     print("The response contains {0} properties".format(len(jData)))
#     print("\n")
#     for key in jData:
#         print(key + " : " + jData[key])
# else:
#     myResponse.raise_for_status()
# 
