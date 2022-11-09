import requests

# Disable cert warnings
requests.packages.urllib3.disable_warnings()

device = {
    "host": "192.168.2.12",
    "port": 443,
    "username": "okan",
    "password": "hollander"
}

headers = {
    "Accept": "application/yang-data+json"
}

url = f"https://{device['host']}:{device['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

response = requests.get(url=url, headers=headers, auth=(device["username"], device["password"]), verify=False)

response.raise_for_status()

print(response.text)