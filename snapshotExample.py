
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

# take a shapshot of all volumes
snapGroup = snapVolumes(sio, vols, systemId)
print(json.dumps(snapGroup))

# remove all snapshot volumes created from snapVolumes() 
res = removeConsistencyGroup(sio, snapGroup["snapshotGroupId"], systemId)
print(res)


# logout
logOut(sio)

