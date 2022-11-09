from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

filter = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
</interfaces>
"""


def get_device_config(task):
    task.run(task=netconf_get_config, source="running", filter_type="subtree", filter_=filter)
    
results = nr.run(task=get_device_config)
print_result(results)