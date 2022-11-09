import requests
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result
# import ipdb

nr = InitNornir(config_file="config.yaml")
requests.packages.urllib3.disable_warnings()

headers = {
    "Accept": "application/yang-data+json"
}

def restconf_test(task):
    url = f"https://{task.host.hostname}:{task.host.port}/restconf/data/native/router/Cisco-IOS-XE-bgp:bgp=65001/neighbor=12.12.12.12"
    response = requests.get(url=url, 
                            headers=headers, 
                            auth=(f"{task.host.username}", f"{task.host.password}"), 
                            verify=False)
    task.host["facts"] = response.json()
    asn = task.host["facts"]["Cisco-IOS-XE-bgp:neighbor"]["remote-as"]
    peer = task.host["facts"]["Cisco-IOS-XE-bgp:neighbor"]["id"]
    print(f"Neighbor {peer} is part of asn: {asn}")
    return Result(host=task.host, result=response.text)
    
result = nr.run(restconf_test)
# print_result(result)
# ipdb.set_trace()