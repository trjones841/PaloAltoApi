'''
Python script

This script was written to authenticate to a PAN-OS firewall.

Author: TJones
Date: 8MAY2021
Name: panfw_auth_session.py

Auth URL: https://<firewall>/api/?type=keygen&user=<username>&password=<password>

'''
import requests
import xmltodict

DEBUG = True

def login_to_panfw(ipaddr, username, passwd):
    url = "https://" + ipaddr + "/api/"
    parameters = {'type':'keygen', 'user': username, 'password': passwd}
    #print('URL: ', url)
    #print('parameters: ', parameters)

    # Do not use verify=False in prod. Use valid certificate or provide directory to CA cert
    #   i.e. - requests.get('https://mydomain.com', verify='/path/to/certfile')
    requests.packages.urllib3.disable_warnings()
    try:
        response = requests.request("GET", url, params=parameters, verify=False)
        #print(response.url)
        dict_data = xmltodict.parse(response.content)
        auth_key = dict_data['response']['result']['key']
        if str(response.status_code) == '200':
            return auth_key
        else:
            raise Exception('Session ID was not received by device. Verify connectivity.')
    except Exception as e:
        if DEBUG:
            print('login_to_panfw::Issue Occurred::', e)
        else:
            exit()


if __name__ == '__main__':
    
    username = 'admin'
    passwd = 'password'
    PANFW01 = '10.40.1.101'  # v10.0
    PANFW02 = '10.40.1.102'  #v11.1
    auth_token = login_to_panfw(PANFW01, username, passwd)
    print('\napi_key: ', auth_token)
