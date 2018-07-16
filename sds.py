from helperSIO import *


# Get all SDSs
def getSDSs(sio):
    return doGet(sio, "/api/types/Sds/instances")
