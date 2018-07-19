from helperSIO.helper import *
import datetime


########################
## SNAP VOLUMES ##
########################
# Description: Snaps volumes 
# Preconds: 1st Arg: ScaleIO object containing authentication mechanism
#           2nd Arg: VolumeIdList - an array of strings representing volume Ids. Any Volume Id included in array will be snapped
#           3rd Arg: SystemId - string
# See client_init.py for more info on ScaleIO object
# PostConds: Returns an Object with the "snapshotGroupId" and a list of new logical Volume Ids. Name of new volumes are dynamically generated based on VolumeID and # date and time.
# http response from Http request. Exit logging sent to stdout with logger
def snapVolumes(sio, volumeIdList, systemId):
    payload = {"snapshotDefs":[]}
    for volumeId in volumeIdList:
        snapObject = {"volumeId" : volumeId, "snapshotName" : "{}_{:%Y%m%d_%H:%M}".format(volumeId, datetime.datetime.now())}
        payload["snapshotDefs"].append(snapObject)     
    res =  doPost(sio, "/api/instances/System::{}/action/snapshotVolumes".format(systemId), payload)
    return json.loads(res.content)

##############################
## REMOVE CONSISTENCY GROUP ##
##############################
# Description: Snaps volumes 
# Preconds: 1st Arg: ScaleIO object containing authentication mechanism
#           2nd Arg: ConsistencyGroupId - a string representing the Consistency Group ID, or "snapshotGroupId" returned from snapVolumes() function.
#           3rd Arg: SystemId - string
# See client_init.py for more info on ScaleIO object
# PostConds: Returns an Object showing the number of volumes removed.
# http response from Http request. Exit logging sent to stdout with logger
def removeConsistencyGroup(sio, consistencyGroupId, systemId):
    payload = {"snapGroupId": consistencyGroupId}
    res =  doPost(sio, "/api/instances/System::{}/action/removeConsistencyGroupSnapshots".format(systemId), payload)
    return res.content

