from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def yangsuite_test(task):
    task.run(task=netconf_get_config, source="running", filter_="/native/hostname", filter_type="xpath")
    
    
result = nr.run(task=yangsuite_test)
print_result(result)