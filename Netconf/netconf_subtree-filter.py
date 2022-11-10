from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_scrapli.tasks import netconf_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

# pyang -f sample-xml-skeleton ietf-interfaces.yang
filter = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name/>
      <description/>
      <type/>
      <link-up-down-trap-enable/>
    </interface>
  </interfaces>
"""
# filter2 = """
# <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
# </interfaces>
# """


def get_device_config(task):
    task.run(task=netconf_get_config, source="running", filter_type="subtree", filter_=filter)
  
# def get_device_config(task):
#     task.run(task=netconf_get, filter_type="subtree", filter_=filter2)
  
results = nr.run(task=get_device_config)
print_result(results)