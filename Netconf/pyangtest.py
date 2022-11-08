from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

filter_test = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name/>
      <description/>
    </interface>
  </interfaces>
"""

def yangsuite_test(task):
    task.run(task=netconf_get_config, source="running", filter_=filter_test, filter_type="subtree")
    
    
result = nr.run(task=yangsuite_test)
print_result(result)