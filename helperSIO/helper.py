import requests
import json
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

##########################################
# httpErrorCheck
# Checks for 200 status_code
# Exits and reports error if 200 not found
# Requires ScaleIO Object and http response
# from ScaleIO API Endpoint
###########################################
def httpErrorCheck (sio, res):
    if  res.status_code != 200:
        sio.alfred.error("The process exited with a {} status".format(res.status_code))
        sio.alfred.error("The error message states: {}".format(res.content))
        exit(1)

def doGet(sio, append_url):
    res = sio._session.get(sio.server + append_url)
    httpErrorCheck(sio, res)
    return res

def doPost(sio, append_url, payload=None):
    res = sio._session.post(sio.server + append_url, json=payload)
    httpErrorCheck(sio, res)
    return res

