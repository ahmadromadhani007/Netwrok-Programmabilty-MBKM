import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers = {"X-Auth-Token": "NC-31-586811f4e1ed414fb82a-nbi"}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
networkDevices = response_json["response"]

for networkDevices in networkDevices:
    print(networkDevices["hostname"], "\t", networkDevices["platformId"],
          "\t", networkDevices["managementIpAddress"])
