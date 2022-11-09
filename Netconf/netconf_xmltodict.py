from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get
from nornir_utils.plugins.functions import print_result
import xmltodict

nr = InitNornir(config_file="config.yaml")

def get_yang(task):
    task.run(task=netconf_get, filter_type="xpath", filter_="interfaces-state//statistics[in-unicast-pkts > 0]")

result = nr.run(task=get_yang)
print_result(result)