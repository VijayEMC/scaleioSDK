## ScaleIO SDK - Python

###### UPDATED FEATURES - 7/16/18:
Volume creation, mapping, unmapping, expansion and deletion.

*************************************************************

This repository features the beginnings of a ScaleIO SDK in python. I plan to build on it over time and update as frequently as possible. You'll see several unpopulated files serving as placeholders for features soon to come. Each feature set will be categorized below. To understand how to utilize a certain feature set, simply read through the category and test using the examples shown.

*************************************************************
###### Installation:

To use this library, simply clone the repo into your working directory.

Required Libraries Include:  
JSON  
Requests  
urllib3  


*************************************************************

###### Use:

This library uses a config file to connect to the ScaleIO Gateaway. After cloning, you'll notice a file named 'settings.json.example' in the directory. Update this file with the appropriate credentials (ip, port, username, password) and remove '.example' from the file name. The application's initialization will automatically connect to your gateway.

When writing your own python app using this library, you'll want to import much of the functionality from the helperSIO folder. To do so, simply add these lines to your file:

from helperSIO.management import *
from helperSIO.helper import *



*************************************************************

###### Volumes:

**Things you can do:**  
    - Get a list of all Volumes  
    - Get a specific volume object using the volume ID  
    - Get the statistics of a specific volume  
    - Delete/Remove a Volume  
    - Add Capacity to a Volume  
    - Create a Volume  
    - Map a Volume to an SDC  
    - UnMap a Volume from an SDC  
    - Erase All Test Voluems -- ** CAREFUL **  
    - Get a Volume ID using the Volume Name  
  
**Example: Please see volumeExample.py for some easy use cases.**

*************************************************************

###### Snapshots:
Coming Soon.

*************************************************************


###### Protection Domains:
Coming Soon.


*************************************************************


###### Quality of Service:
Coming Soon.

*************************************************************


###### MDM:
Coming Soon.

*************************************************************


###### SDC:
Coming Soon.


*************************************************************


###### SDS:
Coming Soon.

*************************************************************


###### And More.... (hopefully soon :)


