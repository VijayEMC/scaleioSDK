from helperSIO.helper import *

def getProtectionDomains(sio):
    res = doGet(sio, "/api/types/ProtectionDomain/instances")
    return json.loads(res.content)

def getProtectionDomainIds(protectionDomainArray):
    pdId = []
    for i in protectionDomainArray:
        pdId.append(i["id"])
    return pdId

