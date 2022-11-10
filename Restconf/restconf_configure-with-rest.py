import requests
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result

nr = InitNornir(config_file="config.yaml")
requests.packages.urllib3.disable_warnings()

headers = {
    "Accept": "application/yang-data+json"
}

# Get the yang model with pyang
# drill into the data and query for the config files
# copy the output and convert the json format into yaml
# create the host file in host_vars/hostname.yaml
# paste the config in the file and create another python file to load the data in memory
# 

def rest_config(task):
    url = f"https://{task.host.hostname}:{task.host.port}/restconf/data/openconfig-acl:acl?content=config"
    response = requests.get(url=url, 
                            headers=headers, 
                            auth=(f"{task.host.username}", f"{task.host.password}"),
                            verify=False)
    return Result(host=task.host, result=response.text)

result = nr.run(task=rest_config)
print_result(result)