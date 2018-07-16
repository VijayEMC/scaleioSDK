from helperSIO.helper import *

#####################
## GET ALL VOLUMES ##
#####################
# Description: Returns all volumes associated with SIO Gateway
# Preconds: ScaleIO object containing authentication mechanism
# See client_init.py for more info on ScaleIO object
# PostConds: Returns a list of volumes or fails due to improper
# http response from Http request. Exit logging sent to stdout with logger
def getVolumes(sio):
    res = doGet(sio, "/api/types/Volume/instances")
    return json.loads(res.content)

########################
## GET VOLUME WITH ID ##
########################
# Description: Returns volume with specific ID
# Preconds: ScaleIO object containing authentication mechanism
#           VolumeID - string
# See client_init.py for more info on ScaleIO object
# PostConds: Returns the requested volume or fails due to improper
# http response from Http request. Exit logging sent to stdout with logger
def getSpecificVolume(sio, id):
    res = doGet(sio, "/api/instances/Volume::" + id)
    return json.loads(res.content)

########################################
## GET STATISTICS FOR SPECIFIC VOLUME ##
########################################
# Description: Returns statistics for specified volume
# Preconds: ScaleIO object containing authentication mechanism
#           Volume ID - string
# See client_init.py for more info on ScaleIO object
# PostConds: Returns a statistics object or fails due to improper
# http response from Http request. Exit logging sent to stdout with logger
def getStatisticsOfVolume(sio, id):
    res = doGet(sio, "/api/instances/Volume::" + id + "/relationships/Statistics")
    return json.loads(res.content)

###################
## REMOVE VOLUME ##
###################
# Description: Removes specified volume. Can remove decendants if requested
# Preconds: ScaleIO object containing authentication mechanism
#           Volume payload: Object containing "id" property ("id" : <id string>) and "removeMode" property
#           which must be set to "ONLY_ME" "INCLUDING_DESCENDANTS" "DESCENDANTS_ONLY" or
#           "WHOLE_VTREE" ("removeMode" : "ONLY_ME") Defaults to "ONLY_ME"
# See client_init.py for more info on ScaleIO object
# PostConds: Removes Volume or fails due to improper
# http response from Http request. Exit logging sent to stdout with logger
def removeVolume(sio, volumeId, removeMode="ONLY_ME"):
    volumeDetail = getSpecificVolume(sio, volumeId)
    if volumeDetail["mappedSdcInfo"] == None:
        res =  doPost(sio, "/api/instances/Volume::" + volumeId + "/action/removeVolume", {"removeMode": removeMode})
        print ("Removing Volume with id: {}".format(volumeId))
        return (res.content)
    else:
        sdcInfo = volumeDetail["mappedSdcInfo"]
        sdcs = []
        for i in sdcInfo:
            sdcs.append(i["sdcId"])
        for i in sdcs:
            res = unmapVolume(sio, volumeId, i)
            print("Unmapping Volume from Sdc ID: {}".format(i))
        res = doPost(sio, "/api/instances/Volume::" + volumeId + "/action/removeVolume", {"removeMode": removeMode})
        return res.content

############################
## ADD CAPACITY TO VOLUME ##
############################
# Description: Removes specified volume. Can remove decendants if requested
# Preconds: ScaleIO object containing authentication mechanism
#           Volume payload: Object containing "id" property ("id" : <id string>) and "sizeInGB" property
#           which must be in multiples of 8 GB
# See client_init.py for more info on ScaleIO object
# PostConds: Adds Capacity to Volume or fails due to improper
# http response from Http request. Exit logging sent to stdout with logger
def addCapacityVolume (sio, volumeId, sizeIncrease):
    payload = {"sizeInGB": sizeIncrease}
    if int(sizeIncrease)%8 != 0:
        print ("Please enter a size increase divisible by 8")
        return None
    res = doPost(sio, "/api/instances/Volume::" + str(volumeId) + "/action/setVolumeSize", payload)
    return res

###################
## CREATE VOLUME ##
###################
# Description: Creates Volume in a specified Storage Pool
# Preconds: ScaleIO object containing authentication mechanism
#           1st Arg: Volume Name  : string
#           2nd Arg: Volume Size in MB : string
#           3rd Arg: Volume Type : string : "ThinProvisioned" (default), "ThickProvisioned", "Snapshot"
#               Assign param by - volType="ThinProvisioned" -- omit this param if Thin provisioning
#           4th Arg: Storage Pool Id : string :
#               Assign param by - storagePoolId=<string>
# See client_init.py for more info on ScaleIO object
# PostConds: Creates volume in specified storage pool
# http response from Http request. Exit logging sent to stdout with logger
# Returns: New Volume Id  as string

