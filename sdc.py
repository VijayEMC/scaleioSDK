from helperSIO.helper import *

# Get all SDCs
def getSDCs(sio):
    res =doGet(sio, "/api/types/Sdc/instances")
    return json.loads(res.content)

def sdcIdByName(sio, name):
    sdcs = getSDCs(sio)
    for sdc in sdcs:
        if sdc["name"] == name:
            return sdc["id"]
    print("SDC with name '{}' Not Found".format(name))
    return None
