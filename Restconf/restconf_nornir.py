import requests
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result

nr = InitNornir(config_file="config.yaml")
requests.packages.urllib3.disable_warnings()

headers = {
    "Accept": "application/yang-data+json"
}

def restconf_test(task):
    url = f"https://{task.host.hostname}:{task.host.port}/restconf/data/native"
    response = requests.get(url=url, 
                            headers=headers, 
                            auth=(f"{task.host.username}", f"{task.host.password}"), 
                            verify=False)
    print(response.text)
    
nr.run(restconf_test)