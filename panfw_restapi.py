'''
Python script

This script was written to pull interface information from PAN-OS using restAPI

Author: TJones
Date: 8MAY2021
Name: panfw_restpai.py


'''
import requests
import json
from panfw_auth_session import login_to_panfw

DEBUG = True

ip = '10.40.1.101'
user = 'admin'
passwd = 'password'

# Global variable call for api_key
api_key = login_to_panfw(ip, user, passwd)


def vlaninterfaces():

    url = "https://" + ip + "/restapi/v10.0/Network/VLANInterfaces"
    headers = {'X-PAN-KEY': api_key}
    # Do not use verify=False in prod. Use valid certificate or provide directory to CA cert
    #   i.e. - requests.get('https://mydomain.com', verify='/path/to/certfile')
    requests.packages.urllib3.disable_warnings()
    try:
        response = requests.request("GET", url, headers=headers, verify=False)
        #print(response.json())
        if str(response.status_code) == '200':
            return response.json()
        else:
            raise Exception('Session ID was not received by device. Verify connectivity.')
    except Exception as e:
        if DEBUG:
            print('login_to_panfw::Issue Occurred::', e)
        else:
            exit()


if __name__ == '__main__':

    print(json.dumps(vlaninterfaces(), indent=4))
