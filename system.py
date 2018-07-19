from helperSIO.helper import *


def getSystemInstances(sio):
    res = doGet(sio, "/api/types/System/instances")
    return json.loads(res.content)


def systemInstanceIdByName(sio, name):
    res = getSystemInstances(sio)
    for systemInstance in res:
        if systemInstance["name"] == name:
            return systemInstance["id"]
    print("System Instance with name '{}' not found".format(name))
    return None

