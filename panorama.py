'''
Python script

This script was written to authenticate to a Palo Alto Networks Panorama management platform. 

Author: TJones
Date: 9MAY2021
Name: panorama.py

Original info pulled from:
https://live.paloaltonetworks.com/t5/automation-api-discussions/how-to-retreive-predefined-applications-from-panorama-using-pan/td-p/401447

'''

from panos.panorama import Panorama

pano = Panorama($ip, $login, $password)
pano.predefined.refreshall_applications()

print("Applications: {0}".format(
    pano.predefined.application_objects.keys()),
)

print("Application Containers: {0}".format(
    pano.predefined.application_container_objects.keys()),
)
