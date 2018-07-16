from helperSIO.helper import *


def getSystemInstances(sio):
    res = doGet(sio, "/api/types/System/instances")
    return json.loads(res.content)