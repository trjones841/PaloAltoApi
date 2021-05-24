'''
Python script

This script was written to retrieve the IP's from Prisma Access (Cloud Managed)

Author: TJones
Date: 20MAY2021
Name: prisma_retrieve_ips.py

'''
import requests
import json

DEBUG = True

def prisma_managed_retrieve_ips(url, api_key, path, method, payload):

    full_url = "https://" + url + "/" + path
    headers = {'header-api-key': api_key}
    # Do not use verify=False in prod. Use valid certificate or provide directory to CA cert
    #   i.e. - requests.get('https://mydomain.com', verify='/path/to/certfile')
    requests.packages.urllib3.disable_warnings()

    try:
        response = requests.request(method, full_url, headers=headers, data=payload, verify=False)
        if str(response.status_code) == '200':
            return response.json()
        else:
            raise Exception('Session ID was not received by device. Verify connectivity.')
    except Exception as e:
        if DEBUG:
            print('IP retrieval method::Issue Occurred::', e)
        else:
            exit()


if __name__ == '__main__':

    url = 'api.lab.gpcloudservice.com'
    api_key = 'adypiixf09__ww2vsY9lLSrebVihF6ym6xGcwI8vZmP5VDGwciR1'
    path = 'getPrismaAccessIP/v2'
    method = 'POST'
    payload = '{"serviceType": "all", "addrType": "all","location": "all"}'

    print(json.dumps(prisma_managed_retrieve_ips(url, api_key, path, method, payload), indent=4))
