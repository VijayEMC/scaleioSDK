ScaleIO SDK - Python

UPDATED FEATURES - 7/16/18:
Volume creation, mapping, unmapping, expansion and deletion.

This repository features the beginnings of a ScaleIO SDK in python. I plan to build on it over time and update as frequently as possible. You'll see several unpopulated files serving as placeholders for features soon to come. Each feature set will be categorized below. To understand how to utilize a certain feature set, simply read through the category and test using the examples shown.


Installation:

To use this library, simply clone the repo into your working directory.

Required Libraries Include:
JSON
Requests
urllib3


Use:

This libarary uses a config file to connect to the ScaleIO Gateaway. After cloning, you'll notice a file named 'settings.json.example' in the directory. Update this file with the appropriate credentials and remove '.example' from the file name and the applications initialization will automatically connect to your gateway.


Volumes:

Things you can do:
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




Snapshots:
Coming Soon.




Protection Domains:
Coming Soon.





Quality of Service:
Coming Soon.




MDM:
Coming Soon.




SDC:
Coming Soon.





SDS:
Coming Soon.




And More.... (hopefully soon :)


