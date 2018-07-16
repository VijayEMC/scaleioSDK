# file to run program

from helperSIO.management import *
from volume import *
from protectionDomain import *
from sdc import *
from system import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Connect to ScaleIO Gateway
sio = sioClient()

# erase all test volumes
res = eraseAllTestVolumes(sio)

# get all volumes
vols = getVolumes(sio)

# grab a volumeID by name
volumeId = volumeIdByName(sio, "kafka_kfkdata")

# get specific volume object
specVol = getSpecificVolume(sio, volumeId)

# get statistics of specific volume
statVol = getStatisticsOfVolume(sio, volumeId)

# get storage pool ID using name
storagePoolId = storagePoolIdByName(sio, "SP1")

# create variables to deploy a test volume
# PREPEND YOUR VOLUME NAME WITH 'test' IF YOU'D LIKE TO AUTO DESTROY THE VOLUME USING
# eraseAllTestVolumes()
volName = "testVolume3"
volSizeInMb = "10"

# create test volume
newVol = createVolume(sio, volName, volSizeInMb, storagePoolId=storagePoolId)

print("Created new volume with id: {}".format(newVol))

# grab SDC Id by name of SDC
sdcId = sdcIdByName(sio, "ESX-10.4.44.106")

# map volume to SDC
res = mapVolume(sio, newVol, sdcId=sdcId)

# get statistics of new volume
specVol = getSpecificVolume(sio, newVol)

print("Size of Volume before adding capacity is: {} Kbs".format(specVol["sizeInKb"]))

# create varaiable for lun expansion -- NOTE: value must be divisible by 8
volumeExpansion = "136"

# add capacity to lun
addCap = addCapacityVolume(sio, newVol, volumeExpansion)

# get updated statistics of lun
specVol = getSpecificVolume(sio, newVol)
print("Size of Volume after adding capacity is: {} Kbs".format(specVol["sizeInKb"]))

# unmap volume from sdc
res = unmapVolume(sio, newVol, sdcId=sdcId)

# erase all test volumes created
res = eraseAllTestVolumes(sio)

# logout
logOut(sio)

