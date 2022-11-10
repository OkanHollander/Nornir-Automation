import requests
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result

nr = InitNornir(config_file="config.yaml")
requests.packages.urllib3.disable_warnings()

headers = {
    "Accept": "application/yang-data+json"
}

def restconf_data(task):
    url = f"https://{task.host.hostname}:{task.host.port}/restconf/data/openconfig-interfaces:interfaces?content=config" # noconfig for state data
    response = requests.get(url=url, 
                            headers=headers, 
                            auth=(f"{task.host.username}", f"{task.host.password}"), 
                            verify=False)
    return Result(host=task.host, result=response.text)

result = nr.run(task=restconf_data)
print_result(result)