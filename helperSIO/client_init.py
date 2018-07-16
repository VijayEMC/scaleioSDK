## client_init.py
## This file creates a client object will all necessary variables and objects needed
## to function and communicate with the ScaleIO Gateway
## The object created here should be used in all communications with SIO gateway

import requests
from requests.auth import HTTPBasicAuth
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging
import json
import os.path


class ScaleIOClient():

    def __init__(self):
        logging.basicConfig()
        self.alfred = logging.getLogger("ScaleIO SDK")
        if os.path.isfile('settings.json'):
            with open("settings.json") as json_file:
                config = json.load(json_file)
                ip = config["ip"]
                port = config["port"]
                user = config["username"]
                password = config["password"]
        else:
            exit("Could not find Settings.Json file.")
            
        self.server = ip + ":" + port
        self._session = requests.Session()
        self.token = self._session.get(self.server + "/api/login", auth=HTTPBasicAuth(user, password), verify=False)
        if self.token != None:
            self.LOGGED_IN = True
        else:
            self.LOGGED_IN = False
        # Check for http Errors
        ####################################
        # Add authorization token to session
        #####################################
        self._session.auth = HTTPBasicAuth('', self.token.json())
        # add more object variables as necessary
        self._session.headers = {"Content-Type": "application/json"}

