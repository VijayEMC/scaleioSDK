from helperSIO.helper import *
from helperSIO import client_init


# Create SIO client object
def sioClient():
    return client_init.ScaleIOClient()

def logOut(sio):
    return doGet(sio, "/api/logout")

# Get all Storage Pools
def getStoragePools(sio):
    res = doGet(sio, "/api/types/StoragePool/instances")
    return json.loads(res.content)



def storagePoolIdByName(sio, name):
    storagePools = getStoragePools(sio)
    for storagePool in storagePools:
        if storagePool["name"] == name:
            return storagePool["id"]
    print("Storage Pool with name '{}' Not Found". format(name))
    return None

