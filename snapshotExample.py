
from helperSIO.management import *
from volume import *
from snapshots import *
from system import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



# Connect to ScaleIO Gateway
sio = sioClient()

systemId = systemInstanceIdByName(sio, "plsio")

# get all volume Ids
vols = getAllVolumeIds(sio)

snapGroup = snapVolumes(sio, vols, systemId)
print(json.dumps(snapGroup))


res = removeConsistencyGroup(sio, snapGroup["snapshotGroupId"], systemId)
print(res)


# logout
logOut(sio)