def createVolume (sio, volName, volSizeInMb, storagePoolId, volType="ThinProvisioned", sdcID=None):
    createVolumePayload = {"storagePoolId": storagePoolId, "volumeSizeInKb": str(int(volSizeInMb) * 1024),
                            "name": volName, "volumeType": volType}
    res = doPost(sio, "/api/types/Volume/instances", payload=createVolumePayload)
    volume = json.loads(res.content)
    if sdcID!=None:
        res = mapVolume(sio, volume["id"], sdcId=sdcID)
        print("Created Volume with ID: {}. Volume mapped to SDC: {}".format(volume["id"], sdcID))
    return volume["id"]

###################
## MAP VOLUME ##
###################
# Description: Maps Volume to SDC
# Preconds: 1st Arg: ScaleIO object containing authentication mechanism
#           2nd Arg: Volume ID  : string
#           3rd Arg: SDC Id : string
#           4th Arg (optional- Defaults to TRUE): Boolean - defines whether or not Volume can be mapped to multiple SDCs
# See client_init.py for more info on ScaleIO object
# PostConds: Maps volume to specified SDC
# http response from Http request. Exit logging sent to stdout with logger
# Returns: New Volume Id  as string

def mapVolume(sio, volId, sdcId=None, allowMultipleMappings="TRUE"):
    url = "/api/instances/Volume::{}/action/addMappedSdc".format(volId)
    if sdcId==None:
        print("please include sdcId in arguments as <sdcId=alphanumstring>")
        return None
    mapVolumePayload = {"sdcId" : sdcId, "allowMultipleMappings": allowMultipleMappings}
    res = doPost(sio, url, payload=mapVolumePayload)
    print("mapVolume function completed with status {}".format(res.status_code))
    return res

###################
## UNMAP VOLUME ##
###################
# Description: UnMaps Volume from SDC
# Preconds: 1st Arg: ScaleIO object containing authentication mechanism
#           2nd Arg: Volume ID  : string
#           3rd Arg: SDC Id : string
#           4th Arg (optional- Defaults to TRUE): Boolean - defines whether or not Volume can be mapped to multiple SDCs
# See client_init.py for more info on ScaleIO object
# PostConds: Maps volume to specified SDC
# http response from Http request. Exit logging sent to stdout with logger
# Returns: New Volume Id  as string

def unmapVolume(sio, volId, sdcId=None, ignoreScsiInitiators="TRUE"):
    if sdcId==None:
        print("please include sdcId in arguments as <sdcId=alphanumstring>")
        return
    url = "/api/instances/Volume::{}/action/removeMappedSdc".format(volId)
    unmapVolumePayload = {"sdcId": sdcId, "ignoreScsiInitiators": ignoreScsiInitiators}
    res = doPost(sio, url, payload=unmapVolumePayload)
    print("unmapVolume function completed with status {}".format(res.status_code))
    return res

########################
## ERASE TEST VOLUMES ##
#########################
# Description: Erases all volumes prepended with 'test' --- CAREFUL!!!!
# Preconds: 1st Arg: ScaleIO object containing authentication mechanism
# See client_init.py for more info on ScaleIO object
# PostConds: Maps volume to specified SDC
# http response from Http request. Exit logging sent to stdout with logger
# Returns: New Volume Id  as string
def eraseAllTestVolumes(sio):
    res = getVolumes(sio)
    for i in res:
        if i["name"].startswith('test'):
            removeVolume(sio, i["id"])
            print ("Removed volume with id: {} and name {}".format(i["id"], i["name"]))


########################
## VOLUME ID BY NAME ##
#########################
# Description: Returns Volume ID based on Volume Name
# Preconds: 1st Arg: ScaleIO object containing authentication mechanism
#           2nd Arg: Name of Volume - String
# See client_init.py for more info on ScaleIO object
# PostConds: Maps volume to specified SDC
# http response from Http request. Exit logging sent to stdout with logger
# Returns: New Volume Id  as string

def volumeIdByName(sio, name):
    vols = getVolumes(sio)
    for vol in vols:
        if vol["name"]== name:
            return vol["id"]
    print("Volume with name '{}' not found".format(name))
    return None


